"""
b4n1_boost — Transparent acceleration middleware for Django, FastAPI & Flask.

Usage::

    import b4n1_boost

    # Auto-detect & accelerate the running framework
    b4n1_boost.autoboost()

    # Or target a specific framework (pass app instance)
    b4n1_boost.install_fastapi(app)
    b4n1_boost.install_flask(app)

    # Django: just call autoboost() — no app instance needed
    b4n1_boost.autoboost()

    # JSON fast-path
    from b4n1_boost import NativeJson
    data = NativeJson.dumps_direct(my_dict)

    # Canonicalize JSON for hashing / dedup
    canonical = b4n1_boost.canonicalize_json(my_dict)  # accepts str or dict
"""

from __future__ import annotations

import json as _json
from typing import Any, Optional

from b4n1_boost.middleware import (
    B4N1BoostCompressionMiddleware,
    BoostWSGIMiddleware,
    DjangoBoostMiddleware,
    FastAPIBoostCompressionMiddleware,
    FastAPIBoostMiddleware,
    NativeJson,
    canonicalize_json,
    validate_json,
    install_django_middleware,
    install_fastapi_middleware,
    install_flask_middleware,
    ETagMiddleware,
    ASGIETagMiddleware,
    RateLimitMiddleware,
    ASGIRateLimitMiddleware,
    SecurityHeadersMiddleware,
    ASGISecurityHeadersMiddleware,
    DecompressionMiddleware,
    HealthCheckMiddleware,
    ASGIHealthCheckMiddleware,
    CORSMiddleware,
    ASGICORSMiddleware,
    RequestLoggingMiddleware,
    ASGIRequestLoggingMiddleware,
    CompressionMetrics,
    detect_proxy,
    metrics,
    batch_dumps,
    batch_dumps_direct,
    batch_loads,
    batch_validate,
)

from b4n1_boost.advanced import (
    validate_jwt,
    minify_html,
    minify_css,
    minify_js,
    ResponseCache,
    CacheMiddleware,
    ASGICacheMiddleware,
    BloomRateLimiter,
    CircuitBreakerMiddleware,
)

try:
    from b4n1_boost._core import (
        py_install_django,
        py_install_fastapi,
        py_install_flask,
        py_autoboost,
        py_run_benchmarks,
        py_json_dumps,
        py_json_loads,
        py_json_dumps_direct,
        py_compress_gzip,
        py_compress_gzip_fast,
        py_compress_brotli,
        py_compress_zstd,
        py_decompress_zstd,
        py_canonicalize_direct,
        py_batch_json_dumps,
        py_batch_json_loads,
        py_worker_compress,
        py_worker_decompress,
        py_worker_jwt_validate,
        py_worker_minify,
        py_worker_shutdown,
        py_html_to_markdown,
    )

    _NATIVE = True
except ImportError:
    _NATIVE = False
    py_install_django = None  # type: ignore[assignment]
    py_install_fastapi = None  # type: ignore[assignment]
    py_install_flask = None  # type: ignore[assignment]
    py_autoboost = None  # type: ignore[assignment]
    py_run_benchmarks = None  # type: ignore[assignment]
    py_json_dumps = None  # type: ignore[assignment]
    py_json_loads = None  # type: ignore[assignment]
    py_json_dumps_direct = None  # type: ignore[assignment]
    py_compress_gzip = None  # type: ignore[assignment]
    py_compress_brotli = None  # type: ignore[assignment]
    py_compress_zstd = None  # type: ignore[assignment]
    py_decompress_zstd = None  # type: ignore[assignment]
    py_canonicalize_direct = None  # type: ignore[assignment]
    py_batch_json_dumps = None  # type: ignore[assignment]
    py_batch_json_loads = None  # type: ignore[assignment]
    py_worker_compress = None  # type: ignore[assignment]
    py_worker_decompress = None  # type: ignore[assignment]
    py_worker_jwt_validate = None  # type: ignore[assignment]
    py_worker_minify = None  # type: ignore[assignment]
    py_worker_shutdown = None  # type: ignore[assignment]
    py_html_to_markdown = None  # type: ignore[assignment]


def _parse(raw: str) -> dict:
    return _json.loads(raw)


def _report(
    framework: str,
    installed: bool,
    reason: str = "",
    native: Optional[bool] = None,
    native_reporter: object = None,
) -> dict:
    """Merge the framework-specific native report with injection state."""
    report: dict[str, Any] = {
        "framework": framework,
        "native": bool(native if native is not None else _NATIVE),
    }
    if _NATIVE and callable(native_reporter):
        try:
            report.update(_parse(native_reporter()))
        except Exception:
            pass
    report["framework"] = framework
    report["middleware_installed"] = installed
    if not installed:
        report["middleware_reason"] = reason
    return report


def install_django(app: object = None) -> dict:
    """Activate b4n1-boost for Django.

    Appends ``DjangoBoostMiddleware`` to ``settings.MIDDLEWARE`` when Django is
    importable and configured; the actual JSON responses flow through the
    native engine.
    """
    installed = install_django_middleware()
    return _report(
        "Django",
        installed,
        "django not importable / not configured",
        native_reporter=py_install_django,
    )


def install_fastapi(app: object = None) -> dict:
    """Activate b4n1-boost for FastAPI/Starlette.

    Pass your ``FastAPI()`` instance to attach the ASGI middleware via
    ``app.add_middleware``. Without ``app``, returns the engine report.
    """
    installed = install_fastapi_middleware(app) if app is not None else False
    return _report(
        "FastAPI",
        installed,
        "no app passed to install_fastapi(app)",
        native_reporter=py_install_fastapi,
    )


def install_flask(app: object = None) -> dict:
    """Activate b4n1-boost for Flask.

    Pass your ``Flask()`` app to wrap ``app.wsgi_app`` with the boost
    middleware. Without ``app``, returns the engine report.
    """
    installed = install_flask_middleware(app) if app is not None else False
    return _report(
        "Flask",
        installed,
        "no app passed to install_flask(app)",
        native_reporter=py_install_flask,
    )


def autoboost(app: object = None) -> dict:
    """Auto-detect the running framework and activate the appropriate boost.

    Pass ``app`` (a FastAPI or Flask instance) to attach the middleware to it
    directly. Without ``app``: Django is configured automatically, while
    FastAPI/Flask reports explain which ``install_*(app)`` call to make.

    When ``app`` is passed:
    - FastAPI: attaches ASGI compression middleware
    - Flask: wraps WSGI app with compression middleware
    """
    if app is not None:
        if hasattr(app, "add_middleware") or hasattr(app, "user_middleware"):
            return install_fastapi(app)
        if hasattr(app, "wsgi_app"):
            return install_flask(app)
    framework = _detect_framework()
    if framework == "Django":
        return install_django()
    if framework == "FastAPI":
        return _report(
            "FastAPI",
            False,
            "autoboost requires an explicit FastAPI app; call install_fastapi(app)",
        )
    if framework in ("Flask", "WSGI"):
        return _report(
            "Flask",
            False,
            "autoboost requires an explicit Flask app; call install_flask(app)",
        )
    return _report("none", False, "no supported framework detected")


def boost_all(
    app: object = None,
    compression: bool = True,
    etag: bool = True,
    security: bool = True,
    cors: bool = False,
    cors_origins: Optional[list[str]] = None,
    rate_limit: bool = False,
    rate: float = 100.0,
    burst: int = 200,
    health_check: bool = True,
    decompression: bool = True,
    min_size: int = 1024,
    fast_mode: bool = False,
) -> dict:
    """One-call setup: auto-detect framework and apply all desired middleware.

    This is the recommended entry point for most users. It composes
    compression, ETag, security headers, CORS, rate limiting, health check,
    and request decompression in the correct order for the detected framework.

    Args:
        app: FastAPI/Flask instance (optional for Django).
        compression: Enable response compression (gzip/brotli/zstd).
        etag: Enable ETag/304 caching.
        security: Enable security headers (X-Frame-Options, etc.).
        cors: Enable CORS headers.
        cors_origins: Allowed origins (default ["*"]).
        rate_limit: Enable rate limiting.
        rate: Max requests per second (when rate_limit=True).
        burst: Max burst size (when rate_limit=True).
        health_check: Enable /_boost/health endpoint.
        decompression: Enable request decompression.
        min_size: Minimum body size to compress.
        fast_mode: Use fastest compressor (zstd/gzip-1) instead of best ratio.

    Returns:
        dict with framework info, applied middlewares, and native status.
    """
    from b4n1_boost.middleware import (
        B4N1BoostCompressionMiddleware,
        FastAPIBoostCompressionMiddleware,
        ETagMiddleware,
        SecurityHeadersMiddleware,
        CORSMiddleware,
        RateLimitMiddleware,
        HealthCheckMiddleware,
        DecompressionMiddleware,
        ASGIRateLimitMiddleware,
        ASGISecurityHeadersMiddleware,
        ASGIHealthCheckMiddleware,
        ASGICORSMiddleware,
    )

    applied: list[str] = []
    framework = _detect_framework()

    # FastAPI / ASGI
    if app is not None and (hasattr(app, "add_middleware") or hasattr(app, "user_middleware")):
        framework = "FastAPI"
        if compression:
            app.add_middleware(FastAPIBoostCompressionMiddleware, min_size=min_size, fast_mode=fast_mode)
            applied.append("compression")
        if etag:
            app.add_middleware(ASGIETagMiddleware)
            applied.append("etag")
        if security:
            app.add_middleware(ASGISecurityHeadersMiddleware)
            applied.append("security")
        if cors:
            app.add_middleware(ASGICORSMiddleware, allow_origins=cors_origins)
            applied.append("cors")
        if rate_limit:
            app.add_middleware(ASGIRateLimitMiddleware, rate=rate, burst=burst)
            applied.append("rate_limit")
        if health_check:
            app.add_middleware(ASGIHealthCheckMiddleware)
            applied.append("health_check")
        if decompression:
            applied.append("decompression")  # ASGI decompression handled by framework
        return {
            "framework": framework,
            "native": _NATIVE,
            "applied": applied,
            "middleware_count": len(applied),
        }

    # Flask / WSGI
    if app is not None and hasattr(app, "wsgi_app"):
        framework = "Flask"
        wsgi = app.wsgi_app
        # Wrap order: innermost first (decompression → health → cors → rate → security → etag → compression)
        if decompression:
            wsgi = DecompressionMiddleware(wsgi)
            applied.append("decompression")
        if health_check:
            wsgi = HealthCheckMiddleware(wsgi)
            applied.append("health_check")
        if rate_limit:
            wsgi = RateLimitMiddleware(wsgi, rate=rate, burst=burst)
            applied.append("rate_limit")
        if security:
            wsgi = SecurityHeadersMiddleware(wsgi)
            applied.append("security")
        if cors:
            wsgi = CORSMiddleware(wsgi, allow_origins=cors_origins)
            applied.append("cors")
        if etag:
            wsgi = ETagMiddleware(wsgi)
            applied.append("etag")
        if compression:
            wsgi = B4N1BoostCompressionMiddleware(wsgi, min_size=min_size, fast_mode=fast_mode)
            applied.append("compression")
        app.wsgi_app = wsgi
        app._b4n1_boost_installed = True
        return {
            "framework": framework,
            "native": _NATIVE,
            "applied": applied,
            "middleware_count": len(applied),
        }

    # Django
    if framework == "Django":
        try:
            from django.conf import settings
            current = list(getattr(settings, "MIDDLEWARE", []) or [])
            if compression or True:  # Django always gets compression
                path = "b4n1_boost.middleware.DjangoBoostMiddleware"
                if path not in current:
                    current.append(path)
                    settings.MIDDLEWARE = current
                applied.append("compression")
            return {
                "framework": "Django",
                "native": _NATIVE,
                "applied": applied,
                "middleware_count": len(applied),
            }
        except ImportError:
            pass

    return {
        "framework": "none",
        "native": _NATIVE,
        "applied": [],
        "error": "no supported framework detected or no app passed",
    }


def _detect_framework() -> str:
    """Best-effort framework detection (no imports executed)."""
    try:
        import django  # noqa: F401

        return "Django"
    except ImportError:
        pass
    try:
        import fastapi  # noqa: F401

        return "FastAPI"
    except ImportError:
        pass
    try:
        import flask  # noqa: F401

        return "Flask"
    except ImportError:
        return "none"


def run_benchmarks(iterations: Optional[int] = None) -> dict:
    """Run the native hardware benchmark suite and return a structured report."""
    if _NATIVE and py_run_benchmarks is not None:
        raw = py_run_benchmarks(iterations)
        return _parse(raw) if isinstance(raw, str) else raw
    return {"status": "pure-python-fallback", "native": False}


__version__ = "0.3.2"


# ── Batch JSON API ─────────────────────────────────────────────────────

def batch_dumps(objs: list) -> list[str]:
    """Serialize N Python objects to JSON strings.

    Uses orjson when available for batch speed.
    Falls back to stdlib json.dumps.
    """
    try:
        import orjson as _oj
        return [_oj.dumps(obj).decode("utf-8") for obj in objs]
    except ImportError:
        return [_json.dumps(obj, separators=(',', ':'), ensure_ascii=False) for obj in objs]


def batch_loads(strs: list[str]) -> list[Any]:
    """Parse N JSON strings to Python objects.

    Uses orjson when available for batch speed.
    Falls back to stdlib json.loads.
    """
    try:
        import orjson as _oj
        return [_oj.loads(s.encode("utf-8") if isinstance(s, str) else s) for s in strs]
    except ImportError:
        return [_json.loads(s) for s in strs]


# ── Worker Thread API (zero-GIL heavy operations) ──────────────────────

def worker_compress(data: bytes, algo: str = "zstd") -> bytes:
    """Compress data via background Rust worker thread (no GIL contention).

    Args:
        data: Raw bytes to compress.
        algo: Compression algorithm - 'gzip', 'gzip_fast', 'brotli', or 'zstd'.

    Returns:
        Compressed bytes.

    Raises:
        IOError: If compression fails.
    """
    if _NATIVE and py_worker_compress is not None:
        return bytes(py_worker_compress(data, algo))
    # Fallback to direct PyO3 call
    if algo == "gzip":
        return bytes(py_compress_gzip(data))
    elif algo == "gzip_fast":
        return bytes(py_compress_gzip_fast(data))
    elif algo == "brotli":
        return bytes(py_compress_brotli(data))
    elif algo == "zstd":
        return bytes(py_compress_zstd(data))
    raise ValueError(f"unknown algo: {algo}")


def worker_decompress(data: bytes) -> bytes:
    """Decompress zstd data via background Rust worker thread."""
    if _NATIVE and py_worker_decompress is not None:
        return bytes(py_worker_decompress(data))
    return bytes(py_decompress_zstd(data))


def worker_jwt_validate(token: str, secret: str) -> dict:
    """Validate JWT token via background Rust worker thread.

    Returns:
        dict with claims (sub, exp, iat, iss, custom claims).

    Raises:
        ValueError: If token is invalid.
    """
    if _NATIVE and py_worker_jwt_validate is not None:
        import json as _json
        return _json.loads(py_worker_jwt_validate(token, secret))
    return validate_jwt(token, secret)


def worker_minify(data: str, kind: str = "html") -> str:
    """Minify HTML/CSS/JS or convert to Markdown via background Rust worker thread.

    Args:
        data: Source string to minify/convert.
        kind: 'html', 'css', 'js', or 'markdown'.
    """
    if _NATIVE and py_worker_minify is not None:
        return py_worker_minify(data, kind)
    if kind == "html":
        return minify_html(data)
    elif kind == "css":
        return minify_css(data)
    elif kind == "js":
        return minify_js(data)
    elif kind == "markdown":
        return html_to_markdown(data)
    raise ValueError(f"unknown kind: {kind}")


def worker_shutdown():
    """Shutdown the background worker thread gracefully."""
    if _NATIVE and py_worker_shutdown is not None:
        py_worker_shutdown()


# ── Agentic Output (HTML → Markdown) ──────────────────────────────────

def html_to_markdown(html: str) -> str:
    """Convert HTML to clean Markdown for agentic output.

    When native extension is available, uses lol_html streaming converter.
    Falls back to simple tag stripping.
    """
    if _NATIVE and py_html_to_markdown is not None:
        return py_html_to_markdown(html)
    # Fallback: strip tags
    import re
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# ── Telemetry (b4n1-telemetry integration) ─────────────────────────────

def telemetry_init(app: str = "b4n1-boost"):
    """Initialize telemetry for error/info logging."""
    if _NATIVE:
        from ._core import py_telemetry_init
        py_telemetry_init(app)


def telemetry_capture_error(error: str, context: dict = None):
    """Capture an error event with context data."""
    if _NATIVE:
        from ._core import py_telemetry_capture_error
        py_telemetry_capture_error(error, context or {})


def telemetry_log_info(message: str, data: dict = None):
    """Log an info event with data."""
    if _NATIVE:
        from ._core import py_telemetry_log_info
        py_telemetry_log_info(message, data or {})


def telemetry_log_phase(phase: str, status: str, duration_ms: int):
    """Log a pipeline phase (phase, status, duration_ms)."""
    if _NATIVE:
        from ._core import py_telemetry_log_phase
        py_telemetry_log_phase(phase, status, duration_ms)


def telemetry_flush():
    """Flush telemetry events to endpoint or file."""
    if _NATIVE:
        from ._core import py_telemetry_flush
        py_telemetry_flush()


# ── Static file compression ────────────────────────────────────────────

def compress_static_file(path: str) -> dict:
    """Compress a file with zstd, brotli, and gzip.

    Writes .zst, .br, .gz files alongside the original.
    Returns dict with compression ratios for each algorithm.
    """
    if _NATIVE:
        from ._core import py_compress_static_file
        import json as _json
        return _json.loads(py_compress_static_file(path))
    raise RuntimeError("native extension required for static file compression")


def compress_static_dir(dir_path: str) -> dict:
    """Compress a directory recursively with all three algorithms.

    Processes .html, .css, .js, .json, .svg, .xml, .txt, .md files.
    Returns dict with summary statistics.
    """
    if _NATIVE:
        from ._core import py_compress_static_dir
        import json as _json
        return _json.loads(py_compress_static_dir(dir_path))
    raise RuntimeError("native extension required for static file compression")


def status() -> dict:
    """Return the current b4n1-boost engine status."""
    return {
        "native_extension": _NATIVE,
        "version": __version__,
        "features": {
            "json_acceleration": True,
            "json_canonicalize": True,
            "compression": ["gzip", "brotli", "zstd"],
            "middleware": ["django", "fastapi", "flask"],
        },
        "compression_engines": {
            "gzip": bool(_NATIVE),
            "brotli": bool(_NATIVE),
            "zstd": bool(_NATIVE),
        },
    }


__all__ = [
    # Public API
    "install_django",
    "install_fastapi",
    "install_flask",
    "autoboost",
    "boost_all",
    "run_benchmarks",
    "status",
    "__version__",
    # Middleware classes
    "NativeJson",
    "BoostWSGIMiddleware",
    "B4N1BoostCompressionMiddleware",
    "DjangoBoostMiddleware",
    "FastAPIBoostMiddleware",
    "FastAPIBoostCompressionMiddleware",
    # New middleware
    "ASGIRateLimitMiddleware",
    "SecurityHeadersMiddleware",
    "ASGISecurityHeadersMiddleware",
    "DecompressionMiddleware",
    "HealthCheckMiddleware",
    "ASGIHealthCheckMiddleware",
    "CORSMiddleware",
    "ASGICORSMiddleware",
    "RequestLoggingMiddleware",
    "ASGIRequestLoggingMiddleware",
    # Utility
    "canonicalize_json",
    "validate_json",
    "ETagMiddleware",
    "ASGIETagMiddleware",
    "RateLimitMiddleware",
    "CompressionMetrics",
    "detect_proxy",
    "metrics",
    # Batch operations
    "batch_dumps",
    "batch_dumps_direct",
    "batch_loads",
    "batch_validate",
    # Worker thread API
    "worker_compress",
    "worker_decompress",
    "worker_jwt_validate",
    "worker_minify",
    "worker_shutdown",
    # Advanced features
    "validate_jwt",
    "minify_html",
    "minify_css",
    "minify_js",
    "html_to_markdown",
    # Telemetry
    "telemetry_init",
    "telemetry_capture_error",
    "telemetry_log_info",
    "telemetry_log_phase",
    "telemetry_flush",
    # Static file compression
    "compress_static_file",
    "compress_static_dir",
    # Cache/Rate-limit
    "ResponseCache",
    "CacheMiddleware",
    "ASGICacheMiddleware",
    "BloomRateLimiter",
    "CircuitBreakerMiddleware",
]
