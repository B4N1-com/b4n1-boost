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
    from b4n1_boost._core import py_json_dumps, py_json_loads
    _NATIVE = True
except ImportError:  # pragma: no cover - exercised only in source checkouts
    py_json_dumps = None  # type: ignore[assignment]
    py_json_loads = None  # type: ignore[assignment]
    _NATIVE = False


class NativeJson:
    """JSON fast-path dispatcher (native Rust engine when present)."""

    @staticmethod
    def dumps(obj: Any) -> str:
        """Serialize ``obj`` (any JSON-serializable Python value) to JSON."""
        text = _json.dumps(obj, separators=(",", ":"), ensure_ascii=False)
        if _NATIVE and py_json_dumps is not None:
            try:
                return py_json_dumps(text)
            except Exception:
                return text
        return text

    @staticmethod
    def loads(text: str) -> Any:
        if _NATIVE and py_json_loads is not None:
            try:
                return _json.loads(py_json_loads(text))
            except Exception:
                pass
        return _json.loads(text)


def _native_json_response(body: bytes) -> Optional[bytes]:
    """Re-serialize a UTF-8 JSON ``body`` through the native engine.

    The native functions take a JSON *string* and return the canonical compact
    form (serde_json ``to_string``). Returns ``None`` when the native engine is
    unavailable or the body is not valid JSON, so callers fall back to the
    original body untouched (no silent corruption).
    """
    if not _NATIVE or py_json_dumps is None:
        return None
    try:
        return py_json_dumps(body.decode("utf-8")).encode("utf-8")
    except Exception:
        return None


class BoostWSGIMiddleware:
    """Generic WSGI middleware: transparent JSON payload compression.

    Wraps any WSGI application and re-serializes ``application/json`` response
    bodies through the native engine (validates + canonicalizes), keeping
    behaviour identical for callers while exercising the Rust code path.
    """

    def __init__(self, app: Callable) -> None:
        self.app = app

    def __call__(self, environ: dict, start_response: Callable) -> list:
        # Capture the app's start_response call, buffer the body, then call
        # start_response exactly once with the final (possibly rewritten)
        # headers — required for real WSGI servers.
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

        content_type = next(
            (v for k, v in captured.get("headers", []) if k.lower() == "content-type"),
            "",
        )
        exc_info = captured.get("exc_info")
        if "application/json" in content_type and body:
            native = _native_json_response(body)
            if native is not None:
                headers = [
                    (k, v) if k.lower() != "content-length" else ("Content-Length", str(len(native)))
                    for k, v in captured.get("headers", [])
                ]
                start_response(captured["status"], headers, exc_info)
                return [native]
        start_response(captured["status"], captured["headers"], exc_info)
        return [body]


class FastAPIBoostMiddleware:
    """ASGI middleware for FastAPI/Starlette.

    Use via ``app.add_middleware(b4n1_boost.middleware.FastAPIBoostMiddleware)``
    or the ``b4n1_boost.install_fastapi(app)`` helper. Forwards to the next
    ASGI app and re-serializes JSON response bodies natively.
    """

    def __init__(self, app: Any) -> None:
        self.app = app

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        async def _send(message: dict) -> None:
            if message["type"] == "http.response.start":
                nonlocal content_type
                for k, v in message.get("headers", []):
                    if k.lower() == b"content-type" and b"application/json" in v:
                        content_type = True
            if message["type"] == "http.response.body" and content_type and message.get("body"):
                native = _native_json_response(message["body"])
                if native is not None:
                    message["body"] = native
                    message["more_body"] = False
            await send(message)

        content_type = False
        await self.app(scope, receive, _send)


class DjangoBoostMiddleware:
    """Django middleware (Django 2+ style callable).

    Install by adding ``"b4n1_boost.middleware.DjangoBoostMiddleware"`` to
    ``settings.MIDDLEWARE`` (``install_django()`` does this automatically).
    Re-serializes JSON responses through the native engine.
    """

    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: Any) -> Any:
        response = self.get_response(request)
        ctype = response.get("Content-Type", "")
        if "application/json" in ctype and response.content:
            native = _native_json_response(response.content)
            if native is not None:
                response.content = native
                has_cl = response.has_header("Content-Length") if hasattr(response, "has_header") else "Content-Length" in response
                if has_cl:
                    response["Content-Length"] = str(len(response.content))
        return response


def install_django_middleware() -> bool:
    """Append the Django middleware to ``settings.MIDDLEWARE`` if possible."""
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
    """Attach the ASGI middleware to a FastAPI/Starlette app."""
    try:
        app.add_middleware(FastAPIBoostMiddleware)
        return True
    except Exception:
        return False


def install_flask_middleware(app: Any) -> bool:
    """Wrap a Flask app's WSGI app."""
    try:
        app.wsgi_app = BoostWSGIMiddleware(app.wsgi_app)
        return True
    except Exception:
        return False