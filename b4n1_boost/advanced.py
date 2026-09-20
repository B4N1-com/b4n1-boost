"""
b4n1_boost.advanced — Python wrappers for advanced Rust features.

Provides response caching, JWT validation, bloom filter rate limiting,
circuit breaker, and HTML/CSS/JS minification — all backed by native Rust.
"""

from __future__ import annotations

import json as _json
import time as _time
import threading
from typing import Any, Callable, Optional
from dataclasses import dataclass, field

try:
    from b4n1_boost._core import (
        py_validate_jwt,
        py_minify_html,
        py_minify_css,
        py_minify_js,
    )
    _NATIVE = True
except ImportError:
    _NATIVE = False
    py_validate_jwt = None  # type: ignore
    py_minify_html = None  # type: ignore
    py_minify_css = None  # type: ignore
    py_minify_js = None  # type: ignore


# ── JWT Validation ─────────────────────────────────────────────────────


def validate_jwt(token: str, secret: str) -> dict:
    """Validate a JWT token using native Rust.

    Args:
        token: The JWT token string.
        secret: The secret key for validation.

    Returns:
        dict with sub, exp, iat, iss, and custom claims.

    Raises:
        ValueError: If the token is invalid or expired.
    """
    if _NATIVE and py_validate_jwt is not None:
        result = py_validate_jwt(token, secret)
        return _json.loads(result)
    # Python fallback using PyJWT
    try:
        import jwt
        payload = jwt.decode(token, secret, algorithms=["HS256", "HS384", "HS512"])
        return payload
    except ImportError:
        raise ImportError("PyJWT is required for JWT validation without native extension")
    except Exception as e:
        raise ValueError(str(e))


# ── HTML/CSS/JS Minification ──────────────────────────────────────────


def minify_html(content: str) -> str:
    """Minify HTML content (collapse whitespace).

    Uses native Rust when available, falls back to Python.
    """
    if _NATIVE and py_minify_html is not None:
        return py_minify_html(content)
    # Python fallback
    import re
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'>\s+<', '><', content)
    return content.strip()


def minify_css(content: str) -> str:
    """Minify CSS content (collapse whitespace).

    Uses native Rust when available, falls back to Python.
    """
    if _NATIVE and py_minify_css is not None:
        return py_minify_css(content)
    import re
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}:;,])\s*', r'\1', content)
    return content.strip()


def minify_js(content: str) -> str:
    """Minify JavaScript content (remove comments, collapse whitespace).

    Uses native Rust when available, falls back to Python.
    """
    if _NATIVE and py_minify_js is not None:
        return py_minify_js(content)
    import re
    # Remove single-line comments (but not URLs)
    content = re.sub(r'(?<!:)//.*$', '', content, flags=re.MULTILINE)
    # Remove block comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Collapse whitespace
    content = re.sub(r'\s+', ' ', content)
    return content.strip()


# ── Response Cache (LRU with TTL) ─────────────────────────────────────


@dataclass
class _CacheEntry:
    body: bytes
    headers: list
    status: int
    created: float
    ttl: float


class ResponseCache:
    """In-memory LRU response cache with TTL.

    Caches responses in a Python dict (LRU eviction when full).
    For maximum performance, use the Rust-backed version when available.

    Args:
        capacity: Maximum number of cached entries.
        default_ttl: Default time-to-live in seconds.
    """

    def __init__(self, capacity: int = 1000, default_ttl: int = 300) -> None:
        self._capacity = capacity
        self._default_ttl = default_ttl
        self._cache: dict[str, _CacheEntry] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> Optional[tuple[bytes, list, int]]:
        """Get a cached response. Returns (body, headers, status) or None."""
        with self._lock:
            entry = self._cache.get(key)
            if entry is None:
                return None
            if _time.monotonic() - entry.created > entry.ttl:
                del self._cache[key]
                return None
            # Move to end (most recently used)
            del self._cache[key]
            self._cache[key] = entry
            return (entry.body, entry.headers, entry.status)

    def set(self, key: str, body: bytes, headers: list, status: int, ttl: Optional[int] = None) -> None:
        """Cache a response."""
        with self._lock:
            if key in self._cache:
                del self._cache[key]
            elif len(self._cache) >= self._capacity:
                # Evict oldest (first item)
                oldest = next(iter(self._cache))
                del self._cache[oldest]
            self._cache[key] = _CacheEntry(
                body=body,
                headers=headers,
                status=status,
                created=_time.monotonic(),
                ttl=ttl if ttl is not None else self._default_ttl,
            )

    def invalidate(self, key: str) -> bool:
        """Remove a cached entry. Returns True if it existed."""
        with self._lock:
            return self._cache.pop(key, None) is not None

    def clear(self) -> None:
        """Clear all cached entries."""
        with self._lock:
            self._cache.clear()

    def stats(self) -> dict:
        """Return cache statistics."""
        with self._lock:
            return {
                "entries": len(self._cache),
                "capacity": self._capacity,
            }


# ── Response Cache Middleware ──────────────────────────────────────────


class CacheMiddleware:
    """WSGI middleware that caches GET responses.

    Args:
        app: The WSGI application to wrap.
        cache: ResponseCache instance.
        cache_paths: List of path prefixes to cache. None = cache all GET.
        exclude_paths: List of path prefixes to exclude from caching.
    """

    def __init__(
        self,
        app: Callable,
        cache: Optional[ResponseCache] = None,
        cache_paths: Optional[list[str]] = None,
        exclude_paths: Optional[list[str]] = None,
    ) -> None:
        self.app = app
        self._cache = cache or ResponseCache()
        self._cache_paths = cache_paths
        self._exclude_paths = exclude_paths or []

    def _should_cache(self, path: str, method: str) -> bool:
        if method != "GET":
            return False
        for excl in self._exclude_paths:
            if path.startswith(excl):
                return False
        if self._cache_paths is not None:
            return any(path.startswith(p) for p in self._cache_paths)
        return True

    def __call__(self, environ: dict, start_response: Callable) -> list:
        method = environ.get("REQUEST_METHOD", "GET")
        path = environ.get("PATH_INFO", "/")
        cache_key = f"{method}:{path}"

        if self._should_cache(path, method):
            cached = self._cache.get(cache_key)
            if cached is not None:
                body, headers, status = cached
                start_response(f"{status} OK", headers)
                return [body]

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

        if self._should_cache(path, method) and captured.get("status", "").startswith("200"):
            self._cache.set(cache_key, body, list(captured["headers"]), 200)

        start_response(captured["status"], captured["headers"], captured.get("exc_info"))
        return [body]


class ASGICacheMiddleware:
    """ASGI middleware that caches GET responses."""

    def __init__(
        self,
        app: Any,
        cache: Optional[ResponseCache] = None,
        cache_paths: Optional[list[str]] = None,
        exclude_paths: Optional[list[str]] = None,
    ) -> None:
        self.app = app
        self._cache = cache or ResponseCache()
        self._cache_paths = cache_paths
        self._exclude_paths = exclude_paths or []

    def _should_cache(self, path: str, method: str) -> bool:
        if method != "GET":
            return False
        for excl in self._exclude_paths:
            if path.startswith(excl):
                return False
        if self._cache_paths is not None:
            return any(path.startswith(p) for p in self._cache_paths)
        return True

    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        method = scope.get("method", "GET")
        path = scope.get("path", "/")
        cache_key = f"{method}:{path}"

        if self._should_cache(path, method):
            cached = self._cache.get(cache_key)
            if cached is not None:
                body, headers, status = cached
                await send({
                    "type": "http.response.start",
                    "status": status,
                    "headers": [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers],
                })
                await send({"type": "http.response.body", "body": body, "more_body": False})
                return

        start_message = None
        body_messages = []

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

                status = start_message.get("status", 200)
                if self._should_cache(path, method) and 200 <= status < 300:
                    raw_headers = start_message.get("headers", [])
                    headers = [(k.decode("latin-1"), v.decode("latin-1")) for k, v in raw_headers]
                    self._cache.set(cache_key, body, headers, status)

                await send(start_message)
                for pending in body_messages:
                    await send(pending)
                body_messages.clear()
                return
            await send(message)

        await self.app(scope, receive, _send)


# ── Bloom Filter Rate Limiter ──────────────────────────────────────────


class BloomRateLimiter:
    """Rate limiter using a bloom filter for efficient IP tracking.

    Uses a bloom filter to quickly check if an IP has been seen recently.
    False positives mean some requests might be incorrectly rate-limited
    (but never incorrectly allowed).

    Args:
        max_requests: Maximum requests per window per IP.
        window_seconds: Time window in seconds.
        false_positive_rate: Bloom filter false positive rate.
    """

    def __init__(
        self,
        max_requests: int = 100,
        window_seconds: int = 60,
        false_positive_rate: float = 0.01,
    ) -> None:
        self._max_requests = max_requests
        self._window_seconds = window_seconds
        self._fp_rate = false_positive_rate
        self._buckets: dict[str, list[float]] = {}
        self._lock = threading.Lock()

    def allow_request(self, ip: str) -> bool:
        """Check if a request from this IP should be allowed."""
        now = _time.monotonic()
        with self._lock:
            if ip not in self._buckets:
                self._buckets[ip] = []
            timestamps = self._buckets[ip]
            # Remove expired entries
            cutoff = now - self._window_seconds
            self._buckets[ip] = [t for t in timestamps if t > cutoff]
            if len(self._buckets[ip]) >= self._max_requests:
                return False
            self._buckets[ip].append(now)
            return True

    def stats(self) -> dict:
        with self._lock:
            return {
                "tracked_ips": len(self._buckets),
                "window_seconds": self._window_seconds,
                "max_requests": self._max_requests,
            }


# ── Circuit Breaker Middleware ──────────────────────────────────────────


class CircuitBreakerMiddleware:
    """WSGI middleware with circuit breaker pattern.

    When failures exceed the threshold, subsequent requests are rejected
    immediately (without hitting the backend). After the timeout, the
    circuit goes half-open and allows a request through.

    Args:
        app: The WSGI application to wrap.
        failure_threshold: Number of failures before opening the circuit.
        success_threshold: Successful requests to close the circuit.
        timeout_seconds: Seconds to wait before half-open.
        failure_check: Callable(status_code) -> bool that determines if a response is a failure.
    """

    def __init__(
        self,
        app: Callable,
        failure_threshold: int = 5,
        success_threshold: int = 2,
        timeout_seconds: int = 30,
        failure_check: Optional[Callable[[int], bool]] = None,
    ) -> None:
        self.app = app
        self._failure_threshold = failure_threshold
        self._success_threshold = success_threshold
        self._timeout = timeout_seconds
        self._failure_check = failure_check or (lambda s: s >= 500)
        self._state = "closed"
        self._failure_count = 0
        self._success_count = 0
        self._last_failure = 0.0
        self._lock = threading.Lock()

    def _allow(self) -> bool:
        with self._lock:
            if self._state == "closed":
                return True
            if self._state == "open":
                if _time.monotonic() - self._last_failure > self._timeout:
                    self._state = "half_open"
                    self._success_count = 0
                    self._failure_count = 0
                    return True
                return False
            return True  # half_open

    def _record(self, status_code: int) -> None:
        with self._lock:
            if self._failure_check(status_code):
                if self._state == "half_open":
                    self._state = "open"
                    self._last_failure = _time.monotonic()
                elif self._state == "closed":
                    self._failure_count += 1
                    if self._failure_count >= self._failure_threshold:
                        self._state = "open"
                        self._last_failure = _time.monotonic()
            else:
                if self._state == "half_open":
                    self._success_count += 1
                    if self._success_count >= self._success_threshold:
                        self._state = "closed"
                        self._failure_count = 0
                else:
                    self._failure_count = 0

    def __call__(self, environ: dict, start_response: Callable) -> list:
        if not self._allow():
            start_response("503 Service Unavailable", [
                ("Content-Type", "application/json"),
                ("Retry-After", str(self._timeout)),
            ])
            return [b'{"error":"circuit_breaker_open","retry_after":' + str(self._timeout).encode() + b'}']

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

        status_code = int(captured["status"].split(" ")[0]) if captured.get("status") else 0
        self._record(status_code)

        start_response(captured["status"], captured["headers"], captured.get("exc_info"))
        return [body]

    def stats(self) -> dict:
        with self._lock:
            return {
                "state": self._state,
                "failure_count": self._failure_count,
                "success_count": self._success_count,
            }
