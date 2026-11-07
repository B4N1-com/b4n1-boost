<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

# 📦 b4n1-boost

**पॉलीग्लॉट त्वरक। एक देशी कोर, सात एसडीके - पायथन, नोड.जेएस, रूबी, पीएचपी, जावा, .NET और गो। JSON 3-5x तेज़, कम्प्रेशन ~21x तेज़ (मापा गया), रिस्पॉन्स कैश, ब्लूम फ़िल्टर और प्रत्येक कोर SDK में सर्किट ब्रेकर।**

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

> 📚 **पूर्ण मैनुअल (इंस्टॉलेशन, मिडलवेयर, एक्सेलेरेटर, प्रदर्शन):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 प्लेटफार्म समर्थन

| प्लैटफ़ॉर्म | वास्तुकला |
|----------|---------------|
| **लिनक्स** | x86_64, आर्क64 |
| **मैक ओएस** | x86_64, आर्म64 (एप्पल सिलिकॉन) |
| **विंडोज़** | x86_64 |

**प्रत्येक प्लेटफ़ॉर्म और प्रत्येक भाषा के लिए पूर्व-संकलित बायनेरिज़** - किसी कंपाइलर की आवश्यकता नहीं है, बॉक्स से बाहर काम करता है।

---

## 📦 इंस्टालेशन - 7 रजिस्ट्रियां, 1 कोर

| रजिस्ट्री | भाषा | पैकेट | आज्ञा |
|----------|----------|---------|---------|
| **पीईपीआई** | पायथन 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **एनपीएम** | नोड.जे.एस | `b4n1-boost` | `npm install b4n1-boost` |
| **न्यूगेट** | .नेट/सी# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **मेवेन** | जावा/कोटलिन | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.6'` |
| **रूबीजेम्स** | रूबी/रैक | `b4n1-boost` | `gem install b4n1-boost` |
| **पैकेजिस्ट** | पीएचपी/लारवेल | `b4n1/boost` | `composer require b4n1/boost` |
| **जाना** | 1.23+ जाओ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

सभी सात पैकेज **समान मूल कोर** (पूर्व-संकलित, कोई कंपाइलर नहीं) शिप करते हैं
आवश्यकता है)। पायथन व्हील अतिरिक्त रूप से HTTP मिडलवेयर सुइट को बंडल करता है, और
रूबी/पीएचपी/गो पैकेज अपने प्लेटफॉर्म के लिए नेटिव लिब को बंडल करते हैं।

---

**भाषाएँ:** [العربية](i18n/README.ar.md) · [जर्मन](i18n/README.de.md) · [स्पेनॉल](i18n/README.es.md) · [फ्रांसीसी](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [इतालवी](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [पुर्तगाली (बीआर)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 प्रत्येक SDK आपको क्या देता है

| क्षमता | अजगर | नोड.जे.एस | जावा/कोटलिन | ।जाल | रूबी | पीएचपी | जाना |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| प्रतिक्रिया कैश (एलआरयू + टीटीएल) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ब्लूम फिल्टर | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| परिपथ वियोजक | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gzip/Zstd संपीड़न | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTML लघुकरण | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| JSON सत्यापन | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP मिडलवेयर (संपीड़न, ETag, CORS, दर सीमा, सुरक्षा हेडर, डीकंप्रेसन, स्वास्थ्य जांच) | ✅ | अभिव्यक्त करना | — | एएसपी.नेट | रैक | laravel | — |
| Zstd डीकंप्रेसन | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| पृष्ठभूमि कार्य (कोई रेडिस नहीं, कोई सेलेरी नहीं) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| ब्रॉटली संपीड़न | ✅ | — | — | — | — | — | — |
| लघुकरण (सीएसएस/जेएस) + HTML→मार्कडाउन | ✅ | — | — | — | — | — | — |
| जेडब्ल्यूटी सत्यापन | ✅ | — | — | — | — | — | — |
| JSON इंजन 3.1-5.0x तेज़ | ✅ | — | — | — | — | — | — |
| Django ORM / DRF / SQLAlchemy त्वरक | ✅ | — | — | — | — | — | — |

कम्प्रेशन + मिनिमिफिकेशन + JSON कोर **सभी में एक ही मूल कॉल है
सात भाषाएँ** (एक सी-एबीआई, प्रति भाषा अनुबंध-परीक्षणित)। कैश, ब्लूम
फ़िल्टर और सर्किट ब्रेकर का पायथन, नोड.जेएस, जावा और में अनुबंध-परीक्षण किया जाता है
।जाल; उनके रूबी, पीएचपी और गो रैपर रोडमैप पर हैं।

---

## ⚡प्रदर्शन एक नजर में

| अवयव | मीट्रिक | बनाम stdlib |
|---|---|---|
| **JSON डंप** (देशी इंजन) | stdlib से 3.1-5.0 गुना तेज `json` | पायथन सतह, 2026-10-21 मापी गई |
| **गज़िप** (मूल) | ~1.0x बनाम stdlib gzip स्तर 6 | 1एमबी पेलोड (देशी जीज़िप लेवल 4 है) |
| **Zstd** (मूल) | ~21x तेज़ (स्तर 1 बनाम जीज़िप 4) | 1एमबी पेलोड |
| **ब्रोटली** (मूल) | सर्वोत्तम अनुपात, gzip से ~1.6x धीमा | 1एमबी पेलोड |
| **डीआरएफ सीरियलाइज़र** | अभी तक मापा नहीं गया | क्वेरीसेट → JSON |
| **Django ORM** | पोस्टग्रेएसक्यूएल कॉपी | थोक में देशी डालें |
| **पहिये का आकार** | ~1.4एमबी | मूल, किसी संकलक की आवश्यकता नहीं |
| **नो-जीआईएल तैयार** | पायथन 3.13+ | फ्री-थ्रेडिंग समर्थन |
| **परीक्षण** | 1253 बीत रहा है | रस्ट 346 (लिब + बिन) + पायथन 907, साथ ही एसडीके अनुबंध सुइट ×7 |

---

## 🚀 त्वरित शुरुआत

### इसे एक कमांड में आज़माएं (ऑफ़लाइन, कोई सेटअप नहीं)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` इंजन का अपना बेंचमार्क चलाता है जहां इसे निष्पादित किया जाता है और
वही प्रिंट करता है जो उसने अभी मापा है - कोई संग्रहीत आंकड़े नहीं, कोई अनुमान नहीं, कोई नेटवर्क नहीं।
ऐतिहासिक प्रति-फ़्रेमवर्क मल्टीप्लायरों को अनुमान के रूप में मुद्रित किया जाता है, लेबल किया जाता है
इस प्रकार।

क्या आप ऐसी फ़ाइल पसंद करेंगे जिसे आप सौंप सकें? `bash scripts/build-demo-bundle.sh` (या
`bash cli.sh boost bundle` फ्रेमवर्क रूट से) एक स्व-निहित बनाता है
पिच के साथ ज़िप, पूर्ण मैनुअल, बाइनरी और एक-कमांड
`demo.sh`.

### साझा कोर (पायथन, नोड.जेएस, जावा, .NET)

रिस्पांस कैश, ब्लूम फिल्टर और सर्किट ब्रेकर - वही मूल आदिम
ये चार एसडीके. चारों में अनुबंध-परीक्षण किया गया।

**नोड.जेएस**
```javascript
const { ResponseCache, BloomFilter, CircuitBreaker } = require('b4n1-boost/core.js');

const cache = new ResponseCache(1024);                       // capacity
cache.set('user:1', JSON.stringify({ id: 1 }), 200, 60);    // key, body, status, ttl (s)

const seen = new BloomFilter(100_000, 0.01);                // expected items, fp rate
if (!seen.checkAndSet('already-processed')) { /* first time we see it */ }

const breaker = new CircuitBreaker(5, 2, 30);               // threshold, successes, timeout (s)
if (!breaker.allows()) return fallback();
```

**।जाल**
```csharp
using B4N1.Boost;

using var cache = new NativeResponseCache(1024);
cache.Set("user:1", Encoding.UTF8.GetBytes("{\"id\":1}"), 200, 60);

using var seen = new NativeBloomFilter(100_000, 0.01);
bool firstTime = !seen.CheckAndSet("already-processed");

var breaker = new NativeCircuitBreaker(5, 2, 30);
if (!breaker.Allows) return Fallback();
```

**जावा/कोटलिन**
```java
import com.b4n1.boost.NativeResponseCache;

try (NativeResponseCache cache = new NativeResponseCache(8)) {
    cache.set("user:1", "{\"id\":1}".getBytes(StandardCharsets.UTF_8), 200, 60_000);
}
```

**पायथन**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### संपीड़न इंजन

**नोड.जेएस**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**।जाल**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**जावा/कोटलिन**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**रूबी**
```ruby
require 'boost'

zstd = B4N1::Boost.compress_zstd(payload)
min  = B4N1::Boost.minify_html(html)
ok   = B4N1::Boost.json_valid?(body)
```

**पीएचपी**
```php
use B4N1\Boost;

$zstd = Boost::compressZstd($payload);
$min  = Boost::minifyHtml($html);
$ok   = Boost::isJsonValid($body);
```

**जाना**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### एक्सप्रेस/एएसपी.नेट मिडलवेयर

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 प्रत्येक भाषा का पूर्ण उपयोग **[मैनुअल में रहता है](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 पायथन सुइट (मिडलवेयर + एक्सेलेरेटर)

पायथन पैकेज सबसे पूर्ण है: उपरोक्त सभी चीजें, साथ ही HTTP
मिडलवेयर सुइट और फ्रेमवर्क एक्सेलेरेटर।

```bash
pip install b4n1-boost
```

Linux (x86_64 + aarch64), macOS (x86_64 + Apple सिलिकॉन), और Windows (x86_64) के लिए पूर्व-संकलित देशी पहिये। किसी कंपाइलर की आवश्यकता नहीं है.

**समर्थित पायथन संस्करण:** 3.10, 3.11, 3.12, 3.13

### जैंगो
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### फास्टएपीआई
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### कुप्पी
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### स्वत: पता लगाना
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### सभी मिडलवेयर को एक-पंक्ति में स्थापित करें
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 विशेषताएँ

### JSON क्रमांकन (stdlib से 3.1-5.0x तेज़ `json`)
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

### संपीड़न (जीज़िप स्तर 4 से ~21x तेज़, जीआईएल-मुक्त)
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

### कंटेंट-टाइप अवेयर मिडलवेयर
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ईटैग/304 कैशिंग
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### दर सीमित करना
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### सुरक्षा शीर्षलेख
```python
from b4n1_boost.middleware import SecurityHeadersMiddleware
app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
# Adds: X-Content-Type-Options, X-Frame-Options, HSTS, X-XSS-Protection, etc.
```

### कॉर्स
```python
from b4n1_boost.middleware import CORSMiddleware
app.wsgi_app = CORSMiddleware(app.wsgi_app, allow_origins=["https://example.com"])
```

### स्वास्थ्य जांच
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### कैश परत
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Django ORM त्वरक
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### डीआरएफ सीरियलाइज़र एक्सेलेरेटर
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

### जेडब्ल्यूटी सत्यापन
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### HTML/CSS/JS न्यूनतमकरण
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → मार्कडाउन (एजेंटिक)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### टेलीमेट्री
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

### पृष्ठभूमि कार्यकर्ता (शून्य-जीआईएल)
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

## 🔍 स्थिति एवं निदान

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

## 🔗लिंक

- वेबसाइट: https://b4n1.com
- पीईपीआई: https://pypi.org/project/b4n1-boost
- एनपीएम: https://www.npmjs.com/package/b4n1-boost
- नुगेट: https://www.nuget.org/packages/B4N1.Boost
- मावेन सेंट्रल: https://central.sonatype.com/artifact/com.b4n1/boost
- रूबीजेम्स: https://rubygems.org/gems/b4n1-boost
- पैकेजिस्ट: https://packagist.org/packages/b4n1/boost
- जाना: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- भंडार: https://github.com/B4N1-com/b4n1-boost
- लाइसेंसिंग: https://b4n1.com/licensing या `b4n1@b4n1.com`
- चेंजलॉग: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 लाइसेंस

**बिजनेस सोर्स लाइसेंस 1.1 (`BUSL-1.1`)** — ध्यान दें यह SPDX आईडी *नहीं* है `BSL-1.1`, जो दर्शाता है Boost Software License.

- **$100K USD** वार्षिक राजस्व के तहत विकास, मूल्यांकन, परीक्षण, व्यक्तिगत परियोजनाओं और स्टार्टअप के लिए **निःशुल्क**।
- **वाणिज्यिक लाइसेंस** संगठनों के लिए आवश्यक है >= **$100K USD**, सरकारी एजेंसियां, और सार्वजनिक बोली।
- **तिथि परिवर्तन** के बाद (4 वर्ष) → **अपाचे लाइसेंस 2.0**।

देखें [लाइसेंस](LICENSE) पूर्ण पाठ के लिए.

---

_b4n1-boost: बहुभाषी त्वरक. एक देशी कोर, सात एसडीके। JSON 3-5x तेज़। जीज़िप स्तर 4 से संपीड़न ~21x तेज़। मिडलवेयर पारदर्शी। ❤️ द्वारा निर्मित B4N1._
