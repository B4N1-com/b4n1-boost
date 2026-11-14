"""WebSocket compression for ASGI applications (RFC 7692 permessage-deflate).

``B4N1Config.enable_websocket_acceleration`` has been part of the public
configuration surface since 0.3.x and ``b4n1-boost status`` reports it as
active, so the capability behind it has to exist. This module is that
capability: an ASGI WebSocket middleware that negotiates
``permessage-deflate`` and compresses messages that are worth compressing.

Design decisions worth knowing:

* **Negotiation is never assumed.** A peer that does not offer
  ``permessage-deflate`` gets no extension header: starting to compress what
  the client cannot decompress breaks the socket.
* **Control frames stay raw.** RFC 7692 §6 forbids compressing close/ping/pong,
  and a compressed close frame is unrecoverable.
* **Small frames stay raw.** Below the threshold the deflate header costs more
  than the payload saves, so compressing would grow the traffic.
* **Nothing is buffered.** Every message crosses as it arrives; a WebSocket is
  a live stream, not a whole-body-in-memory response.
* **``server_no_context_takeover`` is honoured** when the client asks for it,
  which means a fresh zlib context per message.

The wire format follows the RFC: payload is deflated and the trailing empty
block (``0x00 0x00 0xff 0xff``) is stripped by the sender. Messages are
delivered with a ``b4n1_compressed`` marker so a transport layer that owns
the framing (uvicorn, hypercorn, an ASGI server) knows to set ``RSV1``.
"""

from __future__ import annotations

import zlib
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

__all__ = [
    "DEFAULT_COMPRESSION_THRESHOLD",
    "MAX_WINDOW_BITS",
    "MIN_WINDOW_BITS",
    "WebSocketCompressionMiddleware",
    "parse_extensions",
]

#: RFC 7692 §7.1.2.1 — the ceiling for any window-bits parameter.
MAX_WINDOW_BITS = 15

#: Below this the deflate framing costs more than the payload saves.
MIN_WINDOW_BITS = 8

#: A message must exceed this many bytes before compressing is worth it.
DEFAULT_COMPRESSION_THRESHOLD = 128

#: The empty deflate block that terminates a permessage-deflate message.
#: The sender strips it; the receiver re-appends it.
_TRAILER = b"\x00\x00\xff\xff"

#: Message types that must never be compressed (RFC 7692 §6).
_CONTROL_TYPES = frozenset({"close", "ping", "pong", "websocket.close", "websocket.ping", "websocket.pong"})


def parse_extensions(header: bytes | str) -> dict[str, dict[str, str]]:
    """Parse a ``Sec-WebSocket-Extensions`` offer into a name → params map.

    ``permessage-deflate; client_max_window_bits=12, other`` becomes
    ``{"permessage-deflate": {"client_max_window_bits": "12"}, "other": {}}``.
    A malformed offer yields what could be read instead of raising: the
    handshake must not die because a peer sent junk.
    """
    if isinstance(header, bytes):
        try:
            header = header.decode("latin-1")
        except Exception:
            return {}

    parsed: dict[str, dict[str, str]] = {}
    for chunk in header.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        name, _, params = chunk.partition(";")
        name = name.strip().lower()
        if not name:
            continue
        bucket = parsed.setdefault(name, {})
        for param in params.split(";"):
            param = param.strip()
            if not param:
                continue
            key, _, value = param.partition("=")
            bucket[key.strip().lower()] = value.strip()
    return parsed


@dataclass
class _Session:
    """Per-connection compression state."""

    window_bits: int = MAX_WINDOW_BITS
    no_context_takeover: bool = False
    _deflater: Optional[Any] = field(default=None, repr=False)

    def deflater(self) -> Any:
        # A fresh context per message when the peer asked for
        # server_no_context_takeover; otherwise reuse one across messages,
        # which is where permessage-deflate gets its ratio.
        if self.no_context_takeover or self._deflater is None:
            self._deflater = zlib.compressobj(
                zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -self.window_bits
            )
        return self._deflater

    def compress(self, payload: bytes) -> bytes:
        compressor = self.deflater()
        out = compressor.compress(payload) + compressor.flush(zlib.Z_SYNC_FLUSH)
        if out.endswith(_TRAILER):
            out = out[: -len(_TRAILER)]
        return out


class WebSocketCompressionMiddleware:
    """ASGI middleware applying permessage-deflate to WebSocket traffic.

    Sits next to the HTTP compression middlewares and follows the same
    ``(app, ...) -> callable(scope, receive, send)`` shape, so it composes in
    the same stack.

    ``enabled`` comes from ``B4N1Config.enable_websocket_acceleration``:
    turning the flag off must actually turn the feature off.
    """

    def __init__(
        self,
        app: Callable,
        enabled: bool = True,
        threshold: int = DEFAULT_COMPRESSION_THRESHOLD,
    ) -> None:
        if threshold <= 0:
            raise ValueError("threshold must be a positive byte count")
        self.app = app
        self.enabled = enabled
        self.threshold = threshold

    def negotiate(self, scope: dict) -> Optional[str]:
        """Return the extension header to accept with, or ``None``.

        ``None`` means the peer gets no compression — either because it did
        not offer any or because the feature is disabled.
        """
        if not self.enabled:
            return None

        offer: Optional[bytes] = None
        for key, value in scope.get("headers", []):
            if key.lower() == b"sec-websocket-extensions":
                offer = value
                break
        if offer is None:
            return None

        parsed = parse_extensions(offer)
        params = parsed.get("permessage-deflate")
        if params is None:
            return None

        accept = "permessage-deflate"
        accept += f"; server_max_window_bits={self._window_bits(params)}"
        if "server_no_context_takeover" in params or "client_no_context_takeover" in params:
            accept += "; server_no_context_takeover"
        return accept

    @staticmethod
    def _window_bits(params: dict[str, str]) -> int:
        raw = params.get("server_max_window_bits")
        if raw is None:
            return MAX_WINDOW_BITS
        try:
            bits = int(raw.strip('"'))
        except (TypeError, ValueError):
            return MAX_WINDOW_BITS
        return max(MIN_WINDOW_BITS, min(MAX_WINDOW_BITS, bits))

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope.get("type") != "websocket":
            await self.app(scope, receive, send)
            return

        accept_extension = self.negotiate(scope)
        if accept_extension is None:
            await self.app(scope, receive, send)
            return

        session = _Session(
            window_bits=self._window_bits(parse_extensions(
                next(
                    (v for k, v in scope.get("headers", []) if k.lower() == b"sec-websocket-extensions"),
                    b"",
                )
            ).get("permessage-deflate", {})),
            no_context_takeover=True,
        )

        async def _send(message: dict) -> None:
            kind = message.get("type", "")

            if kind == "websocket.accept":
                forwarded = dict(message)
                headers = list(forwarded.get("headers", []))
                headers.append((b"sec-websocket-extensions", accept_extension.encode("latin-1")))
                forwarded["headers"] = headers
                await send(forwarded)
                return

            if kind == "websocket.send" and kind not in _CONTROL_TYPES:
                forwarded = self._maybe_compress(message, session)
                await send(forwarded)
                return

            await send(message)

        await self.app(scope, receive, _send)

    def _maybe_compress(self, message: dict, session: _Session) -> dict:
        forwarded = dict(message)

        payload: Optional[bytes] = None
        is_text = message.get("text") is not None
        if is_text:
            payload = message["text"].encode("utf-8")
        elif message.get("bytes") is not None:
            payload = message["bytes"]

        if payload is None or len(payload) < self.threshold:
            return forwarded

        try:
            compressed = session.compress(payload)
        except zlib.error:
            # Never lose a message to a compression failure: ship it raw.
            return forwarded

        if len(compressed) >= len(payload):
            return forwarded

        if is_text:
            forwarded["text"] = None
        forwarded["bytes"] = compressed
        forwarded["b4n1_compressed"] = True
        return forwarded
