"""
b4n1_boost — Transparent acceleration middleware for Django, FastAPI & Flask.

Usage:
    import b4n1_boost

    # Auto-detect & accelerate the running framework
    b4n1_boost.autoboost()

    # Or target a specific framework
    b4n1_boost.install_django()
    b4n1_boost.install_fastapi(app)
    b4n1_boost.install_flask(app)
"""

from __future__ import annotations

import json as _json
from typing import Optional

from b4n1_boost.middleware import (
    BoostWSGIMiddleware,
    DjangoBoostMiddleware,
    FastAPIBoostMiddleware,
    NativeJson,
    install_django_middleware,
    install_fastapi_middleware,
    install_flask_middleware,
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
    )
    _NATIVE = True
except ImportError:
    # Pure-Python fallback when the native extension is not compiled yet.
    _NATIVE = False


def _parse(raw: str) -> dict:
    return _json.loads(raw)


def _report(framework: str, installed: bool, reason: str = "", native: Optional[bool] = None) -> dict:
    """Merge the native engine report with the real injection result."""
    report = {"framework": framework, "native": bool(native if native is not None else _NATIVE)}
    if _NATIVE:
        try:
            report.update(_parse(py_install_django()))
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
    return _report("Django", installed, "django not importable / not configured")


def install_fastapi(app: object = None) -> dict:
    """Activate b4n1-boost for FastAPI/Starlette.

    Pass your ``FastAPI()`` instance to attach the ASGI middleware via
    ``app.add_middleware``. Without ``app``, returns the engine report.
    """
    installed = install_fastapi_middleware(app) if app is not None else False
    return _report("FastAPI", installed, "no app passed to install_fastapi(app)")


def install_flask(app: object = None) -> dict:
    """Activate b4n1-boost for Flask.

    Pass your ``Flask()`` app to wrap ``app.wsgi_app`` with the boost
    middleware. Without ``app``, returns the engine report.
    """
    installed = install_flask_middleware(app) if app is not None else False
    return _report("Flask", installed, "no app passed to install_flask(app)")


def autoboost() -> dict:
    """Auto-detect the running framework and activate the appropriate boost."""
    framework = _detect_framework()
    if framework == "Django":
        return install_django()
    if framework == "FastAPI":
        return install_fastapi()
    if framework in ("Flask", "WSGI"):
        return install_flask()
    return _report("none", False, "no supported framework detected")


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
    if _NATIVE:
        return _parse(py_run_benchmarks(iterations))
    return {"status": "pure-python-fallback", "native": False}


def status() -> dict:
    """Return the current b4n1-boost engine status."""
    return {
        "native_extension": _NATIVE,
        "version": "0.1.5",
        "features": ["json_acceleration", "orm_interception", "websocket_acceleration"],
    }


__version__ = "0.1.5"
__all__ = [
    "install_django",
    "install_fastapi",
    "install_flask",
    "autoboost",
    "run_benchmarks",
    "status",
    "NativeJson",
    "BoostWSGIMiddleware",
    "DjangoBoostMiddleware",
    "FastAPIBoostMiddleware",
]