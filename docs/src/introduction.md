# b4n1-boost

**The Python Accelerator.** Native middleware for Django, FastAPI and Flask — JSON 10x faster, compression 28x faster.

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-mdBook-blue)](https://b4n1-com.github.io/b4n1-boost/)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![npm](https://img.shields.io/npm/v/b4n1-boost.svg)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet](https://img.shields.io/nuget/v/B4N1.Boost.svg)](https://www.nuget.org/packages/B4N1.Boost)
[![Python](https://img.shields.io/pypi/pyversions/b4n1-boost)](https://pypi.org/project/b4n1-boost/)
[![Tests](https://img.shields.io/badge/tests-772%20passing-brightgreen)](https://pypi.org/project/b4n1-boost/)

[![Total downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FB4N1-com%2Fpublic-repos%2Fmaster%2Fb4n1-boost%2Fbadges%2Fdownloads.json&query=%24.total&label=total%20downloads&color=blue)](https://pypi.org/project/b4n1-boost/)
[![PyPI Downloads/month](https://img.shields.io/pypi/dm/b4n1-boost)](https://pypi.org/project/b4n1-boost/)
[![npm Downloads/month](https://img.shields.io/npm/dm/b4n1-boost)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet Downloads](https://img.shields.io/nuget/dt/B4N1.Boost)](https://www.nuget.org/packages/B4N1.Boost)
[![PyPI total](https://img.shields.io/pepy/dt/b4n1-boost)](https://pepy.tech/project/b4n1-boost)

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
