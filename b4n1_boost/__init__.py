"""
b4n1_boost — Transparent acceleration middleware for Django, FastAPI & Flask.

Usage:
    import b4n1_boost

    # Auto-detect & accelerate the running framework
    b4n1_boost.autoboost()

    # Or target a specific framework
    b4n1_boost.install_django()
    b4n1_boost.install_fastapi()
    b4n1_boost.install_flask()

    # Run the native hardware benchmark suite
    report = b4n1_boost.run_benchmarks()
"""

from __future__ import annotations

import json
from typing import Optional

try:
    from b4n1_boost._core import (
        py_install_django,
        py_install_fastapi,
        py_install_flask,
        py_autoboost,
        py_run_benchmarks,
    )
    _NATIVE = True
except ImportError:
    # Pure-Python fallback when the native extension is not compiled yet.
    # This allows importing the package in development without building first.
    _NATIVE = False


def _parse(raw: str) -> dict:
    return json.loads(raw)


def install_django() -> dict:
    """Activate b4n1-boost acceleration for Django (JSON + ORM + WebSocket)."""
    if _NATIVE:
        return _parse(py_install_django())
    return {"framework": "Django", "status": "pure-python-fallback", "native": False}


def install_fastapi() -> dict:
    """Activate b4n1-boost acceleration for FastAPI (JSON + WebSocket)."""
    if _NATIVE:
        return _parse(py_install_fastapi())
    return {"framework": "FastAPI", "status": "pure-python-fallback", "native": False}


def install_flask() -> dict:
    """Activate b4n1-boost acceleration for Flask (JSON acceleration)."""
    if _NATIVE:
        return _parse(py_install_flask())
    return {"framework": "Flask", "status": "pure-python-fallback", "native": False}


def autoboost() -> dict:
    """Auto-detect the running framework and activate the appropriate boost."""
    if _NATIVE:
        return _parse(py_autoboost())
    return {"framework": "auto", "status": "pure-python-fallback", "native": False}


def run_benchmarks(iterations: Optional[int] = None) -> dict:
    """Run the native hardware benchmark suite and return a structured report."""
    if _NATIVE:
        return _parse(py_run_benchmarks(iterations))
    return {"status": "pure-python-fallback", "native": False}


def status() -> dict:
    """Return the current b4n1-boost engine status."""
    return {
        "native_extension": _NATIVE,
        "version": "0.1.0",
        "features": ["json_acceleration", "orm_interception", "websocket_acceleration"],
    }


__version__ = "0.1.0"
__all__ = [
    "install_django",
    "install_fastapi",
    "install_flask",
    "autoboost",
    "run_benchmarks",
    "status",
]
