<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

# 📦 b4n1-boost

**El acelerador políglota. Un núcleo nativo, siete SDK: Python, Node.js, Ruby, PHP, Java, .NET y Go. JSON entre 3 y 5 veces más rápido, compresión ~21 veces más rápida (medida), caché de respuesta, filtro de floración y disyuntor en cada SDK central.**

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

> 📚 **Manual completo (instalación, middleware, aceleradores, rendimiento):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 Soporte de plataforma

| Plataforma | Arquitecturas |
|----------|---------------|
| **Linux** | x86_64, aarch64 |
| **macOS** | x86_64, arm64 (silicona de Apple) |
| **Windows** | x86_64 |

**Binarios precompilados para cada plataforma y cada idioma**: no se requiere compilador, funciona de inmediato.

---

## 📦 Instalación: 7 registros, 1 núcleo

| Registro | Idioma | Paquete | Dominio |
|----------|----------|---------|---------|
| **PyPI** | Pitón 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Nodo.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET/C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **Maven** | Java/Kotlin | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.4'` |
| **RubíGemas** | Rubí / Estante | `b4n1-boost` | `gem install b4n1-boost` |
| **Empaquetador** | PHP/Laravel | `b4n1/boost` | `composer require b4n1/boost` |
| **Ir** | Ir 1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

Los siete paquetes incluyen el **mismo núcleo nativo** (precompilado, sin compilador)
necesario). La rueda de Python incluye además el conjunto de middleware HTTP y
los paquetes Ruby/PHP/Go incluyen la biblioteca nativa para su plataforma.

---

**Idiomas:** [العربية](i18n/README.ar.md) · [alemán](i18n/README.de.md) · [English](i18n/README.es.md) · [francés](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [italiano](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Portugués (BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 Qué te aporta cada SDK

| Capacidad | Pitón | Nodo.js | Java/Kotlin | .NETO | Rubí | PHP | Ir |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Caché de respuesta (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Filtro de floración | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Cortacircuitos | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Compresión Gzip/Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Minificación HTML | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| validación JSON | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Middleware HTTP (compresión, ETag, CORS, límite de velocidad, encabezados de seguridad, descompresión, verificación de estado) | ✅ | Expresar | — | ASP.NET | Estante | Laravel | — |
| descompresión zstd | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Tareas en segundo plano (sin Redis, sin Apio) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| compresión brotli | ✅ | — | — | — | — | — | — |
| Minificación (CSS/JS) + HTML→Markdown | ✅ | — | — | — | — | — | — |
| validación JWT | ✅ | — | — | — | — | — | — |
| Motor JSON entre 3,1 y 5,0 veces más rápido | ✅ | — | — | — | — | — | — |
| Aceleradores Django ORM/DRF/SQLAlchemy | ✅ | — | — | — | — | — | — |

El núcleo de compresión + minificación + JSON es **la misma llamada nativa en todos
siete idiomas** (un C-ABI, probado por contrato por idioma). El caché, florece.
El filtro y el disyuntor se prueban por contrato en Python, Node.js, Java y
.NETO; sus contenedores Ruby, PHP y Go están en la hoja de ruta.

---

## ⚡ Rendimiento de un vistazo

| Componente | Métrico | frente a stdlib |
|---|---|---|
| **Volcados JSON** (motor nativo) | 3,1-5,0 veces más rápido que stdlib `json` | Superficie de Python, medida 2026-10-21 |
| **Gzip** (nativo) | ~1.0x frente a stdlib gzip nivel 6 | Cargas útiles de 1 MB (el gzip nativo es de nivel 4) |
| **Zstd** (nativo) | ~21 veces más rápido (nivel 1 frente a gzip 4) | Cargas útiles de 1 MB |
| **Brotli** (nativo) | Mejor relación, ~1,6 veces MÁS LENTO que gzip | Cargas útiles de 1 MB |
| **Serializador DRF** | aún no medido | conjunto de consultas → JSON |
| **Django ORM** | COPIA de PostgreSQL | inserción masiva nativa |
| **Tamaño de rueda** | ~1,4MB | nativo, no se necesita compilador |
| **Listo para no GIL** | Pitón 3.13+ | Soporte de subprocesos gratuitos |
| **Pruebas** | 1253 pasando | Rust 346 (lib + bin) + Python 907, más el conjunto de contratos SDK ×7 |

---

## 🚀 Inicio rápido

### Pruébelo con un solo comando (sin conexión, sin configuración)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` ejecuta el propio punto de referencia del motor donde se ejecuta y
imprime lo que acaba de medir: sin cifras almacenadas, sin proyecciones, sin red.
Los multiplicadores históricos por marco se imprimen como estimaciones, etiquetados
tal como.

¿Prefieres un archivo que puedas entregar? `bash scripts/build-demo-bundle.sh` (o
`bash cli.sh boost bundle` desde la raíz del marco) construye un sistema autónomo
ZIP con el tono, el manual completo, el binario y un comando
`demo.sh`.

### El núcleo compartido (Python, Node.js, Java, .NET)

Caché de respuesta, filtro de floración y disyuntor: las mismas primitivas nativas en
estos cuatro SDK. Probado por contrato en los cuatro.

**Nodo.js**
```javascript
const { ResponseCache, BloomFilter, CircuitBreaker } = require('b4n1-boost/core.js');

const cache = new ResponseCache(1024);                       // capacity
cache.set('user:1', JSON.stringify({ id: 1 }), 200, 60);    // key, body, status, ttl (s)

const seen = new BloomFilter(100_000, 0.01);                // expected items, fp rate
if (!seen.checkAndSet('already-processed')) { /* first time we see it */ }

const breaker = new CircuitBreaker(5, 2, 30);               // threshold, successes, timeout (s)
if (!breaker.allows()) return fallback();
```

**.NETO**
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

**Pitón**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### Motor de compresión

**Nodo.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.NETO**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Java/Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**Rubí**
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

**Ir**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Middleware expreso/ASP.NET

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 El uso completo de cada idioma se encuentra en el **[manual](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Suite Python (middleware + aceleradores)

El paquete Python es el más completo: todo lo anterior, más el HTTP
suite de middleware y aceleradores de framework.

```bash
pip install b4n1-boost
```

Ruedas nativas precompiladas para Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) y Windows (x86_64). No se requiere compilador.

**Versiones de Python compatibles:** 3.10, 3.11, 3.12, 3.13

###Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### API rápida
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### matraz
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Detección automática
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### Instalación de una sola línea de todo el middleware
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 Características

### Serialización JSON (3,1-5,0 veces más rápida que stdlib `json`)
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

### Compresión (~21 veces más rápida que gzip nivel 4, sin GIL)
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

### Middleware compatible con el tipo de contenido
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 Almacenamiento en caché
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Limitación de velocidad
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### Encabezados de seguridad
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

### Control de salud
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### Capa de caché
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Acelerador ORM de Django
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### Acelerador de serializador DRF
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

### Validación JWT
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### Minificación de HTML/CSS/JS
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → Markdown (agente)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### Telemetría
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

### Trabajador en segundo plano (cero-GIL)
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

## 🔍 Estado y diagnóstico

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

## 🔗 Enlaces

- Sitio web: https://b4n1.com
-PyPI: https://pypi.org/project/b4n1-boost
- npm: https://www.npmjs.com/package/b4n1-boost
- NuGet: https://www.nuget.org/packages/B4N1.Boost
-Maven Central: https://central.sonatype.com/artifact/com.b4n1/boost
- RubyGems: https://rubygems.org/gems/b4n1-boost
- Empaquetador: https://packagist.org/packages/b4n1/boost
- Ir: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- Repositorio: https://github.com/B4N1-com/b4n1-boost
- Licencias: https://b4n1.com/licensing o `b4n1@b4n1.com`
- Registro de cambios: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 Licencia

**Licencia de fuente comercial 1.1 (`BUSL-1.1`)** — tenga en cuenta que este *no* es el ID de SPDX `BSL-1.1`, que denota el Boost Software License.

- **Gratis** para desarrollo, evaluación, pruebas, proyectos personales y nuevas empresas con ingresos anuales de **$100 000 USD**.
- **Licencia comercial** requerida para organizaciones >= **$100K USD**, agencias gubernamentales y licitaciones públicas.
- Después de **Fecha de cambio** (4 años) → **Licencia Apache 2.0**.

Ver [LICENCIA](LICENSE) para texto completo.

---

_b4n1-boost: El acelerador políglota. Un núcleo nativo, siete SDK. JSON entre 3 y 5 veces más rápido. Compresión ~21 veces más rápida que el nivel 4 de gzip. Middleware transparente. Construido con ❤️ por B4N1._
