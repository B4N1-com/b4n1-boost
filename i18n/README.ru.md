<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

# 📦 b4n1-boost

**Ускоритель-полиглот. Одно собственное ядро, семь SDK — Python, Node.js, Ruby, PHP, Java, .NET и Go. JSON в 3–5 раз быстрее, сжатие примерно в 21 раз быстрее (по измерениям), кэш ответов, фильтр Блума и автоматический выключатель в каждом ядре SDK.**

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

> 📚 **Полное руководство (установка, промежуточное ПО, ускорители, производительность):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 Поддержка платформы

| Платформа | Архитектуры |
|----------|---------------|
| **Линукс** | x86_64, аарх64 |
| **macOS** | x86_64, Arm64 (Apple Silicon) |
| **Окна** | x86_64 |

**Предварительно скомпилированные двоичные файлы для каждой платформы и каждого языка** — компилятор не требуется, работает «из коробки».

---

## 📦 Установка — 7 реестров, 1 ядро

| Реестр | Язык | Упаковка | Команда |
|----------|----------|---------|---------|
| **ПиПИ** | Питон 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **нпм** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **НюГет** | .NET/С# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **Мавен** | Ява/Котлин | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.6'` |
| **РубиДжемс** | Рубин / Стойка | `b4n1-boost` | `gem install b4n1-boost` |
| **Упаковщик** | PHP/Ларавель | `b4n1/boost` | `composer require b4n1/boost` |
| **Идти** | Перейти 1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

Все семь пакетов содержат **одно и то же собственное ядро** (предварительно скомпилированное, без компилятора).
нужный). Колесо Python дополнительно включает в себя пакет промежуточного программного обеспечения HTTP и
Пакеты Ruby/PHP/Go включают в себя собственную библиотеку для своей платформы.

---

**Языки:** [العربية](i18n/README.ar.md) · [Немецкий](i18n/README.de.md) · [Испанский](i18n/README.es.md) · [Французский](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [итальянский](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Португальский (BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 Что дает вам каждый SDK

| Возможность | Питон | Node.js | Ява/Котлин | .СЕТЬ | Руби | PHP | Идти |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Кэш ответов (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Фильтр Блума | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Автоматический выключатель | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Сжатие Gzip/Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Минимизация HTML | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Проверка JSON | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Промежуточное ПО HTTP (сжатие, ETag, CORS, ограничение скорости, заголовки безопасности, распаковка, проверка работоспособности) | ✅ | Выражать | — | АСП.НЕТ | Стойка | Ларавел | — |
| Zstd декомпрессия | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Фоновые задачи (без Redis, без Celery) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Компрессия Бротли | ✅ | — | — | — | — | — | — |
| Минимизация (CSS/JS) + HTML→Markdown | ✅ | — | — | — | — | — | — |
| JWT-проверка | ✅ | — | — | — | — | — | — |
| JSON-движок в 3,1–5,0 раза быстрее | ✅ | — | — | — | — | — | — |
| Ускорители Django ORM/DRF/SQLAlchemy | ✅ | — | — | — | — | — | — |

Ядро сжатия + минификации + JSON — это **один и тот же собственный вызов во всех
семь языков** (по одному C-ABI, проверенному по контракту для каждого языка). Кэш, цветение
фильтр и автоматический выключатель протестированы по контракту на Python, Node.js, Java и
.СЕТЬ; их оболочки Ruby, PHP и Go находятся в планах.

---

## ⚡ Обзор производительности

| Компонент | Метрика | против стандартной библиотеки |
|---|---|---|
| **Дампы JSON** (собственный движок) | В 3,1-5,0 раз быстрее, чем stdlib `json` | Поверхность Python, измерено 21 октября 2026 г. |
| **Gzip** (родной) | ~1.0x против stdlib gzip уровня 6 | Полезная нагрузка 1 МБ (родной gzip — уровень 4) |
| **Зстд** (родной) | ~ в 21 раз быстрее (уровень 1 по сравнению с gzip 4) | Полезная нагрузка 1 МБ |
| **Бротли** (родной) | Лучшее соотношение, примерно в 1,6 раза медленнее, чем gzip. | Полезная нагрузка 1 МБ |
| **Сериализатор DRF** | еще не измерен | набор запросов → JSON |
| **Джанго ОРМ** | PostgreSQL КОПИЯ | массовая вставка в исходном виде |
| **Размер колес** | ~1,4 МБ | родной, компилятор не требуется |
| **Готов без GIL** | Питон 3.13+ | Поддержка свободной потоковой обработки |
| **Тесты** | 1253 прохождения | Rust 346 (lib + bin) + Python 907, плюс пакет контрактов SDK ×7 |

---

## 🚀 Быстрый старт

### Попробуйте одной командой (офлайн, без настройки)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` запускает собственный тест движка, где он выполняется и
печатает то, что только что измерил — без сохраненных цифр, прогнозов и сети.
Исторические множители для каждой платформы печатаются как оценки, помеченные как
как таковой.

Предпочитаете файл, который можно передать? `bash scripts/build-demo-bundle.sh` (или
`bash cli.sh boost bundle` из корня фреймворка) создает автономный
ZIP с питчем, полное руководство, бинарник и однокомандный файл
`demo.sh`.

### Общее ядро ​​(Python, Node.js, Java, .NET)

Кэш ответов, фильтр Блума и автоматический выключатель — одни и те же нативные примитивы в
эти четыре SDK. Проверено по контракту во всех четырех.

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

**.СЕТЬ**
```csharp
using B4N1.Boost;

using var cache = new NativeResponseCache(1024);
cache.Set("user:1", Encoding.UTF8.GetBytes("{\"id\":1}"), 200, 60);

using var seen = new NativeBloomFilter(100_000, 0.01);
bool firstTime = !seen.CheckAndSet("already-processed");

var breaker = new NativeCircuitBreaker(5, 2, 30);
if (!breaker.Allows) return Fallback();
```

**Ява/Котлин**
```java
import com.b4n1.boost.NativeResponseCache;

try (NativeResponseCache cache = new NativeResponseCache(8)) {
    cache.set("user:1", "{\"id\":1}".getBytes(StandardCharsets.UTF_8), 200, 60_000);
}
```

**Питон**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### Двигатель сжатия

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.СЕТЬ**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Ява/Котлин**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**Рубин**
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

**Идти**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Промежуточное программное обеспечение Express/ASP.NET

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 Полное использование каждого языка описано в **[руководстве](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Пакет Python (промежуточное ПО + ускорители)

Пакет Python является наиболее полным: все вышеперечисленное, плюс HTTP
пакет промежуточного программного обеспечения и ускорители фреймворка.

```bash
pip install b4n1-boost
```

Предварительно скомпилированные собственные диски для Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) и Windows (x86_64). Компилятор не требуется.

**Поддерживаемые версии Python:** 3.10, 3.11, 3.12, 3.13.

### Джанго
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### ФастAPI
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Колба
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Автоопределение
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### Установка всего промежуточного программного обеспечения в одну строку
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 Особенности

### Сериализация JSON (в 3,1–5,0 раза быстрее, чем в stdlib) `json`)
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

### Сжатие (~ в 21 раз быстрее, чем gzip уровня 4, без GIL)
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

### Промежуточное ПО с учетом типа контента
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304-кэширование
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Ограничение скорости
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### Заголовки безопасности
```python
from b4n1_boost.middleware import SecurityHeadersMiddleware
app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
# Adds: X-Content-Type-Options, X-Frame-Options, HSTS, X-XSS-Protection, etc.
```

### КОРС
```python
from b4n1_boost.middleware import CORSMiddleware
app.wsgi_app = CORSMiddleware(app.wsgi_app, allow_origins=["https://example.com"])
```

### Проверка здоровья
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### Уровень кэша
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Ускоритель ORM Django
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### Ускоритель сериализации DRF
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

### JWT-проверка
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### Минимизация HTML/CSS/JS
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → Markdown (агент)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### Телеметрия
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

### Фоновый рабочий (нулевой GIL)
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

## 🔍 Статус и диагностика

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

## 🔗 Ссылки

- Веб-сайт: https://b4n1.com
- ПиПИ: https://pypi.org/project/b4n1-boost
- НПМ: https://www.npmjs.com/package/b4n1-boost
- НуГет: https://www.nuget.org/packages/B4N1.Boost
- Центральный Maven: https://central.sonatype.com/artifact/com.b4n1/boost
- Рубиновые камни: https://rubygems.org/gems/b4n1-boost
- Упаковщик: https://packagist.org/packages/b4n1/boost
- Идти: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- Репозиторий: https://github.com/B4N1-com/b4n1-boost
- Лицензирование: https://b4n1.com/licensing или `b4n1@b4n1.com`
- Журнал изменений: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 Лицензия

**Лицензия Business Source 1.1 (`BUSL-1.1`)** — обратите внимание, что это *не* идентификатор SPDX `BSL-1.1`, что обозначает Boost Software License.

- **Бесплатно** для разработки, оценки, тестирования, личных проектов и стартапов с годовым доходом **100 тыс. долларов США**.
- **Коммерческая лицензия** требуется для организаций стоимостью >= **100 тыс. долларов США**, государственных учреждений и участников публичных торгов.
- После **Даты изменения** (4 года) → **Лицензия Apache 2.0**.

См. [ЛИЦЕНЗИЯ](LICENSE) для полного текста.

---

_b4n1-boost: Акселератор-полиглот. Одно собственное ядро, семь SDK. JSON в 3–5 раз быстрее. Сжатие примерно в 21 раз быстрее, чем при использовании gzip уровня 4. Промежуточное программное обеспечение прозрачно. Создано с ❤️ автором B4N1._
