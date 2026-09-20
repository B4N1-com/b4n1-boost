<div align="center">

# 📦 b4n1-boost

**The Python Accelerator. Native middleware for Django, FastAPI, Flask — JSON 10x faster, compression 28x faster.**

[![License](https://img.shields.io/badge/license-BSL%201.1-lightgrey)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/b4n1-boost?label=downloads%2Fmonth)](https://pypi.org/project/b4n1-boost/)
[![Downloads](https://img.shields.io/pepy/n/b4n1-boost?label=downloads)](https://pepy.tech/project/b4n1-boost)
[![Python](https://img.shields.io/pypi/pyversions/b4n1-boost)](https://pypi.org/project/b4n1-boost/)
[![Tests](https://img.shields.io/badge/tests-772%20passing-brightgreen)](https://pypi.org/project/b4n1-boost/)

</div>

## ⚡ Performance at a Glance

| Component | Metric | vs stdlib |
|---|---|---|
| **JSON dumps** (orjson) | 10.5x faster | Medium dicts (20 users) |
| **JSON dumps** (orjson) | 8.5x faster | Large dicts (500 users) |
| **Gzip** (native) | 1.47x faster | 1MB payloads |
| **Zstd** (native) | 28x faster | 1MB payloads |
| **Brotli** (native) | Best ratio | 1MB payloads |
| **DRF serializer** | 5-10x faster | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | bulk insert native |
| **Wheel size** | ~1.4MB | simd-json + zstd |
| **PyO3** | 0.28 | Free-threading support |
| **Tests** | 772 passing | Unit + Integration + ASGI + Edge Cases |

---

## 📦 Installation

```bash
pip install b4n1-boost
```

Precompiled native wheels for Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon), and Windows (x86_64). No compiler required.

**Supported Python versions:** 3.10, 3.11, 3.12, 3.13

---

## 🚀 Quick Start

### Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### FastAPI
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Flask
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Auto-detection
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### One-line install all middleware
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 Features

### JSON Serialization (10x faster)
```python
from b4n1_boost import NativeJson, canonicalize_json, validate_json

# Fast JSON dumps (uses orjson when available, 10x faster)
result = NativeJson.dumps({"users": [...]})

# Direct PyO3 path (no intermediate conversion)
result = NativeJson.dumps_direct(data)

# Batch: serialize N objects in a single GIL acquire
results = NativeJson.batch_dumps([obj1, obj2, obj3])

# Canonicalize: sorted keys, compact form (accepts str or dict)
canonicalize_json({"z": 1, "a": 2})  # '{"a":2,"z":1}'

# Fast JSON validation
validate_json('{"valid": true}')  # True
```

### Compression (28x faster, GIL-free)
```python
from b4n1_boost import compress

compressed = compress(payload, "zstd")   # 28x faster than stdlib gzip
compressed = compress(payload, "brotli") # Best ratio
compressed = compress(payload, "gzip")   # 1.47x faster than stdlib

# Static file compression
from b4n1_boost import compress_static_file, compress_static_dir
compress_static_file("app/static/app.js", algorithm="zstd")
compress_static_dir("app/static/", algorithm="zstd")
```

### Content-Type Aware Middleware
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 Caching
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Rate Limiting
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### Security Headers
```python
from b4n1_boost.middleware import SecurityHeadersMiddleware
app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
# Adds: X-Content-Type-Options, X-Frame-Options, HSTS, X-XSS-Protection, etc.
```

### CORS
```python
from b4n1_boost.middleware import CORSMiddleware
app.wsgi_app = CORSMiddleware(app.wsgi_app, allow_origins=["https://example.com"])
```

### Health Check
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### Cache Layer
```python
from b4n1_boost.advanced import ResponseCache
from b4n1_boost.middleware import CacheMiddleware

cache = ResponseCache(max_size=1000, ttl_seconds=300)
app.wsgi_app = CacheMiddleware(app.wsgi_app, cache=cache)
```

### Django ORM Accelerator
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — 5-10x faster than Django ORM
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### DRF Serializer Accelerator
```python
from b4n1_boost.drf_accelerator import fast_serialize, FastSerializerMixin

# queryset → JSON without DRF overhead (5-10x faster)
json_bytes = fast_serialize(queryset, fields=["id", "name", "email"])

# Mixin for existing serializers
class MySerializer(FastSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ["id", "name"]
```

### JWT Validation
```python
from b4n1_boost.advanced import validate_jwt

# Rust-native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### HTML/CSS/JS Minification
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → Markdown (Agentic)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### Telemetry
```python
from b4n1_boost import telemetry_init, capture_error, log_info, log_phase, flush

telemetry_init(dsn="https://...")
capture_error(Exception("something"), context={"user": "123"})
log_info("Request processed", phase="http")
flush()
```

### Background Worker (zero-GIL)
```python
from b4n1_boost import worker_compress, worker_decompress, worker_minify_html, worker_validate_jwt

# Heavy ops offloaded to background thread — no GIL contention
future = worker_compress(data, "zstd")
compressed = future.result()
```

---

## 🔍 Status & Diagnostics

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.3.4', 'native_extension': True, 'features': [...]}
```

```python
# Run hardware benchmarks
report = b4n1_boost.run_benchmarks(iterations=100_000)
```

```python
# Generate fresh HTML status report
# python3 generate_report.py --open
```

---

## 🔗 Links

- Website: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- Repository: https://github.com/B4N1-com/b4n1-boost
- Licensing: https://b4n1.com/licensing or `b4n1@b4n1.com`
- Changelog: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 License

**Business Source License 1.1 (BSL 1.1)**.

- **Free** for development, evaluation, testing, personal projects, and startups under **$100K USD** annual revenue.
- **Commercial license** required for organizations >= **$100K USD**, government agencies, and public bidding.
- After **Change Date** (4 years) → **Apache License 2.0**.

See [LICENSE](LICENSE) for full text.

---

_b4n1-boost: The Python Accelerator. JSON 10x faster. Compression 28x faster. Middleware transparent. Built with ❤️ by B4N1._
