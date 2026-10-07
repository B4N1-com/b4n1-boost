# Middleware Reference

Middleware is where most of the practical speedup lives. Each class is
independent — use one, or stack them.

## Compression

```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)
```

Content-Type aware: it compresses what benefits from it and skips what does
not — images, video, audio, fonts, archives and anything already compressed.
`min_size` avoids spending CPU on payloads too small to gain.

### ASGI / FastAPI

```python
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware

app.add_middleware(FastAPIBoostCompressionMiddleware)
```

Streaming responses are compressed incrementally rather than buffered, so a
large streamed response does not have to be materialized in memory first.

## ETag / 304 caching

```python
from b4n1_boost.middleware import ETagMiddleware

app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

Clients that already hold a valid copy get `304 Not Modified` and no body,
saving both bandwidth and serialization work on repeat requests.

ASGI variant: `ASGIETagMiddleware`.

## Security headers

```python
from b4n1_boost.middleware import SecurityHeadersMiddleware

app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
```

Adds `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`,
`X-XSS-Protection` and related headers.

ASGI variant: `ASGISecurityHeadersMiddleware`.

## CORS

```python
from b4n1_boost.middleware import CORSMiddleware

app.wsgi_app = CORSMiddleware(app.wsgi_app,
                              allow_origins=["https://example.com"])
```

ASGI variant: `ASGICORSMiddleware`.

## Rate limiting

```python
from b4n1_boost.middleware import RateLimitMiddleware

app.wsgi_app = RateLimitMiddleware(app.wsgi_app,
                                   max_requests=100,
                                   window_seconds=60)
```

Fixed-window limiting held in process. It is a guard against accidental
abuse and hot loops, not a distributed quota — for limits that must hold
across many processes, enforce them at the edge.

ASGI variant: `ASGIRateLimitMiddleware`.

## Health check

```python
from b4n1_boost.middleware import HealthCheckMiddleware

app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health -> 200 {"status": "ok"}
```

Answers without touching application code, which keeps a health probe from
consuming a worker.

ASGI variant: `ASGIHealthCheckMiddleware`.

## Response cache

```python
from b4n1_boost.advanced import ResponseCache
from b4n1_boost.middleware import CacheMiddleware

cache = ResponseCache(max_size=1000, ttl_seconds=300)
app.wsgi_app = CacheMiddleware(app.wsgi_app, cache=cache)
```

`max_size` is a hard bound on entries held — the cache never grows without
limit. Entries expire after `ttl_seconds`.

## Request logging

```python
from b4n1_boost.middleware import RequestLoggingMiddleware

app.wsgi_app = RequestLoggingMiddleware(app.wsgi_app)
```

ASGI variant: `ASGIRequestLoggingMiddleware`.

## Decompression

```python
from b4n1_boost.middleware import DecompressionMiddleware

app.wsgi_app = DecompressionMiddleware(app.wsgi_app)
```

Handles incoming `Content-Encoding` so endpoints can accept compressed
request bodies.

## Metrics

```python
from b4n1_boost.middleware import CompressionMetrics, detect_proxy, metrics
```

`CompressionMetrics` tracks what was compressed and by how much, which is
the fastest way to find out whether compression is earning its CPU time.

## Proxy detection

```python
from b4n1_boost.middleware import detect_proxy
```

Determines whether a reverse proxy is in front of the app, so headers such
as `X-Forwarded-For` are only trusted when they came from one.

## Ordering

Apply middleware in this order of intent:

1. **Proxy / trust boundary** — establish what headers you believe
2. **Security headers** — applied to every response
3. **Rate limiting** — reject early, before expensive work
4. **Compression** — last transform before bytes leave
5. **ETag / cache** — after the body is final

Reversing 4 and 5 produces incorrect ETags, because the validator would be
computed over a body that no longer matches what the client receives.

## See also

- [Quick Start](quickstart.md) — the one-line installers
- [Python SDK](python.md) — utilities alongside the middleware
