<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

#📦 b4n1-boost

**L'acceleratore poliglotta. Un core nativo, sette SDK: Python, Node.js, Ruby, PHP, Java, .NET e Go. JSON 3-5 volte più veloce, compressione ~21 volte più veloce (misurata), cache di risposta, filtro Bloom e interruttore di circuito in ogni SDK core.**

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

> 📚 **Manuale completo (installazione, middleware, acceleratori, prestazioni):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥Supporto della piattaforma

| Piattaforma | Architetture |
|----------|---------------|
| **Linux** | x86_64, aarch64 |
| **macOS** | x86_64, arm64 (Apple Silicon) |
| **Finestre** | x86_64 |

**Binari precompilati per ogni piattaforma e ogni linguaggio**: non è richiesto alcun compilatore, funziona immediatamente.

---

## 📦 Installazione: 7 registri, 1 core

| Registro | Lingua | Pacchetto | Comando |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET/C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **Esperto** | Java/Kotlin | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.6'` |
| **GemmeRubino** | Rubino/Cremagliera | `b4n1-boost` | `gem install b4n1-boost` |
| **Packagista** | PHP/Laravel | `b4n1/boost` | `composer require b4n1/boost` |
| **Andare** | Vai 1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

Tutti e sette i pacchetti contengono lo **stesso core nativo** (precompilato, senza compilatore
necessario). La ruota Python raggruppa inoltre la suite middleware HTTP e
i pacchetti Ruby/PHP/Go raggruppano la libreria nativa per la loro piattaforma.

---

**Lingue:** [العربية](i18n/README.ar.md) · [Tedesco](i18n/README.de.md) · [Spagnolo](i18n/README.es.md) · [Francese](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [Italiano](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Portoghese (BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 Cosa ti offre ogni SDK

| Capacità | Pitone | Node.js | Java/Kotlin | .NETTO | Rubino | PHP | Andare |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Cache di risposta (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Filtro Bloom | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Interruttore automatico | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Compressione Gzip/Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Minimizzazione HTML | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Convalida JSON | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Middleware HTTP (compressione, ETag, CORS, limite di velocità, intestazioni di sicurezza, decompressione, controllo dello stato) | ✅ | Esprimere | — | ASP.NET | Cremagliera | Laravel | — |
| Decompressione Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Attività in background (no Redis, no Celery) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Compressione Brotli | ✅ | — | — | — | — | — | — |
| Minimizzazione (CSS / JS) + HTML→Markdown | ✅ | — | — | — | — | — | — |
| Convalida JWT | ✅ | — | — | — | — | — | — |
| Motore JSON 3,1-5,0 volte più veloce | ✅ | — | — | — | — | — | — |
| Acceleratori Django ORM / DRF / SQLAlchemy | ✅ | — | — | — | — | — | — |

Il core compressione + minimizzazione + JSON è la **stessa chiamata nativa in tutto
sette lingue** (un C-ABI, testato a contratto per lingua). La cache, sboccia
il filtro e l'interruttore automatico sono testati a contratto in Python, Node.js, Java e
.NETTO; i loro wrapper Ruby, PHP e Go sono sulla tabella di marcia.

---

## ⚡ Prestazioni in breve

| Componente | Metrico | rispetto a stdlib |
|---|---|---|
| **Dump JSON** (motore nativo) | 3,1-5,0 volte più veloce di stdlib `json` | Superficie di Python, misurata il 21-10-2026 |
| **Gzip** (nativo) | ~1.0x rispetto a stdlib gzip livello 6 | Payload da 1 MB (il gzip nativo è di livello 4) |
| **Zstd** (nativo) | ~21 volte più veloce (livello 1 rispetto a gzip 4) | Carichi utili da 1 MB |
| **Brotli** (nativo) | Miglior rapporto, ~1,6 volte PIÙ LENTO di gzip | Carichi utili da 1 MB |
| **Serializzatore DRF** | non ancora misurato | set di query → JSON |
| **Django ORM** | COPIA PostgreSQL | inserimento collettivo nativo |
| **Misura della ruota** | ~1,4 MB | nativo, non è necessario alcun compilatore |
| **No-GIL pronto** | Python 3.13+ | Supporto per threading libero |
| **Test** | 1253 passaggio | Rust 346 (lib + bin) + Python 907, più la suite di contratti SDK ×7 |

---

## 🚀Avvio rapido

### Provalo con un comando (offline, nessuna configurazione)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` esegue il benchmark del motore in cui viene eseguito e
stampa ciò che ha appena misurato: nessuna cifra memorizzata, nessuna proiezione, nessuna rete.
I moltiplicatori storici per quadro vengono stampati come stime, etichettati
come tale.

Preferisci un file che puoi consegnare? `bash scripts/build-demo-bundle.sh` (O
`bash cli.sh boost bundle` dalla radice del framework) costruisce un file autonomo
ZIP con il tono, il manuale completo, il binario e un comando singolo
`demo.sh`.

### Il core condiviso (Python, Node.js, Java, .NET)

Cache di risposta, filtro Bloom e interruttore automatico: gli stessi primitivi nativi presenti
questi quattro SDK. Testato a contratto in tutti e quattro.

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

**Java/Kotlin**
```java
import com.b4n1.boost.NativeResponseCache;

try (NativeResponseCache cache = new NativeResponseCache(8)) {
    cache.set("user:1", "{\"id\":1}".getBytes(StandardCharsets.UTF_8), 200, 60_000);
}
```

**Pitone**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### Motore di compressione

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

**Java/Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**Rubino**
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

**Andare**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Middleware Express/ASP.NET

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 L'utilizzo completo di ogni lingua è disponibile nel **[manual](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Suite Python (middleware + acceleratori)

Il pacchetto Python è quello più completo: tutto quanto sopra, più HTTP
suite middleware e gli acceleratori del framework.

```bash
pip install b4n1-boost
```

Volanti nativi precompilati per Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) e Windows (x86_64). Nessun compilatore richiesto.

**Versioni Python supportate:** 3.10, 3.11, 3.12, 3.13

###Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### API veloce
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Pallone
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Rilevamento automatico
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### Installa tutto il middleware da una riga
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧Caratteristiche

### Serializzazione JSON (3,1-5,0 volte più veloce di stdlib `json`)
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

### Compressione (~21 volte più veloce di gzip livello 4, senza GIL)
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

### Middleware compatibile con il tipo di contenuto
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 Memorizzazione nella cache
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Limitazione della velocità
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### Intestazioni di sicurezza
```python
from b4n1_boost.middleware import SecurityHeadersMiddleware
app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
# Adds: X-Content-Type-Options, X-Frame-Options, HSTS, X-XSS-Protection, etc.
```

### CORSO
```python
from b4n1_boost.middleware import CORSMiddleware
app.wsgi_app = CORSMiddleware(app.wsgi_app, allow_origins=["https://example.com"])
```

### Controllo dello stato di salute
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### Livello cache
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Acceleratore Django ORM
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### Acceleratore serializzatore DRF
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

### Convalida JWT
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### Minimizzazione HTML/CSS/JS
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → Ribasso (Agent)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### Telemetria
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

### Lavoratore in background (zero-GIL)
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

## 🔍 Stato e diagnostica

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.4.6', 'native_extension': True, 'features': [...]}
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

## 🔗Link

- Sito web: https://b4n1.com
-PyPI: https://pypi.org/project/b4n1-boost
-npm: https://www.npmjs.com/package/b4n1-boost
-NuGet: https://www.nuget.org/packages/B4N1.Boost
- Centrale Maven: https://central.sonatype.com/artifact/com.b4n1/boost
- Gemme di rubino: https://rubygems.org/gems/b4n1-boost
- Imballatore: https://packagist.org/packages/b4n1/boost
- Andare: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- Deposito: https://github.com/B4N1-com/b4n1-boost
- Licenza: https://b4n1.com/licensing O `b4n1@b4n1.com`
- Registro delle modifiche: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 Licenza

**Licenza Business Source 1.1 (`BUSL-1.1`)** — nota che questo *non* è l'ID SPDX `BSL-1.1`, che denota il Boost Software License.

- **Gratuito** per sviluppo, valutazione, test, progetti personali e startup con entrate annuali inferiori a **$100.000**.
- **Licenza commerciale** richiesta per organizzazioni >= **$ 100.000 USD**, agenzie governative e gare d'appalto pubbliche.
- Dopo la **Data di modifica** (4 anni) → **Licenza Apache 2.0**.

Vedi [LICENZA](LICENSE) per il testo completo.

---

_b4n1-boost: L'acceleratore poliglotta. Un core nativo, sette SDK. JSON 3-5 volte più veloce. Compressione ~21 volte più veloce del livello 4 di gzip. Middleware trasparente. Costruito con ❤️ da B4N1._
