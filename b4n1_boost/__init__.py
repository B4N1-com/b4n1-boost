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
import os
import platform
import sys
from pathlib import Path
from typing import Optional

VERSION = "0.1.0"


def _ensure_native_extension():
    """Attempt to import native extension or auto-download binary for host platform."""
    try:
        from b4n1_boost import _core
        return _core, True
    except ImportError:
        pass

    # Dynamic platform loader if extension is not present locally
    system = sys.platform
    machine = platform.machine()
    arch = "x86_64" if machine in ("x86_64", "amd64") else "aarch64" if machine in ("aarch64", "arm64") else machine

    # Look in package directory or user cache
    pkg_dir = Path(__file__).parent
    ext_suffix = ".so" if system != "win32" else ".pyd"
    local_binary = pkg_dir / f"_core_{system}_{arch}{ext_suffix}"

    if local_binary.exists():
        import importlib.util
        spec = importlib.util.spec_from_file_location("_core", str(local_binary))
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod, True

    return None, False


_core_module, _NATIVE = _ensure_native_extension()


def _parse(raw: str) -> dict:
    return json.loads(raw)


def install_django() -> dict:
    """Activate b4n1-boost acceleration for Django (JSON + ORM + WebSocket)."""
    if _NATIVE and _core_module:
        return _parse(_core_module.py_install_django())
    return {"framework": "Django", "status": "pure-python-fallback", "native": False}


def install_fastapi() -> dict:
    """Activate b4n1-boost acceleration for FastAPI (JSON + WebSocket)."""
    if _NATIVE and _core_module:
        return _parse(_core_module.py_install_fastapi())
    return {"framework": "FastAPI", "status": "pure-python-fallback", "native": False}


def install_flask() -> dict:
    """Activate b4n1-boost acceleration for Flask (JSON acceleration)."""
    if _NATIVE and _core_module:
        return _parse(_core_module.py_install_flask())
    return {"framework": "Flask", "status": "pure-python-fallback", "native": False}


def autoboost() -> dict:
    """Auto-detect the running framework and activate the appropriate boost."""
    if _NATIVE and _core_module:
        return _parse(_core_module.py_autoboost())
    return {"framework": "auto", "status": "pure-python-fallback", "native": False}


def run_benchmarks(iterations: Optional[int] = None) -> dict:
    """Run the native hardware benchmark suite and return a structured report."""
    if _NATIVE and _core_module:
        return _parse(_core_module.py_run_benchmarks(iterations))
    return {"status": "pure-python-fallback", "native": False}


def status() -> dict:
    """Return the current b4n1-boost engine status."""
    return {
        "native_extension": _NATIVE,
        "version": VERSION,
        "features": ["json_acceleration", "orm_interception", "websocket_acceleration"],
    }


__version__ = VERSION
__all__ = [
    "install_django",
    "install_fastapi",
    "install_flask",
    "autoboost",
    "run_benchmarks",
    "status",
]
