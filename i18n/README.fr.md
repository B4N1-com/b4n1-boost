<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

#📦 b4n1-boost

**L'accélérateur polyglotte. Un noyau natif, sept SDK : Python, Node.js, Ruby, PHP, Java, .NET et Go. JSON 3 à 5 fois plus rapide, compression environ 21 fois plus rapide (mesurée), cache de réponse, filtre Bloom et disjoncteur dans chaque SDK principal.**

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

> 📚 **Manuel complet (installation, middleware, accélérateurs, performances) :**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 Prise en charge de la plateforme

| Plate-forme | Architectures |
|----------|---------------|
| **Linux** | x86_64, aarch64 |
| **macOS** | x86_64, arm64 (Apple Silicon) |
| **Fenêtres** | x86_64 |

**Binaires précompilés pour chaque plateforme et chaque langage** — aucun compilateur requis, fonctionne immédiatement.

---

## 📦 Installation — 7 registres, 1 cœur

| Enregistrement | Langue | Emballer | Commande |
|----------|----------|---------|---------|
| **PyPI** | Python3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Noeud.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET/C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **Maven** | Java/Kotlin | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.7'` |
| **RubisGemmes** | Rubis / Crémaillère | `b4n1-boost` | `gem install b4n1-boost` |
| **Emballeur** | PHP/Laravel | `b4n1/boost` | `composer require b4n1/boost` |
| **Aller** | Allez 1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

Les sept packages sont livrés avec le **même noyau natif** (précompilé, sans compilateur
nécessaire). La roue Python regroupe en outre la suite middleware HTTP, et
les packages Ruby/PHP/Go regroupent la bibliothèque native pour leur plate-forme.

---

**Langues :** [العربية](i18n/README.ar.md) · [Allemand](i18n/README.de.md) · [Espagnol](i18n/README.es.md) · [English](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [italien](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Português (BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 Ce que chaque SDK vous apporte

| Capacité | Python | Noeud.js | Java/Kotlin | .FILET | Rubis | PHP | Aller |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Cache de réponse (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Filtre de floraison | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Disjoncteur | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Compression Gzip/Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Minification HTML | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Validation JSON | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Middleware HTTP (compression, ETag, CORS, limite de débit, en-têtes de sécurité, décompression, bilan de santé) | ✅ | Exprimer | — | ASP.NET | Étagère | Laravel | — |
| Décompression Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tâches en arrière-plan (pas de Redis, pas de céleri) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Compression Brotli | ✅ | — | — | — | — | — | — |
| Minification (CSS / JS) + HTML→Markdown | ✅ | — | — | — | — | — | — |
| Validation JWT | ✅ | — | — | — | — | — | — |
| Moteur JSON 3.1-5.0x plus rapide | ✅ | — | — | — | — | — | — |
| Accélérateurs Django ORM / DRF / SQLAlchemy | ✅ | — | — | — | — | — | — |

Le noyau compression + minification + JSON est le **même appel natif en tout
sept langues** (un C-ABI, testé sous contrat par langue). La cache, fleurir
le filtre et le disjoncteur sont testés sous contrat en Python, Node.js, Java et
.FILET; leurs wrappers Ruby, PHP et Go sont sur la feuille de route.

---

## ⚡ Les performances en un coup d'œil

| Composant | Métrique | contre stdlib |
|---|---|---|
| **Dumps JSON** (moteur natif) | 3.1-5.0x plus rapide que stdlib `json` | Surface Python, mesurée le 21/10/2026 |
| **Gzip** (natif) | ~ 1.0x contre stdlib gzip niveau 6 | Charges utiles de 1 Mo (le gzip natif est de niveau 4) |
| **Zstd** (natif) | ~21x plus rapide (niveau 1 vs gzip 4) | Charges utiles de 1 Mo |
| **Brotli** (natif) | Meilleur rapport, ~1,6x PLUS LENT que gzip | Charges utiles de 1 Mo |
| **Sérialiseur DRF** | pas encore mesuré | ensemble de requêtes → JSON |
| ** Django ORM ** | COPIE PostgreSQL | insertion groupée native |
| **Taille des roues** | ~1,4 Mo | natif, aucun compilateur n'est nécessaire |
| **Pas de GIL prêt** | Python3.13+ | Prise en charge du thread libre |
| **Tests** | 1253 passage | Rust 346 (lib + bin) + Python 907, plus la suite de contrats SDK ×7 |

---

## 🚀 Démarrage rapide

### Essayez-le en une seule commande (hors ligne, pas de configuration)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` exécute le propre benchmark du moteur où il est exécuté et
imprime ce qu'il vient de mesurer - pas de chiffres stockés, pas de projections, pas de réseau.
Les multiplicateurs historiques par framework sont imprimés sous forme d'estimations, étiquetées
en tant que tel.

Vous préférez un dossier que vous pouvez remettre ? `bash scripts/build-demo-bundle.sh` (ou
`bash cli.sh boost bundle` à partir de la racine du framework) construit un
ZIP avec le pitch, le manuel complet, le binaire et une one-command
`demo.sh`.

### Le noyau partagé (Python, Node.js, Java, .NET)

Cache de réponse, filtre Bloom et disjoncteur : les mêmes primitives natives dans
ces quatre SDK. Testé sous contrat dans les quatre cas.

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

**.FILET**
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

**Python**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### Moteur de compression

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.FILET**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Java/Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**Rubis**
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

**Aller**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Intergiciel Express / ASP.NET

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 L'utilisation complète de chaque langue se trouve dans le **[manuel](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Suite Python (middleware + accélérateurs)

Le package Python est le plus complet : tout ce qui précède, plus le HTTP
suite middleware et les accélérateurs de framework.

```bash
pip install b4n1-boost
```

Roues natives précompilées pour Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) et Windows (x86_64). Aucun compilateur requis.

**Versions Python prises en charge :** 3.10, 3.11, 3.12, 3.13

### Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### API rapide
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Flacon
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Détection automatique
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### Installation en une seule ligne de tous les middlewares
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 Fonctionnalités

### Sérialisation JSON (3.1-5.0x plus rapide que stdlib `json`)
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

### Compression (~21x plus rapide que gzip niveau 4, sans GIL)
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

### Middleware prenant en compte le type de contenu
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / Mise en cache 304
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Limitation du débit
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### En-têtes de sécurité
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

### Bilan de santé
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### Couche de cache
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Accélérateur ORM Django
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### Accélérateur de sérialiseur DRF
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

### Validation JWT
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### Minification HTML/CSS/JS
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

### Télémétrie
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

### Travailleur d'arrière-plan (zéro-GIL)
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

## 🔍 État et diagnostics

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.4.7', 'native_extension': True, 'features': [...]}
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

## 🔗 Liens

- Site web: https://b4n1.com
-PyPI : https://pypi.org/project/b4n1-boost
- npm : https://www.npmjs.com/package/b4n1-boost
- NuGet : https://www.nuget.org/packages/B4N1.Boost
-Maven Central : https://central.sonatype.com/artifact/com.b4n1/boost
- RubyGems : https://rubygems.org/gems/b4n1-boost
- Packagiste : https://packagist.org/packages/b4n1/boost
- Aller: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- Référentiel : https://github.com/B4N1-com/b4n1-boost
- Licence : https://b4n1.com/licensing ou `b4n1@b4n1.com`
- Journal des modifications : [CHANGELOG.md](CHANGELOG.md)

---

## 📄 Licence

**Licence Business Source 1.1 (`BUSL-1.1`)** — notez qu'il ne s'agit *pas* de l'identifiant SPDX `BSL-1.1`, qui désigne le Boost Software License.

- **Gratuit** pour le développement, l'évaluation, les tests, les projets personnels et les startups d'un chiffre d'affaires annuel inférieur à **100 000 USD**.
- **Licence commerciale** requise pour les organisations >= **100 000 USD**, les agences gouvernementales et les appels d'offres publics.
- Après **Date de changement** (4 ans) → **Licence Apache 2.0**.

Voir [LICENCE](LICENSE) pour le texte intégral.

---

_b4n1-boost: L'accélérateur polyglotte. Un cœur natif, sept SDK. JSON 3 à 5 fois plus rapide. Compression ~21 fois plus rapide que le niveau gzip 4. Middleware transparent. Construit avec ❤️ par B4N1._
