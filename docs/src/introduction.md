# b4n1-boost

**The Python Accelerator.** Native middleware for Django, FastAPI and Flask — JSON 10x faster, compression 28x faster.

b4n1-boost ships as a precompiled native extension, so there is nothing to compile on your machine. Drop it into an existing project and the hot paths — serialization, compression, static assets — run in native code while your application code stays exactly the same.

## What it does

| Area | What you get |
|---|---|
| **JSON** | Up to 10.5x faster `dumps`, canonical form, validation, batch operations |
| **Compression** | Gzip, Zstd (28x faster) and Brotli, with Content-Type awareness |
| **Middleware** | ETag/304, security headers, CORS, rate limiting, health check, caching |
| **ORM** | Bulk insert through PostgreSQL COPY, 5-10x faster than the ORM path |
| **Serializers** | Django REST Framework output without the serializer overhead |
| **Utilities** | JWT validation, HTML/CSS/JS minification, HTML → Markdown |
| **Background** | Worker-thread offloading with no external queue broker |

## Who it is for

- Teams whose Django or FastAPI app is **CPU-bound on serialization or compression**
- Applications serving **large JSON payloads** or heavy static assets
- Projects that want native speed **without adding a service** (no Redis, no broker)

## Where to go next

- **[Quick Start](quickstart.md)** — one import, running in under a minute
- **[Installation](installation.md)** — supported platforms and Python versions
- **[Performance](performance.md)** — the measured numbers and how to reproduce them
- **[Python SDK](python.md)** — the full API surface

## Design notes

Everything runs in-process. There is no daemon, no sidecar and no network hop: b4n1-boost is a library you import. When the native core is unavailable, the documented fallbacks are explicit — the package never silently pretends a fast path is active. Call `status()` at any time to see exactly which engines are live (see [Status & Diagnostics](status.md)).
