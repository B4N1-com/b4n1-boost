<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

# 📦 b4n1-boost

**Der polyglotte Beschleuniger. Ein nativer Kern, sieben SDKs – Python, Node.js, Ruby, PHP, Java, .NET und Go. JSON 3-5x schneller, Komprimierung ~21x schneller (gemessen), Antwort-Cache, Bloom-Filter und Schutzschalter in jedem Kern-SDK.**

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
[![Tests](https://img.shields.io/badge/tests-1253%20passing-brightgreen)](https://pypi.org/project/b4n1-boost/)

> 📚 **Vollständiges Handbuch (Installation, Middleware, Beschleuniger, Leistung):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 Plattformunterstützung

| Plattform | Architekturen |
|----------|---------------|
| **Linux** | x86_64, aarch64 |
| **macOS** | x86_64, arm64 (Apple Silicon) |
| **Windows** | x86_64 |

**Vorkompilierte Binärdateien für jede Plattform und jede Sprache** – kein Compiler erforderlich, sofort einsatzbereit.

---

## 📦 Installation – 7 Register, 1 Kern

| Registrierung | Sprache | Paket | Befehl |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET / C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **Maven** | Java / Kotlin | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.4'` |
| **RubyGems** | Rubin / Rack | `b4n1-boost` | `gem install b4n1-boost` |
| **Verpacker** | PHP / Laravel | `b4n1/boost` | `composer require b4n1/boost` |
| **Gehen** | Gehen Sie 1,23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

Alle sieben Pakete liefern den **gleichen nativen Kern** (vorkompiliert, kein Compiler).
benötigt). Das Python-Rad bündelt zusätzlich die HTTP-Middleware-Suite und
Die Ruby/PHP/Go-Pakete bündeln die native Bibliothek für ihre Plattform.

---

**Sprachen:** [العربية](i18n/README.ar.md) · [Deutsch](i18n/README.de.md) · [Español](i18n/README.es.md) · [Französisch](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [Italienisch](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Português (BR)](i18n/README.pt-BR.md) · [Russisch](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 Was Ihnen jedes SDK bietet

| Fähigkeit | Python | Node.js | Java / Kotlin | .NETTO | Rubin | PHP | Gehen |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Antwortcache (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Bloom-Filter | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Leistungsschalter | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Gzip/Zstd-Komprimierung | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTML-Minimierung | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| JSON-Validierung | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP-Middleware (Komprimierung, ETag, CORS, Ratenlimit, Sicherheitsheader, Dekomprimierung, Gesundheitsprüfung) | ✅ | Äußern | — | ASP.NET | Gestell | Laravel | — |
| Zstd-Dekomprimierung | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Hintergrundaufgaben (kein Redis, kein Celery) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Brotli-Komprimierung | ✅ | — | — | — | — | — | — |
| Minimierung (CSS / JS) + HTML→Markdown | ✅ | — | — | — | — | — | — |
| JWT-Validierung | ✅ | — | — | — | — | — | — |
| JSON-Engine 3.1-5.0x schneller | ✅ | — | — | — | — | — | — |
| Django ORM / DRF / SQLAlchemy-Beschleuniger | ✅ | — | — | — | — | — | — |

Die Komprimierung + Minimierung + JSON-Kern ist insgesamt derselbe native Aufruf
sieben Sprachen** (ein C-ABI, vertragsgeprüft pro Sprache). Der Cache, blühen
Filter und Leistungsschalter sind vertragsgeprüft in Python, Node.js, Java und
.NETTO; Ihre Ruby-, PHP- und Go-Wrapper stehen auf der Roadmap.

---

## ⚡ Leistung auf einen Blick

| Komponente | Metrisch | vs. stdlib |
|---|---|---|
| **JSON-Dumps** (native Engine) | 3,1-5,0x schneller als stdlib `json` | Python-Oberfläche, gemessen am 21.10.2026 |
| **Gzip** (nativ) | ~1,0x vs. stdlib gzip Level 6 | 1 MB Nutzlast (die native gzip-Datei ist Level 4) |
| **Zstd** (nativ) | ~21x schneller (Level 1 vs. gzip 4) | 1 MB Nutzlast |
| **Brotli** (einheimisch) | Bestes Verhältnis, ~1,6x LANGSAMER als gzip | 1 MB Nutzlast |
| **DRF-Serialisierer** | noch nicht gemessen | Abfragesatz → JSON |
| **Django ORM** | PostgreSQL-KOPIE | Masseneinfügung nativ |
| **Radgröße** | ~1,4 MB | nativ, kein Compiler erforderlich |
| **No-GIL-fähig** | Python 3.13+ | Free-Threading-Unterstützung |
| **Tests** | 1253 vorbei | Rust 346 (lib + bin) + Python 907, plus die SDK-Vertragssuite ×7 |

---

## 🚀 Schnellstart

### Probieren Sie es mit einem Befehl aus (offline, kein Setup)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` führt den eigenen Benchmark der Engine aus, wo er ausgeführt wird und
druckt, was gerade gemessen wurde – keine gespeicherten Zahlen, keine Prognosen, kein Netzwerk.
Die historischen Multiplikatoren pro Framework werden als Schätzungen gedruckt und beschriftet
als solche.

Bevorzugen Sie eine Datei zur Übergabe? `bash scripts/build-demo-bundle.sh` (oder
`bash cli.sh boost bundle` aus dem Framework-Root) erstellt ein eigenständiges System
ZIP mit der Tonhöhe, dem vollständigen Handbuch, der Binärdatei und einem Ein-Befehl
`demo.sh`.

### Der gemeinsame Kern (Python, Node.js, Java, .NET)

Antwortcache, Bloomfilter und Leistungsschalter – die gleichen nativen Grundelemente in
diese vier SDKs. Vertragserprobt in allen vier Fällen.

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

**.NETTO**
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

### Kompressionsmotor

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.NETTO**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Java / Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**Rubin**
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

**Gehen**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Express / ASP.NET-Middleware

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 Die vollständige Nutzung aller Sprachen finden Sie im **[Handbuch](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Python-Suite (Middleware + Beschleuniger)

Das Python-Paket ist das umfassendste: alles oben Genannte sowie HTTP
Middleware-Suite und die Framework-Beschleuniger.

```bash
pip install b4n1-boost
```

Vorkompilierte native Räder für Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) und Windows (x86_64). Kein Compiler erforderlich.

**Unterstützte Python-Versionen:** 3.10, 3.11, 3.12, 3.13

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

### Flasche
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Automatische Erkennung
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### Einzeilige Installation der gesamten Middleware
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 Funktionen

### JSON-Serialisierung (3,1-5,0x schneller als stdlib `json`)
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

### Komprimierung (~21x schneller als gzip Level 4, GIL-frei)
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

### Inhaltstypbewusste Middleware
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304-Caching
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Ratenbegrenzung
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### Sicherheitsheader
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

### Gesundheitscheck
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### Cache-Schicht
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

### JWT-Validierung
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### HTML/CSS/JS-Minimierung
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

### Telemetrie
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

### Hintergrundarbeiter (Null-GIL)
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

## 🔍 Status und Diagnose

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.4.4', 'native_extension': True, 'features': [...]}
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
-npm: https://www.npmjs.com/package/b4n1-boost
- NuGet: https://www.nuget.org/packages/B4N1.Boost
- Maven Central: https://central.sonatype.com/artifact/com.b4n1/boost
- RubyGems: https://rubygems.org/gems/b4n1-boost
- Paketist: https://packagist.org/packages/b4n1/boost
- Gehen: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- Repository: https://github.com/B4N1-com/b4n1-boost
- Lizenzierung: https://b4n1.com/licensing oder `b4n1@b4n1.com`
- Änderungsprotokoll: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 Lizenz

**Business Source-Lizenz 1.1 (`BUSL-1.1`)** – Beachten Sie, dass dies *nicht* die SPDX-ID ist `BSL-1.1`, was die bezeichnet Boost Software License.

- **Kostenlos** für Entwicklung, Evaluierung, Tests, persönliche Projekte und Startups mit einem Jahresumsatz von weniger als **100.000 USD**.
- **Kommerzielle Lizenz** erforderlich für Organisationen >= **100.000 USD**, Regierungsbehörden und öffentliche Ausschreibungen.
- Nach **Änderungsdatum** (4 Jahre) → **Apache-Lizenz 2.0**.

Siehe [LIZENZ](LICENSE) zum Volltext.

---

_b4n1-boost: Der polyglotte Beschleuniger. Ein nativer Kern, sieben SDKs. JSON 3-5x schneller. Komprimierung ~21x schneller als gzip Level 4. Middleware transparent. Gebaut mit ❤️ von B4N1._
