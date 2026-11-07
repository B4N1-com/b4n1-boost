<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

#📦 b4n1-boost

**O acelerador poliglota. Um núcleo nativo, sete SDKs — Python, Node.js, Ruby, PHP, Java, .NET e Go. JSON 3 a 5x mais rápido, compactação ~21x mais rápida (medida), cache de resposta, filtro Bloom e disjuntor em todos os SDKs principais.**

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

> 📚 **Manual completo (instalação, middleware, aceleradores, desempenho):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 Suporte à plataforma

| Plataforma | Arquiteturas |
|----------|---------------|
| **Linux** | x86_64, aarch64 |
| **macOS** | x86_64, arm64 (silício da Apple) |
| **Windows** | x86_64 |

**Binários pré-compilados para todas as plataformas e linguagens** — não é necessário nenhum compilador, funciona imediatamente.

---

## 📦 Instalação — 7 registros, 1 núcleo

| Registro | Linguagem | Pacote | Comando |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET/C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **Maven** | Java/Kotlin | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.6'` |
| **RubyGems** | Rubi / Rack | `b4n1-boost` | `gem install b4n1-boost` |
| **Embalador** | PHP/Laravel | `b4n1/boost` | `composer require b4n1/boost` |
| **Ir** | Vá para 1,23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

Todos os sete pacotes enviam o **mesmo núcleo nativo** (pré-compilado, sem compilador
necessário). A roda Python também inclui o conjunto de middleware HTTP e
os pacotes Ruby/PHP/Go agrupam a biblioteca nativa para sua plataforma.

---

**Idiomas:** [العربية](i18n/README.ar.md) · [Alemão](i18n/README.de.md) · [Espanhol](i18n/README.es.md) · [Francês](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [Italiano](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Português (BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 O que cada SDK oferece

| Capacidade | Pitão | Node.js | Java/Kotlin | .LÍQUIDO | Rubi | PHP | Ir |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Cache de resposta (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Filtro de flor | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Disjuntor | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Compressão Gzip/Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Minificação de HTML | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Validação JSON | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Middleware HTTP (compactação, ETag, CORS, limite de taxa, cabeçalhos de segurança, descompactação, verificação de integridade) | ✅ | Expressar | — | ASP.NET | Prateleira | Laravel | — |
| Descompressão Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tarefas em segundo plano (sem Redis, sem Celery) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Compressão Brotli | ✅ | — | — | — | — | — | — |
| Minificação (CSS/JS) + HTML→Markdown | ✅ | — | — | — | — | — | — |
| Validação JWT | ✅ | — | — | — | — | — | — |
| Mecanismo JSON 3.1-5.0x mais rápido | ✅ | — | — | — | — | — | — |
| Aceleradores Django ORM / DRF / SQLAlchemy | ✅ | — | — | — | — | — | — |

A compactação + minificação + núcleo JSON é ** a mesma chamada nativa em todos
sete idiomas** (um C-ABI, testado em contrato por idioma). O cache, florescer
filtro e disjuntor são testados em contrato em Python, Node.js, Java e
.LÍQUIDO; seus wrappers Ruby, PHP e Go estão no roteiro.

---

## ⚡ Visão geral do desempenho

| Componente | Métrica | versus stdlib |
|---|---|---|
| **Despejos JSON** (mecanismo nativo) | 3,1-5,0x mais rápido que stdlib `json` | Superfície Python, medida em 21/10/2026 |
| **Gzip** (nativo) | ~ 1,0x vs stdlib gzip nível 6 | Cargas úteis de 1 MB (o gzip nativo é de nível 4) |
| **Zstd** (nativo) | ~21x mais rápido (nível 1 vs gzip 4) | Cargas úteis de 1 MB |
| **Brotli** (nativo) | Melhor proporção, ~ 1,6x MAIS LENTA que gzip | Cargas úteis de 1 MB |
| **Serializador DRF** | ainda não foi medido | conjunto de consultas → JSON |
| **Django ORM** | CÓPIA PostgreSQL | inserção em massa nativa |
| **Tamanho da roda** | ~ 1,4 MB | nativo, nenhum compilador necessário |
| **Não-GIL pronto** | Pitão 3.13+ | Suporte para threading grátis |
| **Testes** | 1253 passagem | Rust 346 (lib + bin) + Python 907, mais o conjunto de contratos SDK ×7 |

---

## 🚀 Início rápido

### Experimente em um comando (offline, sem configuração)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` executa o próprio benchmark do mecanismo onde é executado e
imprime o que acabou de medir - sem números armazenados, sem projeções, sem rede.
Os multiplicadores históricos por estrutura são impressos como estimativas, rotulados
Como tal.

Prefere um arquivo que você possa entregar? `bash scripts/build-demo-bundle.sh` (ou
`bash cli.sh boost bundle` da raiz da estrutura) constrói um sistema independente
ZIP com o pitch, o manual completo, o binário e um comando
`demo.sh`.

### O núcleo compartilhado (Python, Node.js, Java, .NET)

Cache de resposta, filtro Bloom e disjuntor - os mesmos primitivos nativos em
esses quatro SDKs. Testado por contrato em todos os quatro.

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

**.LÍQUIDO**
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

**Píton**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### Mecanismo de compressão

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.LÍQUIDO**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Java/Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**Rubi**
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

### Middleware Express/ASP.NET

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 O uso completo para todos os idiomas está no **[manual](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Suíte Python (middleware + aceleradores)

O pacote Python é o mais completo: tudo acima, mais o HTTP
suíte de middleware e aceleradores de framework.

```bash
pip install b4n1-boost
```

Rodas nativas pré-compiladas para Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) e Windows (x86_64). Não é necessário compilador.

**Versões Python suportadas:** 3.10, 3.11, 3.12, 3.13

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

### Frasco
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Detecção automática
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### Instalação em uma linha de todo o middleware
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 Recursos

### Serialização JSON (3,1-5,0x mais rápida que stdlib `json`)
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

### Compressão (~21x mais rápida que gzip nível 4, sem GIL)
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

### Middleware com reconhecimento de tipo de conteúdo
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / Cache 304
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Limitação de taxa
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### Cabeçalhos de segurança
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

### Exame de saúde
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### Camada de Cache
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Acelerador Django ORM
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### Acelerador serializador DRF
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

### Validação JWT
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### Minificação de HTML/CSS/JS
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → Markdown (Agente)
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

### Trabalhador em segundo plano (zero-GIL)
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

## 🔍 Status e diagnóstico

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

## 🔗 Links

- Site: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- npm: https://www.npmjs.com/package/b4n1-boost
- NuGet: https://www.nuget.org/packages/B4N1.Boost
-Maven Central: https://central.sonatype.com/artifact/com.b4n1/boost
- RubyGems: https://rubygems.org/gems/b4n1-boost
- Embalador: https://packagist.org/packages/b4n1/boost
- Ir: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- Repositório: https://github.com/B4N1-com/b4n1-boost
- Licenciamento: https://b4n1.com/licensing ou `b4n1@b4n1.com`
- Registro de alterações: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 Licença

**Licença de fonte comercial 1.1 (`BUSL-1.1`)** — observe que este *não* é o ID SPDX `BSL-1.1`, que denota o Boost Software License.

- **Gratuito** para desenvolvimento, avaliação, testes, projetos pessoais e startups com receita anual de **US$ 100 mil**.
- **Licença comercial** necessária para organizações >= **US$ 100 mil**, agências governamentais e licitações públicas.
- Após **Data de alteração** (4 anos) → **Licença Apache 2.0**.

Consulte [LICENÇA](LICENSE) para texto completo.

---

_b4n1-boost: O acelerador poliglota. Um núcleo nativo, sete SDKs. JSON 3 a 5x mais rápido. Compressão ~21x mais rápida que o nível 4 do gzip. Middleware transparente. Construído com ❤️ por B4N1._
