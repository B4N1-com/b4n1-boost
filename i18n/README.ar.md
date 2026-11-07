<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

# 📦 b4n1-boost

**المسرع متعدد اللغات. نواة أصلية واحدة وسبعة حزم SDK — Python وNode.js وRuby وPHP وJava و.NET وGo. JSON أسرع بمعدل 3 إلى 5 مرات، والضغط أسرع بمعدل 21 مرة تقريبًا (يتم قياسه)، وذاكرة التخزين المؤقت للاستجابة، ومرشح الازدهار، وقاطع الدائرة في كل مجموعة أدوات تطوير البرامج (SDK) الأساسية.**

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

> 📚 **الدليل الكامل (التثبيت، البرامج الوسيطة، المسرعات، الأداء):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 دعم المنصة

| منصة | أبنية |
|----------|---------------|
| **لينكس** | x86_64, aarch64 |
| **ماك** | x86_64,arm64 (أبل سيليكون) |
| **ويندوز** | x86_64 |

**الثنائيات المترجمة مسبقًا لكل نظام أساسي وكل لغة** — لا يلزم وجود مترجم، فهو يعمل خارج الصندوق.

---

## 📦 التثبيت — 7 سجلات، 1 مركزي

| التسجيل | لغة | طَرد | يأمر |
|----------|----------|---------|---------|
| **بايبي** | بايثون 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **نبم** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| ** نوجيت ** | صافي / سي # | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| ** مخضرم ** | جافا / كوتلين | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.7'` |
| **جواهر روبي** | روبي / رف | `b4n1-boost` | `gem install b4n1-boost` |
| **باكاجيست** | بي إتش بي / لارافيل | `b4n1/boost` | `composer require b4n1/boost` |
| **يذهب** | الذهاب 1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

جميع الحزم السبعة تشحن ** نفس النواة الأصلية ** (مترجمة مسبقًا، بدون مترجم
ضروري). بالإضافة إلى ذلك، تحتوي عجلة Python على مجموعة البرامج الوسيطة HTTP و
تقوم حزم Ruby/PHP/Go بتجميع lib الأصلي لنظامها الأساسي.

---

**اللغات:** [العربية](i18n/README.ar.md) · [الألمانية](i18n/README.de.md) · [الإسبانية](i18n/README.es.md) · [الفرنسية](i18n/README.fr.md) · [الهندية](i18n/README.hi.md) · [الإيطالية](i18n/README.it.md) · [الصفحة الرئيسية](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [البرتغالية (BR)](i18n/README.pt-BR.md) · [الروسية](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 ما يقدمه لك كل SDK

| القدرة | بايثون | Node.js | جافا / كوتلين | .شبكة | روبي | PHP | يذهب |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ذاكرة التخزين المؤقت للاستجابة (LRU + TTL) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| مرشح بلوم | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| قاطع الدائرة | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ضغط Gzip / Zstd | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| تصغير HTML | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| التحقق من صحة JSON | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| برامج HTTP الوسيطة (الضغط، ETag، CORS، حد المعدل، رؤوس الأمان، إلغاء الضغط، فحص الصحة) | ✅ | يعبر | — | أسب.نت | رف | لارافيل | — |
| ZSTD تخفيف الضغط | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| مهام الخلفية (لا يوجد Redis ولا الكرفس) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| ضغط بروتلي | ✅ | — | — | — | — | — | — |
| التصغير (CSS / JS) + HTML → Markdown | ✅ | — | — | — | — | — | — |
| التحقق من صحة JWT | ✅ | — | — | — | — | — | — |
| محرك JSON أسرع بـ 3.1-5.0x | ✅ | — | — | — | — | — | — |
| مسرعات Django ORM/DRF/SQLAlchemy | ✅ | — | — | — | — | — | — |

الضغط + التصغير + JSON core هو ** نفس المكالمة الأصلية على الإطلاق
سبع لغات** (واحدة من C-ABI، تم اختبارها بموجب عقد لكل لغة). ذاكرة التخزين المؤقت، ازهر
يتم اختبار الفلتر وقاطع الدائرة بشكل متعاقد عليه في Python وNode.js وJava و
.شبكة؛ توجد أغلفة Ruby وPHP وGo الخاصة بهم على خريطة الطريق.

---

## ⚡ نظرة سريعة على الأداء

| عنصر | متري | مقابل ستدليب |
|---|---|---|
| ** مقالب JSON ** (المحرك الأصلي) | 3.1-5.0x أسرع من stdlib `json` | سطح بايثون، مقاس 2026-10-21 |
| **Gzip** (أصلي) | ~1.0x مقابل مستوى stdlib gzip 6 | حمولات 1 ميجا بايت (gzip الأصلي هو المستوى 4) |
| **Zstd** (أصلي) | ~21x أسرع (المستوى 1 مقابل gzip 4) | حمولات 1 ميجابايت |
| ** بروتلي ** (محلي) | أفضل نسبة، أبطأ بحوالي 1.6 مرة من gzip | حمولات 1 ميجابايت |
| ** تسلسل DRF ** | لم يتم قياسه بعد | مجموعة الاستعلام → JSON |
| ** جانغو أورم ** | نسخة بوستجرس | إدراج بالجملة الأصلي |
| **حجم العجلة** | ~1.4 ميجابايت | أصلي، لا حاجة إلى مترجم |
| ** لا يوجد GIL جاهز ** | بايثون 3.13+ | دعم الخيوط الحرة |
| **الاختبارات** | 1253 مرور | Rust 346 (lib + bin) + Python 907، بالإضافة إلى مجموعة عقود SDK ×7 |

---

## 🚀 بداية سريعة

### جربه بأمر واحد (بدون اتصال، بدون إعداد)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` يدير المعيار الخاص بالمحرك حيث يتم تنفيذه و
يطبع ما تم قياسه للتو - لا توجد أرقام مخزنة، ولا إسقاطات، ولا شبكة.
تتم طباعة المضاعفات التاريخية لكل إطار كتقديرات، مصنفة
كما.

هل تفضل ملفًا يمكنك تسليمه؟ `bash scripts/build-demo-bundle.sh` (أو
`bash cli.sh boost bundle` من جذر الإطار) يبني قائمة بذاتها
الرمز البريدي مع الملعب، والدليل الكامل، والثنائي وأمر واحد
`demo.sh`.

### النواة المشتركة (Python، Node.js، Java، .NET)

ذاكرة التخزين المؤقت للاستجابة، ومرشح الازدهار، وقاطع الدائرة - نفس البدائيات الأصلية الموجودة
هذه SDK الأربعة. تم اختبار العقد في جميع الأربعة.

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

**.شبكة**
```csharp
using B4N1.Boost;

using var cache = new NativeResponseCache(1024);
cache.Set("user:1", Encoding.UTF8.GetBytes("{\"id\":1}"), 200, 60);

using var seen = new NativeBloomFilter(100_000, 0.01);
bool firstTime = !seen.CheckAndSet("already-processed");

var breaker = new NativeCircuitBreaker(5, 2, 30);
if (!breaker.Allows) return Fallback();
```

**جافا/كوتلين**
```java
import com.b4n1.boost.NativeResponseCache;

try (NativeResponseCache cache = new NativeResponseCache(8)) {
    cache.set("user:1", "{\"id\":1}".getBytes(StandardCharsets.UTF_8), 200, 60_000);
}
```

**بايثون**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### محرك الضغط

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.شبكة**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**جافا/كوتلين**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**روبي**
```ruby
require 'boost'

zstd = B4N1::Boost.compress_zstd(payload)
min  = B4N1::Boost.minify_html(html)
ok   = B4N1::Boost.json_valid?(body)
```

** PHP **
```php
use B4N1\Boost;

$zstd = Boost::compressZstd($payload);
$min  = Boost::minifyHtml($html);
$ok   = Boost::isJsonValid($body);
```

**يذهب**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### البرمجيات الوسيطة Express / ASP.NET

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 الاستخدام الكامل لكل لغة موجود في **[الدليل](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 مجموعة بايثون (البرامج الوسيطة + المسرعات)

حزمة Python هي الحزمة الأكثر اكتمالاً: كل ما سبق، بالإضافة إلى HTTP
مجموعة البرمجيات الوسيطة ومسرعات الإطار.

```bash
pip install b4n1-boost
```

العجلات الأصلية المترجمة مسبقًا لنظام التشغيل Linux (x86_64 + aarch64)، وmacOS (x86_64 + Apple Silicon)، وWindows (x86_64). لا يوجد مترجم المطلوبة.

**إصدارات بايثون المدعومة:** 3.10، 3.11، 3.12، 3.13

### جانجو
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### واجهة برمجة التطبيقات السريعة
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

###قارورة
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### الكشف التلقائي
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### تثبيت جميع البرامج الوسيطة في سطر واحد
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 المميزات

### تسلسل JSON (3.1-5.0x أسرع من stdlib `json`)
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

### الضغط (أسرع بحوالي 21 مرة من مستوى gzip 4، بدون GIL)
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

### البرامج الوسيطة المدركة لنوع المحتوى
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 التخزين المؤقت
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### تحديد المعدل
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### رؤوس الأمان
```python
from b4n1_boost.middleware import SecurityHeadersMiddleware
app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
# Adds: X-Content-Type-Options, X-Frame-Options, HSTS, X-XSS-Protection, etc.
```

### كورس
```python
from b4n1_boost.middleware import CORSMiddleware
app.wsgi_app = CORSMiddleware(app.wsgi_app, allow_origins=["https://example.com"])
```

### فحص الصحة
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### طبقة ذاكرة التخزين المؤقت
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### مسرع جانغو ORM
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### مسرع DRF التسلسلي
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

### التحقق من صحة JWT
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### تصغير HTML/CSS/JS
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → تخفيض السعر (الوكيل)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### القياس عن بعد
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

### عامل الخلفية (صفر جيل)
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

## 🔍 الحالة والتشخيص

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

## 🔗روابط

- موقع إلكتروني: https://b4n1.com
- باي بي آي: https://pypi.org/project/b4n1-boost
- نبم: https://www.npmjs.com/package/b4n1-boost
- نوجيت: https://www.nuget.org/packages/B4N1.Boost
- مافن سنترال: https://central.sonatype.com/artifact/com.b4n1/boost
- جواهر روبي: https://rubygems.org/gems/b4n1-boost
- التعبئة والتغليف: https://packagist.org/packages/b4n1/boost
- يذهب: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- المستودع: https://github.com/B4N1-com/b4n1-boost
- الترخيص: https://b4n1.com/licensing أو `b4n1@b4n1.com`
- سجل التغيير: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 الترخيص

** ترخيص مصدر الأعمال 1.1 (`BUSL-1.1`)** — لاحظ أن هذا *ليس* معرف SPDX `BSL-1.1`، والذي يدل على Boost Software License.

- **مجانًا** للتطوير والتقييم والاختبار والمشاريع الشخصية والشركات الناشئة التي تقل عائداتها السنوية عن **100 ألف دولار أمريكي**.
- **الترخيص التجاري** مطلوب للمؤسسات >= **100 ألف دولار أمريكي** والوكالات الحكومية والمزايدات العامة.
- بعد **تاريخ التغيير** (4 سنوات) → **ترخيص Apache 2.0**.

انظر [الترخيص](LICENSE) للنص الكامل.

---

_b4n1-boost: المسرع متعدد اللغات. نواة أصلية واحدة وسبعة أدوات تطوير البرامج (SDKs). JSON 3-5x أسرع. الضغط أسرع بحوالي 21 مرة من مستوى gzip 4. برنامج وسيط شفاف. تم البناء باستخدام ❤️ بواسطة B4N1._
