<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

# 📦 b4n1-boost

**The polyglot accelerator. One native core, seven SDKs — Python, Node.js, Ruby, PHP, Java, .NET and Go. JSON 3-5x faster, compression ~21x faster (measured), response cache, bloom filter and circuit breaker in every core SDK.**

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-mdBook-blue)](https://b4n1-com.github.io/b4n1-boost/)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![Python versions](https://img.shields.io/pypi/pyversions/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![PyPI downloads](https://img.shields.io/pypi/dm/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![Pepy downloads](https://img.shields.io/pepy/dt/b4n1-boost.svg)](https://pepy.tech/project/b4n1-boost)
[![npm](https://img.shields.io/npm/v/b4n1-boost.svg)](https://www.npmjs.com/package/b4n1-boost)
[![npm downloads](https://img.shields.io/npm/dm/b4n1-boost.svg)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet](https://img.shields.io/nuget/v/B4N1.Boost.svg)](https://www.nuget.org/packages/B4N1.Boost)
[![NuGet downloads](https://img.shields.io/nuget/dt/B4N1.Boost.svg)](https://www.nuget.org/packages/B4N1.Boost)
[![Maven Central](https://img.shields.io/maven-central/v/com.b4n1/boost.svg)](https://central.sonatype.com/artifact/com.b4n1/boost)
[![RubyGems](https://img.shields.io/gem/v/b4n1-boost.svg)](https://rubygems.org/gems/b4n1-boost)
[![Packagist](https://img.shields.io/packagist/v/b4n1/boost.svg)](https://packagist.org/packages/b4n1/boost)
[![Go Reference](https://pkg.go.dev/badge/github.com/B4N1-com/b4n1-boost/sdks/go.svg)](https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go)
[![Tests](https://img.shields.io/badge/tests-948%20passing-brightgreen)](https://pypi.org/project/b4n1-boost/)

> 📚 **Full manual (installation, middleware, accelerators, performance):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 Platform Support

| Platform | Architectures |
|----------|---------------|
| **Linux** | x86_64, aarch64 |
| **macOS** | x86_64, arm64 (Apple Silicon) |
| **Windows** | x86_64 |

**Pre-compiled binaries for every platform and every language** — no compiler required, works out of the box.

---

## 📦 Installation — 7 registries, 1 core

| Registry | Language | Package | Command |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET / C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **Maven** | Java / Kotlin | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.2'` |
| **RubyGems** | Ruby / Rack | `b4n1-boost` | `gem install b4n1-boost` |
| **Packagist** | PHP / Laravel | `b4n1/boost` | `composer require b4n1/boost` |
| **Go** | Go 1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

All seven packages ship the **same native core** (pre-compiled, no compiler
needed). The Python wheel additionally bundles the HTTP middleware suite, and
the Ruby/PHP/Go packages bundle the native lib for their platform.

---

**Languages:** [العربية](i18n/README.ar.md) · [Deutsch](i18n/README.de.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [Italiano](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Português (BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 What each SDK gives you

| Capability | Python | Node.js | Java / Kotlin | .NET | Ruby | PHP | Go |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Response cache (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Bloom filter | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Circuit breaker | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Gzip / Zstd compression | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTML minification | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| JSON validation | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP middleware (compression, ETag, CORS, rate limit, security headers) | ✅ | Express | — | ASP.NET | Rack | Laravel | — |
| JSON engine 3.1-5.0x faster | ✅ | — | — | — | — | — | — |
| Django ORM / DRF accelerators | ✅ | — | — | — | — | — | — |

The compression + minification + JSON core is the **same native call in all
seven languages** (one C-ABI, contract-tested per language). The cache, bloom
filter and circuit breaker are contract-tested in Python, Node.js, Java and
.NET; their Ruby, PHP and Go wrappers are on the roadmap.

---

## ⚡ Performance at a Glance

| Component | Metric | vs stdlib |
|---|---|---|
| **JSON dumps** (native engine) | 3.1-5.0x faster than stdlib `json` | Python surface, measured 2026-10-21 |
| **Gzip** (native) | ~1.0x vs stdlib gzip level 6 | 1MB payloads (the native gzip is level 4) |
| **Zstd** (native) | ~21x faster (level 1 vs gzip 4) | 1MB payloads |
| **Brotli** (native) | Best ratio, ~1.6x SLOWER than gzip | 1MB payloads |
| **DRF serializer** | not measured yet | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | bulk insert native |
| **Wheel size** | ~1.4MB | native, no compiler needed |
| **No-GIL ready** | Python 3.13+ | Free-threading support |
| **Tests** | 1253 passing | Rust 346 (lib + bin) + Python 907, plus the SDK contract suite ×7 |

---

## 🚀 Quick Start

### Try it in one command (offline, no setup)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` runs the engine's own benchmark where it is executed and
prints what it just measured — no stored figures, no projections, no network.
The historical per-framework multipliers are printed as estimates, labelled
as such.

Prefer a file you can hand over? `bash scripts/build-demo-bundle.sh` (or
`bash cli.sh boost bundle` from the framework root) builds a self-contained
ZIP with the pitch, the full manual, the binary and a one-command
`demo.sh`.

### The shared core (Python, Node.js, Java, .NET)

Response cache, bloom filter and circuit breaker — the same native primitives in
these four SDKs. Contract-tested in all four.

**Node.js**
```javascript
const { ResponseCache, BloomFilter, CircuitBreaker } = require('b4n1-boost/core.js');

const cache = new ResponseCache(1024);                       // capacity
cache.set('user:1', JSON.stringify({ id: 1 }), 200, 60);    // key, body, status, ttl (s)

const seen = new BloomFilter(100_000, 0.01);                // expected items, fp rate
if (!seen.checkAndSet('already-processed')) { /* first time we see it */ }

const breaker = new CircuitBreaker(5, 2, 30);               // threshold, successes, timeout (s)
if (!breaker.allows()) return fallback();
```

**.NET**
```csharp
using B4N1.Boost;

using var cache = new NativeResponseCache(1024);
cache.Set("user:1", Encoding.UTF8.GetBytes("{\"id\":1}"), 200, 60);

using var seen = new NativeBloomFilter(100_000, 0.01);
bool firstTime = !seen.CheckAndSet("already-processed");

var breaker = new NativeCircuitBreaker(5, 2, 30);
if (!breaker.Allows) return Fallback();
```

**Java / Kotlin**
```java
import com.b4n1.boost.NativeResponseCache;

try (NativeResponseCache cache = new NativeResponseCache(8)) {
    cache.set("user:1", "{\"id\":1}".getBytes(StandardCharsets.UTF_8), 200, 60_000);
}
```

**Python**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### Compression engine

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.NET**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Java / Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**Ruby**
```ruby
require 'boost'

zstd = B4N1::Boost.compress_zstd(payload)
min  = B4N1::Boost.minify_html(html)
ok   = B4N1::Boost.json_valid?(body)
```

**PHP**
```php
use B4N1\Boost;

$zstd = Boost::compressZstd($payload);
$min  = Boost::minifyHtml($html);
$ok   = Boost::isJsonValid($body);
```

**Go**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Express / ASP.NET middleware

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 Full usage for every language lives in the **[manual](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Python suite (middleware + accelerators)

The Python package is the most complete one: everything above, plus the HTTP
middleware suite and the framework accelerators.

```bash
pip install b4n1-boost
```

Precompiled native wheels for Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon), and Windows (x86_64). No compiler required.

**Supported Python versions:** 3.10, 3.11, 3.12, 3.13

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

### JSON Serialization (3.1-5.0x faster than stdlib `json`)
```python
from b4n1_boost import NativeJson, canonicalize_json, validate_json

# Fast JSON dumps (native engine, 3.1-5.0x faster than stdlib `json`)
result = NativeJson.dumps({"users": [...]})

# Direct native path (no intermediate conversion)
result = NativeJson.dumps_direct(data)

# Batch: serialize N objects in a single GIL acquire
results = NativeJson.batch_dumps([obj1, obj2, obj3])

# Canonicalize: sorted keys, compact form (accepts str or dict)
canonicalize_json({"z": 1, "a": 2})  # '{"a":2,"z":1}'

# Fast JSON validation
validate_json('{"valid": true}')  # True
```

### Compression (~21x faster than gzip level 4, GIL-free)
```python
from b4n1_boost import py_compress_zstd, py_compress_gzip, py_compress_brotli

compressed = py_compress_zstd(payload)   # ~21x faster than gzip level 4 (1MB)
compressed = py_compress_brotli(payload) # Best ratio (slower than gzip)
compressed = py_compress_gzip(payload)   # ~1.0x vs stdlib gzip level 6

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

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Django ORM Accelerator
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### DRF Serializer Accelerator
```python
from b4n1_boost.drf_accelerator import fast_serialize, FastSerializerMixin

# queryset → JSON without DRF overhead (speed not measured yet)
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

# Native HMAC-SHA256 (no PyJWT dependency required)
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
from b4n1_boost import (
    telemetry_init,
    telemetry_capture_error,
    telemetry_log_info,
    telemetry_log_phase,
    telemetry_flush,
)

telemetry_init(app="b4n1-boost")
telemetry_capture_error("something failed", {"user": "123"})
telemetry_log_info("Request processed", {"phase": "http"})
telemetry_log_phase("http", "ok", 12)
telemetry_flush()
```

### Background Worker (zero-GIL)
```python
from b4n1_boost import (
    worker_compress,
    worker_decompress,
    worker_minify,
    worker_jwt_validate,
)

# Heavy ops offloaded to the background worker — the caller does not hold
# the GIL while they run
compressed = worker_compress(data, "zstd")
restored = worker_decompress(compressed)
markup = worker_minify(html, "html")
claims = worker_jwt_validate(token, secret)
```

---

## 🔍 Status & Diagnostics

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.4.2', 'native_extension': True, 'features': [...]}
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
- npm: https://www.npmjs.com/package/b4n1-boost
- NuGet: https://www.nuget.org/packages/B4N1.Boost
- Maven Central: https://central.sonatype.com/artifact/com.b4n1/boost
- RubyGems: https://rubygems.org/gems/b4n1-boost
- Packagist: https://packagist.org/packages/b4n1/boost
- Go: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- Repository: https://github.com/B4N1-com/b4n1-boost
- Licensing: https://b4n1.com/licensing or `b4n1@b4n1.com`
- Changelog: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 License

**Business Source License 1.1 (`BUSL-1.1`)** — note this is *not* the SPDX id `BSL-1.1`, which denotes the Boost Software License.

- **Free** for development, evaluation, testing, personal projects, and startups under **$100K USD** annual revenue.
- **Commercial license** required for organizations >= **$100K USD**, government agencies, and public bidding.
- After **Change Date** (4 years) → **Apache License 2.0**.

See [LICENSE](LICENSE) for full text.

---

_b4n1-boost: The polyglot accelerator. One native core, seven SDKs. JSON 3-5x faster. Compression ~21x faster than gzip level 4. Middleware transparent. Built with ❤️ by B4N1._
