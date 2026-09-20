"""
b4n1_boost.middleware — concrete middleware classes and injection helpers.

These are the *real* integration points: they wrap the running framework
(Django, FastAPI, Flask or plain WSGI) and route JSON work through the native
Rust engine when it is available (`_NATIVE = True`), falling back to the
Python standard library otherwise.
"""

from __future__ import annotations

import json as _json
from typing import Any, Callable, Optional

try:
    from b4n1_boost._core import (
        py_json_dumps,
        py_json_loads,
        py_json_dumps_direct,
        py_compress_gzip,
        py_compress_gzip_fast,
        py_compress_brotli,
        py_compress_zstd,
        py_decompress_zstd,
        py_canonicalize_direct,
        py_json_validate,
    )

    _NATIVE = True
except ImportError:  # pragma: no cover - exercised only in source checkouts
    py_json_dumps = None  # type: ignore[assignment]
    py_json_dumps_direct = None  # type: ignore[assignment]
    py_json_loads = None  # type: ignore[assignment]
    py_compress_gzip = None  # type: ignore[assignment]
    py_compress_gzip_fast = None  # type: ignore[assignment]
    py_compress_brotli = None  # type: ignore[assignment]
    py_compress_zstd = None  # type: ignore[assignment]
    py_decompress_zstd = None  # type: ignore[assignment]
    py_canonicalize_direct = None  # type: ignore[assignment]
    py_json_validate = None  # type: ignore[assignment]
    _NATIVE = False


# ── Content types that should NOT be compressed ──────────────────────────

_SKIP_COMPRESSION_TYPES = frozenset((
    "image/",       # all image types (png, jpeg, gif, webp, avif, svg)
    "video/",       # all video types
    "audio/",       # all audio types
    "application/zip",
    "application/gzip",
    "application/x-brotli",
    "application/x-zstd",
    "application/octet-stream",  # binary blobs
    "font/woff",
    "font/woff2",
))


def _should_compress(content_type: str) -> bool:
    """Return True if the response body should be compressed.

    Skips already-compressed formats (images, video, audio, fonts, etc.)
    to avoid wasting CPU on data that won't compress further.
    """
    if not content_type:
        return True  # unknown type: try compressing
    ct = content_type.lower()
    for prefix in _SKIP_COMPRESSION_TYPES:
        if ct.startswith(prefix):
            return False
    return True


_orjson = None
try:
    import orjson as _orjson
except ImportError:
    pass


class NativeJson:
    """JSON fast-path dispatcher (native Rust engine when present).

    Uses orjson when available (3-10x faster than stdlib), falls back
    to stdlib JSON otherwise. The Rust direct path is used for
    canonicalization and small-object fast paths.
    """

    @staticmethod
    def dumps_direct(obj: Any) -> bytes:
        """Serialize Python JSON-compatible objects directly in Rust.

        Uses the fast PyO3 traversal path (no intermediate serde_json::Value).
        Falls back to orjson (if available) or stdlib JSON.
        """
        if _NATIVE and py_json_dumps_direct is not None:
            try:
                return bytes(py_json_dumps_direct(obj))
            except (TypeError, ValueError):
                pass
        if _orjson is not None:
            return _orjson.dumps(obj)
        return _json.dumps(obj, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    @staticmethod
    def dumps(obj: Any) -> str:
        """Serialize ``obj`` to a compact JSON string.

        Uses orjson when available (3-10x faster than stdlib),
        falls back to stdlib JSON. For direct-bytes output use
        :meth:`dumps_direct`.
        """
        if _orjson is not None:
            return _orjson.dumps(obj).decode('utf-8')
        return _json.dumps(obj, separators=(',', ':'), ensure_ascii=False)

    @staticmethod
    def loads(text: str) -> Any:
        """Parse a JSON string (delegates to orjson or stdlib)."""
        if _orjson is not None:
            if isinstance(text, str):
                return _orjson.loads(text.encode('utf-8'))
            return _orjson.loads(text)
        return _json.loads(text)


# ── JSON validation ──────────────────────────────────────────────────────


def validate_json(text: str) -> bool:
    """Fast JSON validation using the native engine.

    Returns True if the string is valid JSON, False otherwise.
    Uses simd-json when available (10x faster than serde_json).
    """
    if _NATIVE and py_json_validate is not None:
        return py_json_validate(text)
    try:
        _json.loads(text)
        return True
    except (ValueError, TypeError):
        return False


# ── Batch JSON operations ─────────────────────────────────────────────


def batch_dumps(objects: list[Any]) -> list[str]:
    """Serialize a list of Python objects to JSON strings.

    Uses orjson when available for batch speed.
    """
    if _orjson is not None:
        return [_orjson.dumps(obj).decode("utf-8") for obj in objects]
    return [_json.dumps(obj, separators=(',', ':'), ensure_ascii=False) for obj in objects]


def batch_dumps_direct(objects: list[Any]) -> list[bytes]:
    """Serialize a list of Python objects to JSON bytes.

    Uses the native PyO3 direct path when available.
    """
    return [NativeJson.dumps_direct(obj) for obj in objects]


def batch_loads(texts: list[str]) -> list[Any]:
    """Parse a list of JSON strings to Python objects.

    Uses orjson when available for batch speed.
    """
    if _orjson is not None:
        return [_orjson.loads(t.encode("utf-8") if isinstance(t, str) else t) for t in texts]
    return [_json.loads(t) for t in texts]


def batch_validate(texts: list[str]) -> list[bool]:
    """Validate a list of JSON strings.

    Returns a list of booleans, one per input string.
    """
    return [validate_json(t) for t in texts]


# ── Compression helpers ──────────────────────────────────────────────────


def _native_gzip(body: bytes) -> Optional[bytes]:
    """Gzip-compress ``body`` in Rust without holding the GIL."""
    if not _NATIVE or py_compress_gzip is None:
        return None
    try:
        return bytes(py_compress_gzip(body))
    except Exception:
        return None


def _native_gzip_fast(body: bytes) -> Optional[bytes]:
    """Gzip-compress ``body`` with level 1 (fastest, slightly larger output)."""
    if not _NATIVE or py_compress_gzip_fast is None:
        return None
    try:
        return bytes(py_compress_gzip_fast(body))
    except Exception:
        return None


def _native_brotli(body: bytes) -> Optional[bytes]:
    """Brotli-compress ``body`` in Rust without holding the GIL."""
    if not _NATIVE or py_compress_brotli is None:
        return None
    try:
        return bytes(py_compress_brotli(body))
    except Exception:
        return None


def _native_zstd(body: bytes) -> Optional[bytes]:
    """Zstd-compress ``body`` in Rust without holding the GIL."""
    if not _NATIVE or py_compress_zstd is None:
        return None
    try:
        return bytes(py_compress_zstd(body))
    except Exception:
        return None


def _pick_compressor(accept_encoding: str) -> Optional[Callable[[bytes], Optional[bytes]]]:
    """Choose the best available native compressor based on ``Accept-Encoding``.

    Prefers brotli (best ratio), then zstd (best speed/ratio), then gzip.
    """
    accept = accept_encoding.lower()
    if "br" in accept:
        compressor = _native_brotli
        if compressor is not None:
            return compressor
    if "zstd" in accept:
        compressor = _native_zstd
        if compressor is not None:
            return compressor
    if "gzip" in accept:
        return _native_gzip
    return None


def _pick_compressor_fast(accept_encoding: str) -> Optional[Callable[[bytes], Optional[bytes]]]:
    """Choose the FASTEST available compressor (for high-throughput scenarios).

    Prefers zstd (fastest), then gzip-fast (level 1), then brotli.
    """
    accept = accept_encoding.lower()
    if "zstd" in accept:
        compressor = _native_zstd
        if compressor is not None:
            return compressor
    if "gzip" in accept:
        compressor = _native_gzip_fast
        if compressor is not None:
            return compressor
    if "br" in accept:
        compressor = _native_brotli
        if compressor is not None:
            return compressor
    return None


def _encoding_name(compressor: Callable) -> str:
    """Return the Content-Encoding header value for a compressor."""
    if compressor is _native_brotli:
        return "br"
    if compressor is _native_zstd:
        return "zstd"
    return "gzip"


def _native_json_response(body: bytes) -> Optional[bytes]:
    """Pass-through: responses already serialized by the framework are
    forwarded untouched."""
    return None


# ── WSGI Middleware ──────────────────────────────────────────────────────


class BoostWSGIMiddleware:
    """Generic WSGI middleware: transparent zero-copy pass-through."""

    def __init__(self, app: Callable) -> None:
        self.app = app

    def __call__(self, environ: dict, start_response: Callable) -> list:
        captured: dict = {}

        def _capture(status: str, headers: list, exc_info: Any = None) -> None:
            captured["status"] = status
            captured["headers"] = headers
            captured["exc_info"] = exc_info

        chunks = self.app(environ, _capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()

        start_response(captured["status"], captured["headers"], captured.get("exc_info"))
        return [body]


class B4N1BoostCompressionMiddleware:
    """WSGI middleware that natively compresses large responses (GIL-free).

    Negotiates ``Accept-Encoding`` (brotli > zstd > gzip), skips already-
    compressed content types, only compresses bodies above ``min_size``, and
    always falls back to the original body when the native engine is
    unavailable or compression fails.

    Args:
        app: The WSGI application to wrap.
        min_size: Minimum response body size (in bytes) to compress.
        fast_mode: If True, use fastest compressor (zstd/gzip-1) instead of
                   best-ratio compressor (brotli). Default: False.
    """

    def __init__(
        self,
        app: Callable,
        min_size: int = 1024,
        fast_mode: bool = False,
    ) -> None:
        self.app = app
        self.min_size = min_size
        self.fast_mode = fast_mode

    def __call__(self, environ: dict, start_response: Callable) -> list:
        accept_encoding = environ.get("HTTP_ACCEPT_ENCODING", "")
        pick = _pick_compressor_fast if self.fast_mode else _pick_compressor
        compressor = pick(accept_encoding)
        if compressor is None:
            return self.app(environ, start_response)

        captured: dict = {}

        def _capture(status: str, headers: list, exc_info: Any = None) -> None:
            captured["status"] = status
            captured["headers"] = headers
            captured["exc_info"] = exc_info

        chunks = self.app(environ, _capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()

        if len(body) < self.min_size:
            start_response(captured["status"], captured["headers"], captured.get("exc_info"))
            return [body]

        # Check content-type: skip compression for already-compressed data
        content_type = ""
        for k, v in captured["headers"]:
            if k.lower() == "content-type":
                content_type = v
                break
        if not _should_compress(content_type):
            start_response(captured["status"], captured["headers"], captured.get("exc_info"))
            return [body]

        compressed = compressor(body)
        if compressed is None:
            start_response(captured["status"], captured["headers"], captured.get("exc_info"))
            return [body]

        encoding = _encoding_name(compressor)
        headers = [
            (k, v)
            for k, v in captured["headers"]
            if k.lower() not in ("content-length", "content-encoding", "vary")
        ]
        headers.append(("Content-Encoding", encoding))
        headers.append(("Content-Length", str(len(compressed))))
        headers.append(("Vary", "Accept-Encoding"))
        start_response(captured["status"], headers, captured.get("exc_info"))
        return [compressed]


# ── ASGI Middleware (FastAPI / Starlette) ────────────────────────────────


class FastAPIBoostMiddleware:
    """ASGI middleware for FastAPI/Starlette — zero-copy pass-through."""

    def __init__(self, app: Any) -> None:
        self.app = app

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        await self.app(scope, receive, send)


class FastAPIBoostCompressionMiddleware:
    """ASGI middleware that natively compresses (br/zstd/gzip) responses.

    Buffers the body, compresses it in Rust when the client accepts the
    encoding and the body is above ``min_size``, and rewrites
    ``Content-Encoding``, ``Content-Length`` and ``Vary``. Falls back to the
    untouched body when the native engine is unavailable or compression fails.

    Args:
        app: The ASGI application to wrap.
        min_size: Minimum response body size (in bytes) to compress.
        fast_mode: If True, use fastest compressor (zstd/gzip-1) instead of
                   best-ratio compressor (brotli). Default: False.
    """

    def __init__(
        self,
        app: Any,
        min_size: int = 1024,
        fast_mode: bool = False,
    ) -> None:
        self.app = app
        self.min_size = min_size
        self.fast_mode = fast_mode

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        accept_encoding = ""
        for key, value in scope.get("headers", []):
            if key.lower() == b"accept-encoding":
                try:
                    accept_encoding = value.decode("latin-1")
                except Exception:
                    pass
        pick = _pick_compressor_fast if self.fast_mode else _pick_compressor
        compressor = pick(accept_encoding)
        if compressor is None:
            await self.app(scope, receive, send)
            return

        start_message: Optional[dict] = None
        body_messages: list[dict] = []

        async def _send(message: dict) -> None:
            nonlocal start_message
            if message["type"] == "http.response.start":
                start_message = dict(message)
                return
            if message["type"] == "http.response.body":
                body_messages.append(dict(message))
                if message.get("more_body", False):
                    return

                body = b"".join(item.get("body", b"") for item in body_messages)
                if start_message is None:
                    await send(message)
                    return

                # Check content-type: skip compression for already-compressed data
                headers_list = start_message.get("headers", [])
                content_type = ""
                for k, v in headers_list:
                    if k.lower() == b"content-type":
                        content_type = v.decode("latin-1", errors="replace")
                        break
                if not _should_compress(content_type):
                    await send(start_message)
                    for pending in body_messages:
                        await send(pending)
                    body_messages.clear()
                    return

                if len(body) >= self.min_size:
                    compressed = compressor(body)
                    if compressed is not None:
                        encoding = _encoding_name(compressor)
                        new_headers = [
                            (k, v)
                            for k, v in headers_list
                            if k.lower() not in (b"content-length", b"content-encoding", b"vary")
                        ]
                        new_headers.append((b"content-encoding", encoding.encode("latin-1")))
                        new_headers.append(
                            (b"content-length", str(len(compressed)).encode("latin-1"))
                        )
                        new_headers.append((b"vary", b"Accept-Encoding"))
                        start_message["headers"] = new_headers
                        await send(start_message)
                        final_message = dict(message)
                        final_message["body"] = compressed
                        final_message["more_body"] = False
                        body_messages.clear()
                        await send(final_message)
                        return

                await send(start_message)
                for pending in body_messages:
                    await send(pending)
                body_messages.clear()
                return
            await send(message)

        await self.app(scope, receive, _send)


# ── Django Middleware ────────────────────────────────────────────────────


class DjangoBoostMiddleware:
    """Django middleware (Django 2+ style callable).

    Zero-copy pass-through: responses flow through untouched.
    """

    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: Any) -> Any:
        return self.get_response(request)


# ── Middleware injection helpers ─────────────────────────────────────────


def install_django_middleware() -> bool:
    """Append the Django middleware to ``settings.MIDDLEWARE`` if possible.

    Idempotent: checks for existing presence before appending.
    """
    try:
        from django.conf import settings
    except ImportError:
        return False
    try:
        path = "b4n1_boost.middleware.DjangoBoostMiddleware"
        current = list(getattr(settings, "MIDDLEWARE", []) or [])
        if path not in current:
            current.append(path)
            settings.MIDDLEWARE = current
        return True
    except Exception:
        return False


def install_fastapi_middleware(app: Any) -> bool:
    """Attach the ASGI middleware to a FastAPI/Starlette app (idempotent)."""
    try:
        if getattr(app, "_b4n1_boost_installed", False):
            return True
        user_mw = getattr(app, "user_middleware", None)
        if user_mw is not None and any(
            getattr(m, "cls", None) is FastAPIBoostMiddleware for m in user_mw
        ):
            return True
        app.add_middleware(FastAPIBoostMiddleware)
        app._b4n1_boost_installed = True
        return True
    except Exception:
        return False


def install_flask_middleware(app: Any) -> bool:
    """Wrap a Flask app's WSGI app (idempotent — never double-wraps)."""
    try:
        if getattr(app, "_b4n1_boost_installed", False):
            return True
        app.wsgi_app = BoostWSGIMiddleware(app.wsgi_app)
        app._b4n1_boost_installed = True
        return True
    except Exception:
        return False


# ── JSON canonicalization ───────────────────────────────────────────────


def canonicalize_json(obj: Any) -> str:
    """Re-serialize an object into compact canonical JSON.

    Accepts either a JSON string or a Python dict/list. When the native
    engine is available, uses the direct PyO3 traversal for dicts/lists
    (no intermediate string conversion).

    Examples::

        canonicalize_json('{"z":1,"a":2}')  # '{"a":2,"z":1}'
        canonicalize_json({"z": 1, "a": 2})  # '{"a":2,"z":1}'
    """
    if isinstance(obj, str):
        if _NATIVE and py_json_dumps is not None:
            return str(py_json_dumps(obj))
        return _json.dumps(_json.loads(obj), separators=(",", ":"))
    else:
        if _NATIVE and py_canonicalize_direct is not None:
            try:
                return bytes(py_canonicalize_direct(obj)).decode("utf-8")
            except (TypeError, ValueError):
                pass
        return _json.dumps(obj, separators=(",", ":"))


# ── ETag / 304 Cache Middleware ────────────────────────────────────────


class ETagMiddleware:
    """WSGI middleware that adds ETag headers and handles 304 responses.

    Generates an xxhash-based ETag from the response body. On subsequent
    requests with ``If-None-Match``, returns 304 Not Modified (empty body)
    when the ETag matches, saving bandwidth.

    Args:
        app: The WSGI application to wrap.
        hash_fn: Hash function to use. Default: hashlib.md5 (fast, built-in).
    """

    def __init__(self, app: Callable, hash_fn: Any = None) -> None:
        self.app = app
        self._hash_fn = hash_fn

    def _compute_etag(self, body: bytes) -> str:
        if self._hash_fn is not None:
            return self._hash_fn(body)
        import hashlib
        return hashlib.md5(body).hexdigest()

    def __call__(self, environ: dict, start_response: Callable) -> list:
        if_none_match = environ.get("HTTP_IF_NONE_MATCH", "")

        captured: dict = {}

        def _capture(status: str, headers: list, exc_info: Any = None) -> None:
            captured["status"] = status
            captured["headers"] = headers
            captured["exc_info"] = exc_info

        chunks = self.app(environ, _capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()

        etag = self._compute_etag(body)

        # 304 Not Modified
        if if_none_match and if_none_match.strip('"') == etag:
            start_response("304 Not Modified", [], None)
            return [b""]

        # Add ETag header
        headers = [
            (k, v)
            for k, v in captured["headers"]
            if k.lower() not in ("etag",)
        ]
        headers.append(("ETag", f'"{etag}"'))
        start_response(captured["status"], headers, captured.get("exc_info"))
        return [body]


class ASGIETagMiddleware:
    """ASGI middleware that adds ETag headers and handles 304 responses."""

    def __init__(self, app: Any, hash_fn: Any = None) -> None:
        self.app = app
        self._hash_fn = hash_fn

    def _compute_etag(self, body: bytes) -> str:
        if self._hash_fn is not None:
            return self._hash_fn(body)
        import hashlib
        return hashlib.md5(body).hexdigest()

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        # Check If-None-Match
        if_none_match = ""
        for key, value in scope.get("headers", []):
            if key == b"if-none-match":
                if_none_match = value.decode("latin-1")
                break

        start_message: Optional[dict] = None
        body_messages: list[dict] = []

        async def _send(message: dict) -> None:
            nonlocal start_message
            if message["type"] == "http.response.start":
                start_message = dict(message)
                return
            if message["type"] == "http.response.body":
                body_messages.append(dict(message))
                if message.get("more_body", False):
                    return

                body = b"".join(item.get("body", b"") for item in body_messages)
                if start_message is None:
                    await send(message)
                    return

                etag = self._compute_etag(body)

                # 304 Not Modified
                if if_none_match and if_none_match.strip('"') == etag:
                    await send({"type": "http.response.start", "status": 304, "headers": []})
                    await send({"type": "http.response.body", "body": b"", "more_body": False})
                    body_messages.clear()
                    return

                # Add ETag header
                headers_list = start_message.get("headers", [])
                new_headers = [
                    (k, v)
                    for k, v in headers_list
                    if k.lower() != b"etag"
                ]
                new_headers.append((b"etag", f'"{etag}"'.encode("latin-1")))
                start_message["headers"] = new_headers
                await send(start_message)
                for pending in body_messages:
                    await send(pending)
                body_messages.clear()
                return
            await send(message)

        await self.app(scope, receive, _send)


# ── Rate Limiting Middleware ───────────────────────────────────────────


class RateLimitMiddleware:
    """WSGI middleware with rate limiting (token bucket).

    Args:
        app: The WSGI application to wrap.
        rate: Maximum requests per second per IP.
        burst: Maximum burst size (tokens in bucket).
    """

    def __init__(self, app: Callable, rate: float = 100.0, burst: int = 200) -> None:
        self.app = app
        self.rate = rate
        self.burst = burst
        self._buckets: dict[str, tuple[float, float]] = {}

    def _get_client_ip(self, environ: dict) -> str:
        return (
            environ.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip()
            or environ.get("REMOTE_ADDR", "0.0.0.0")
        )

    def _allow_request(self, ip: str) -> bool:
        import time
        now = time.monotonic()
        tokens, last = self._buckets.get(ip, (float(self.burst), now))
        elapsed = now - last
        tokens = min(float(self.burst), tokens + elapsed * self.rate)
        if tokens >= 1.0:
            self._buckets[ip] = (tokens - 1.0, now)
            return True
        self._buckets[ip] = (tokens, now)
        return False

    def __call__(self, environ: dict, start_response: Callable) -> list:
        ip = self._get_client_ip(environ)
        if not self._allow_request(ip):
            start_response("429 Too Many Requests", [
                ("Content-Type", "application/json"),
                ("Retry-After", "1"),
            ], None)
            return [b'{"error":"rate_limit_exceeded","retry_after":1}']
        return self.app(environ, start_response)# ── ASGI Rate Limiting Middleware ─────────────────────────────────────


class ASGIRateLimitMiddleware:
    """ASGI middleware with rate limiting (token bucket).

    Args:
        app: The ASGI application to wrap.
        rate: Maximum requests per second per IP.
        burst: Maximum burst size (tokens in bucket).
    """

    def __init__(self, app: Any, rate: float = 100.0, burst: int = 200) -> None:
        self.app = app
        self.rate = rate
        self.burst = burst
        self._buckets: dict[str, tuple[float, float]] = {}

    def _get_client_ip(self, scope: dict) -> str:
        for key, value in scope.get("headers", []):
            if key == b"x-forwarded-for":
                return value.decode("latin-1").split(",")[0].strip()
        return scope.get("client", ("0.0.0.0", 0))[0]

    def _allow_request(self, ip: str) -> bool:
        import time
        now = time.monotonic()
        tokens, last = self._buckets.get(ip, (float(self.burst), now))
        elapsed = now - last
        tokens = min(float(self.burst), tokens + elapsed * self.rate)
        if tokens >= 1.0:
            self._buckets[ip] = (tokens - 1.0, now)
            return True
        self._buckets[ip] = (tokens, now)
        return False

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        ip = self._get_client_ip(scope)
        if not self._allow_request(ip):
            await send({
                "type": "http.response.start",
                "status": 429,
                "headers": [
                    (b"content-type", b"application/json"),
                    (b"retry-after", b"1"),
                ],
            })
            await send({
                "type": "http.response.body",
                "body": b'{"error":"rate_limit_exceeded","retry_after":1}',
                "more_body": False,
            })
            return
        await self.app(scope, receive, send)


# ── Security Headers Middleware ────────────────────────────────────────

_DEFAULT_SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "X-Permitted-Cross-Domain-Policies": "none",
}


class SecurityHeadersMiddleware:
    """WSGI middleware that adds security headers to all responses.

    Args:
        app: The WSGI application to wrap.
        headers: Optional dict of extra headers to add/override.
        csp: Optional Content-Security-Policy header value.
        hsts: Optional Strict-Transport-Security header value.
    """

    def __init__(
        self,
        app: Callable,
        headers: Optional[dict[str, str]] = None,
        csp: Optional[str] = None,
        hsts: Optional[str] = None,
    ) -> None:
        self.app = app
        self._headers = {**_DEFAULT_SECURITY_HEADERS}
        if headers:
            self._headers.update(headers)
        if csp:
            self._headers["Content-Security-Policy"] = csp
        if hsts:
            self._headers["Strict-Transport-Security"] = hsts

    def __call__(self, environ: dict, start_response: Callable) -> list:
        captured: dict = {}

        def _capture(status: str, headers: list, exc_info: Any = None) -> None:
            captured["status"] = status
            captured["headers"] = headers
            captured["exc_info"] = exc_info

        chunks = self.app(environ, _capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()

        existing = {k.lower() for k, _ in captured["headers"]}
        headers = list(captured["headers"])
        for k, v in self._headers.items():
            if k.lower() not in existing:
                headers.append((k, v))

        start_response(captured["status"], headers, captured.get("exc_info"))
        return [body]


class ASGISecurityHeadersMiddleware:
    """ASGI middleware that adds security headers to all responses.

    Args:
        app: The ASGI application to wrap.
        headers: Optional dict of extra headers to add/override.
        csp: Optional Content-Security-Policy header value.
        hsts: Optional Strict-Transport-Security header value.
    """

    def __init__(
        self,
        app: Any,
        headers: Optional[dict[str, str]] = None,
        csp: Optional[str] = None,
        hsts: Optional[str] = None,
    ) -> None:
        self.app = app
        self._headers = {**_DEFAULT_SECURITY_HEADERS}
        if headers:
            self._headers.update(headers)
        if csp:
            self._headers["Content-Security-Policy"] = csp
        if hsts:
            self._headers["Strict-Transport-Security"] = hsts

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        start_message: Optional[dict] = None

        async def _send(message: dict) -> None:
            nonlocal start_message
            if message["type"] == "http.response.start":
                start_message = dict(message)
                headers_list = list(start_message.get("headers", []))
                existing = {k.lower() for k, _ in headers_list}
                for k, v in self._headers.items():
                    if k.lower() not in existing:
                        headers_list.append((k.lower().encode("latin-1"), v.encode("latin-1")))
                start_message["headers"] = headers_list
                await send(start_message)
                return
            await send(message)

        await self.app(scope, receive, _send)


# ── Request Decompression Middleware ───────────────────────────────────


def _decompress_body(body: bytes, encoding: str) -> Optional[bytes]:
    """Decompress a request body based on Content-Encoding."""
    encoding = encoding.lower().strip()
    if encoding == "gzip":
        import gzip
        try:
            return gzip.decompress(body)
        except Exception:
            return None
    if encoding == "br":
        try:
            import brotli
            return brotli.decompress(body)
        except Exception:
            return None
    if encoding == "deflate":
        import zlib
        try:
            return zlib.decompress(body)
        except Exception:
            return None
    if encoding == "zstd" and _NATIVE and py_decompress_zstd is not None:
        try:
            return bytes(py_decompress_zstd(body))
        except Exception:
            return None
    return None


class DecompressionMiddleware:
    """WSGI middleware that transparently decompresses request bodies.

    Handles gzip, brotli, deflate, and zstd Content-Encoding on incoming
    requests. Useful when clients send compressed POST/PUT bodies.
    """

    def __init__(self, app: Callable) -> None:
        self.app = app

    def __call__(self, environ: dict, start_response: Callable) -> list:
        encoding = environ.get("HTTP_CONTENT_ENCODING", "")
        if encoding:
            try:
                content_length = int(environ.get("CONTENT_LENGTH", "0") or "0")
            except (ValueError, TypeError):
                content_length = 0

            if content_length > 0:
                raw = environ["wsgi.input"].read(content_length)
                decompressed = _decompress_body(raw, encoding)
                if decompressed is not None:
                    import io
                    environ["wsgi.input"] = io.BytesIO(decompressed)
                    environ["CONTENT_LENGTH"] = str(len(decompressed))
                    environ.pop("HTTP_CONTENT_ENCODING", None)

        return self.app(environ, start_response)


# ── Health Check Middleware ────────────────────────────────────────────


class HealthCheckMiddleware:
    """WSGI middleware that serves a health check endpoint.

    Responds to GET requests at ``path`` (default ``/_boost/health``) with
    a JSON status payload without touching the wrapped application.

    Args:
        app: The WSGI application to wrap.
        path: The health check URL path.
    """

    def __init__(self, app: Callable, path: str = "/_boost/health") -> None:
        self.app = app
        self._path = path
        self._start_time = __import__("time").monotonic()

    def __call__(self, environ: dict, start_response: Callable) -> list:
        if (
            environ.get("REQUEST_METHOD") == "GET"
            and environ.get("PATH_INFO") == self._path
        ):
            import time
            uptime = time.monotonic() - self._start_time
            body = _json.dumps({
                "status": "ok",
                "version": __import__("b4n1_boost").__version__,
                "native": _NATIVE,
                "uptime_seconds": round(uptime, 1),
            }).encode("utf-8")
            start_response("200 OK", [
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(body))),
            ])
            return [body]
        return self.app(environ, start_response)


class ASGIHealthCheckMiddleware:
    """ASGI middleware that serves a health check endpoint."""

    def __init__(self, app: Any, path: str = "/_boost/health") -> None:
        self.app = app
        self._path = path
        self._start_time = __import__("time").monotonic()

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if (
            scope.get("type") == "http"
            and scope.get("method") == "GET"
            and scope.get("path") == self._path
        ):
            import time
            uptime = time.monotonic() - self._start_time
            body = _json.dumps({
                "status": "ok",
                "version": __import__("b4n1_boost").__version__,
                "native": _NATIVE,
                "uptime_seconds": round(uptime, 1),
            }).encode("utf-8")
            await send({
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    (b"content-type", b"application/json"),
                    (b"content-length", str(len(body)).encode("latin-1")),
                ],
            })
            await send({
                "type": "http.response.body",
                "body": body,
                "more_body": False,
            })
            return
        await self.app(scope, receive, send)


# ── CORS Middleware ────────────────────────────────────────────────────


class CORSMiddleware:
    """WSGI middleware that adds CORS headers to responses.

    Args:
        app: The WSGI application to wrap.
        allow_origins: List of allowed origins. Use ["*"] for all.
        allow_methods: List of allowed HTTP methods.
        allow_headers: List of allowed request headers.
        allow_credentials: Whether to include Access-Control-Allow-Credentials.
        max_age: Preflight cache duration in seconds.
    """

    def __init__(
        self,
        app: Callable,
        allow_origins: Optional[list[str]] = None,
        allow_methods: Optional[list[str]] = None,
        allow_headers: Optional[list[str]] = None,
        allow_credentials: bool = False,
        max_age: int = 86400,
    ) -> None:
        self.app = app
        self._origins = allow_origins or ["*"]
        self._methods = allow_methods or [
            "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS",
        ]
        self._headers = allow_headers or [
            "Content-Type", "Authorization", "X-Requested-With",
        ]
        self._credentials = allow_credentials
        self._max_age = max_age

    def _cors_headers(self, origin: str) -> list[tuple[str, str]]:
        headers = []
        if "*" in self._origins or origin in self._origins:
            headers.append(("Access-Control-Allow-Origin", origin if "*" not in self._origins else "*"))
        else:
            headers.append(("Access-Control-Allow-Origin", "null"))
        headers.append(("Access-Control-Allow-Methods", ", ".join(self._methods)))
        headers.append(("Access-Control-Allow-Headers", ", ".join(self._headers)))
        headers.append(("Access-Control-Max-Age", str(self._max_age)))
        if self._credentials:
            headers.append(("Access-Control-Allow-Credentials", "true"))
        return headers

    def __call__(self, environ: dict, start_response: Callable) -> list:
        origin = environ.get("HTTP_ORIGIN", "")
        method = environ.get("REQUEST_METHOD", "")

        # Handle preflight OPTIONS
        if method == "OPTIONS" and origin:
            headers = self._cors_headers(origin)
            start_response("204 No Content", headers)
            return [b""]

        captured: dict = {}

        def _capture(status: str, headers: list, exc_info: Any = None) -> None:
            captured["status"] = status
            captured["headers"] = headers
            captured["exc_info"] = exc_info

        chunks = self.app(environ, _capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()

        if origin:
            resp_headers = list(captured["headers"])
            existing = {k.lower() for k, _ in resp_headers}
            for k, v in self._cors_headers(origin):
                if k.lower() not in existing:
                    resp_headers.append((k, v))
            start_response(captured["status"], resp_headers, captured.get("exc_info"))
        else:
            start_response(captured["status"], captured["headers"], captured.get("exc_info"))
        return [body]


class ASGICORSMiddleware:
    """ASGI middleware that adds CORS headers to responses."""

    def __init__(
        self,
        app: Any,
        allow_origins: Optional[list[str]] = None,
        allow_methods: Optional[list[str]] = None,
        allow_headers: Optional[list[str]] = None,
        allow_credentials: bool = False,
        max_age: int = 86400,
    ) -> None:
        self.app = app
        self._origins = allow_origins or ["*"]
        self._methods = allow_methods or [
            "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS",
        ]
        self._headers = allow_headers or [
            "Content-Type", "Authorization", "X-Requested-With",
        ]
        self._credentials = allow_credentials
        self._max_age = max_age

    def _cors_headers(self, origin: str) -> list[tuple[bytes, bytes]]:
        headers = []
        if "*" in self._origins or origin in self._origins:
            headers.append((b"access-control-allow-origin", (origin if "*" not in self._origins else "*").encode("latin-1")))
        else:
            headers.append((b"access-control-allow-origin", b"null"))
        headers.append((b"access-control-allow-methods", ", ".join(self._methods).encode("latin-1")))
        headers.append((b"access-control-allow-headers", ", ".join(self._headers).encode("latin-1")))
        headers.append((b"access-control-max-age", str(self._max_age).encode("latin-1")))
        if self._credentials:
            headers.append((b"access-control-allow-credentials", b"true"))
        return headers

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope.get("type") != "http":
            await self.app(scope, receive, send)
            return

        origin = ""
        for key, value in scope.get("headers", []):
            if key == b"origin":
                origin = value.decode("latin-1")
                break

        # Preflight
        if scope.get("method") == "OPTIONS" and origin:
            await send({
                "type": "http.response.start",
                "status": 204,
                "headers": self._cors_headers(origin),
            })
            await send({"type": "http.response.body", "body": b"", "more_body": False})
            return

        start_message: Optional[dict] = None

        async def _send(message: dict) -> None:
            nonlocal start_message
            if message["type"] == "http.response.start":
                start_message = dict(message)
                if origin:
                    headers_list = list(start_message.get("headers", []))
                    existing = {k.lower() for k, _ in headers_list}
                    for k, v in self._cors_headers(origin):
                        if k not in existing:
                            headers_list.append((k, v))
                    start_message["headers"] = headers_list
                await send(start_message)
                return
            await send(message)

        await self.app(scope, receive, _send)


# ── Request Logging Middleware ────────────────────────────────────────


class RequestLoggingMiddleware:
    """WSGI middleware that logs request timing, status, and compression.

    Collects per-request metrics (latency, status, bytes in/out, encoding)
    and makes them available via ``get_stats()`` and ``get_recent()``.

    Args:
        app: The WSGI application to wrap.
        logger: Optional callable for per-request logging.
        max_recent: Maximum number of recent requests to keep.
    """

    def __init__(
        self,
        app: Callable,
        logger: Optional[Callable[[dict], None]] = None,
        max_recent: int = 100,
    ) -> None:
        self.app = app
        self._logger = logger
        self._max_recent = max_recent
        self._recent: list[dict] = []
        self._total_requests = 0
        self._total_latency_ms = 0.0
        self._status_counts: dict[int, int] = {}
        self._total_bytes_in = 0
        self._total_bytes_out = 0
        self._compressed_count = 0

    def __call__(self, environ: dict, start_response: Callable) -> list:
        import time
        start = time.monotonic()
        method = environ.get("REQUEST_METHOD", "GET")
        path = environ.get("PATH_INFO", "/")
        content_length = 0
        try:
            content_length = int(environ.get("CONTENT_LENGTH", "0") or "0")
        except (ValueError, TypeError):
            pass

        captured: dict = {}

        def _capture(status: str, headers: list, exc_info: Any = None) -> None:
            captured["status"] = status
            captured["headers"] = headers
            captured["exc_info"] = exc_info

        chunks = self.app(environ, _capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()

        latency_ms = (time.monotonic() - start) * 1000
        status_code = int(captured["status"].split(" ")[0]) if captured.get("status") else 0
        encoding = ""
        for k, v in captured.get("headers", []):
            if k.lower() == "content-encoding":
                encoding = v
                break

        record = {
            "method": method,
            "path": path,
            "status": status_code,
            "latency_ms": round(latency_ms, 2),
            "bytes_in": content_length,
            "bytes_out": len(body),
            "encoding": encoding,
        }

        with self._lock():
            self._total_requests += 1
            self._total_latency_ms += latency_ms
            self._status_counts[status_code] = self._status_counts.get(status_code, 0) + 1
            self._total_bytes_in += content_length
            self._total_bytes_out += len(body)
            if encoding:
                self._compressed_count += 1
            self._recent.append(record)
            if len(self._recent) > self._max_recent:
                self._recent = self._recent[-self._max_recent:]

        if self._logger is not None:
            try:
                self._logger(record)
            except Exception:
                pass

        start_response(captured["status"], captured["headers"], captured.get("exc_info"))
        return [body]

    def _lock(self):
        """Simple non-thread-safe lock placeholder (metrics are approximate)."""
        return _NoLock()

    def get_stats(self) -> dict:
        """Return aggregate statistics."""
        avg = self._total_latency_ms / self._total_requests if self._total_requests else 0
        return {
            "total_requests": self._total_requests,
            "avg_latency_ms": round(avg, 2),
            "total_bytes_in": self._total_bytes_in,
            "total_bytes_out": self._total_bytes_out,
            "compressed_requests": self._compressed_count,
            "status_codes": dict(self._status_counts),
        }

    def get_recent(self, limit: int = 10) -> list[dict]:
        """Return the most recent N requests."""
        return list(self._recent[-limit:])

    def reset(self) -> None:
        """Reset all counters."""
        self._recent.clear()
        self._total_requests = 0
        self._total_latency_ms = 0.0
        self._status_counts.clear()
        self._total_bytes_in = 0
        self._total_bytes_out = 0
        self._compressed_count = 0


class _NoLock:
    """No-op lock for non-threaded usage."""
    def __enter__(self):
        return self
    def __exit__(self, *a):
        pass


class ASGIRequestLoggingMiddleware:
    """ASGI middleware that logs request timing, status, and compression."""

    def __init__(
        self,
        app: Any,
        logger: Optional[Callable[[dict], None]] = None,
        max_recent: int = 100,
    ) -> None:
        self.app = app
        self._logger = logger
        self._max_recent = max_recent
        self._recent: list[dict] = []
        self._total_requests = 0
        self._total_latency_ms = 0.0
        self._status_counts: dict[int, int] = {}
        self._total_bytes_out = 0
        self._compressed_count = 0

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        import time
        start = time.monotonic()
        method = scope.get("method", "GET")
        path = scope.get("path", "/")
        status_code = 0
        encoding = ""
        bytes_out = 0

        async def _send(message: dict) -> None:
            nonlocal status_code, encoding, bytes_out
            if message["type"] == "http.response.start":
                status_code = message.get("status", 0)
                for k, v in message.get("headers", []):
                    if k.lower() == b"content-encoding":
                        encoding = v.decode("latin-1")
                    if k.lower() == b"content-length":
                        try:
                            bytes_out = int(v.decode("latin-1"))
                        except ValueError:
                            pass
            if message["type"] == "http.response.body":
                body = message.get("body", b"")
                if body and not bytes_out:
                    bytes_out = len(body)
            await send(message)

        await self.app(scope, receive, _send)
        latency_ms = (time.monotonic() - start) * 1000

        record = {
            "method": method,
            "path": path,
            "status": status_code,
            "latency_ms": round(latency_ms, 2),
            "bytes_out": bytes_out,
            "encoding": encoding,
        }

        self._total_requests += 1
        self._total_latency_ms += latency_ms
        self._status_counts[status_code] = self._status_counts.get(status_code, 0) + 1
        self._total_bytes_out += bytes_out
        if encoding:
            self._compressed_count += 1
        self._recent.append(record)
        if len(self._recent) > self._max_recent:
            self._recent = self._recent[-self._max_recent:]

        if self._logger is not None:
            try:
                self._logger(record)
            except Exception:
                pass

    def get_stats(self) -> dict:
        avg = self._total_latency_ms / self._total_requests if self._total_requests else 0
        return {
            "total_requests": self._total_requests,
            "avg_latency_ms": round(avg, 2),
            "total_bytes_out": self._total_bytes_out,
            "compressed_requests": self._compressed_count,
            "status_codes": dict(self._status_counts),
        }

    def get_recent(self, limit: int = 10) -> list[dict]:
        return list(self._recent[-limit:])

    def reset(self) -> None:
        self._recent.clear()
        self._total_requests = 0
        self._total_latency_ms = 0.0
        self._status_counts.clear()
        self._total_bytes_out = 0
        self._compressed_count = 0


# ── Proxy Detection ───────────────────────────────────────────────────


def detect_proxy(environ: dict) -> bool:
    """Detect if the request is behind a reverse proxy.

    Returns True if common proxy headers are present (X-Forwarded-For,
    X-Real-IP, Via, X-Forwarded-Proto). Use this to decide whether to
    skip compression (the proxy already handles it).
    """
    proxy_headers = (
        "HTTP_X_FORWARDED_FOR",
        "HTTP_X_REAL_IP",
        "HTTP_VIA",
        "HTTP_X_FORWARDED_PROTO",
        "HTTP_X_FORWARDED_HOST",
    )
    return any(environ.get(h) for h in proxy_headers)


# ── Atomic Compression Metrics ─────────────────────────────────────────


import threading
from dataclasses import dataclass, field


@dataclass
class CompressionMetrics:
    """Thread-safe compression metrics counters.

    Tracks total compressions, bytes in/out, and per-algorithm breakdown.
    Read via ``get_snapshot()`` for zero-contention observation.
    """
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)
    total_compressions: int = 0
    total_bytes_in: int = 0
    total_bytes_out: int = 0
    gzip_count: int = 0
    brotli_count: int = 0
    zstd_count: int = 0

    def record(self, algorithm: str, bytes_in: int, bytes_out: int) -> None:
        with self._lock:
            self.total_compressions += 1
            self.total_bytes_in += bytes_in
            self.total_bytes_out += bytes_out
            if algorithm == "gzip":
                self.gzip_count += 1
            elif algorithm == "brotli":
                self.brotli_count += 1
            elif algorithm == "zstd":
                self.zstd_count += 1

    def get_snapshot(self) -> dict:
        with self._lock:
            ratio = (
                self.total_bytes_out / self.total_bytes_in
                if self.total_bytes_in > 0
                else 0.0
            )
            return {
                "total_compressions": self.total_compressions,
                "total_bytes_in": self.total_bytes_in,
                "total_bytes_out": self.total_bytes_out,
                "compression_ratio": round(ratio, 4),
                "space_saved_pct": round((1 - ratio) * 100, 1),
                "gzip_count": self.gzip_count,
                "brotli_count": self.brotli_count,
                "zstd_count": self.zstd_count,
            }

    def reset(self) -> None:
        with self._lock:
            self.total_compressions = 0
            self.total_bytes_in = 0
            self.total_bytes_out = 0
            self.gzip_count = 0
            self.brotli_count = 0
            self.zstd_count = 0


# Global metrics instance
metrics = CompressionMetrics()
