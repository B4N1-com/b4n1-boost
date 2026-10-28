<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

# 📦 b4n1-boost

**다언어 가속기. 하나의 네이티브 코어, 7개의 SDK(Python, Node.js, Ruby, PHP, Java, .NET, Go). JSON은 3~5배 더 빠르며, 압축은 최대 21배 더 빠릅니다(측정). 모든 코어 SDK에는 응답 캐시, 블룸 필터 및 회로 차단기가 있습니다.**

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

> 📚 **전체 매뉴얼(설치, 미들웨어, 가속기, 성능):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 플랫폼 지원

| 플랫폼 | 아키텍처 |
|----------|---------------|
| **리눅스** | x86_64, aarch64 |
| **맥OS** | x86_64, arm64(애플 실리콘) |
| **창** | x86_64 |

**모든 플랫폼과 모든 언어에 대해 사전 컴파일된 바이너리** — 컴파일러가 필요하지 않으며 즉시 작동합니다.

---

## 📦 설치 — 레지스트리 7개, 코어 1개

| 기재 | 언어 | 패키지 | 명령 |
|----------|----------|---------|---------|
| **PyPI** | 파이썬 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **누겟** | .NET/C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **메이븐** | 자바/코틀린 | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.3'` |
| **RubyGems** | 루비 / 랙 | `b4n1-boost` | `gem install b4n1-boost` |
| **패키지 담당자** | PHP/라라벨 | `b4n1/boost` | `composer require b4n1/boost` |
| **가다** | 1.23+로 이동 | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

7개 패키지 모두 **동일한 기본 코어**(사전 컴파일됨, 컴파일러 없음)를 제공합니다.
필요). Python 휠은 추가로 HTTP 미들웨어 제품군을 번들로 제공합니다.
Ruby/PHP/Go 패키지는 해당 플랫폼에 맞는 기본 lib를 번들로 제공합니다.

---

**언어:** [العربية](i18n/README.ar.md) · [독일어](i18n/README.de.md) · [스페인어](i18n/README.es.md) · [프랑스](i18n/README.fr.md) · [힌디어](i18n/README.hi.md) · [이탈리아노](i18n/README.it.md) · [일본어](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [포르투갈어(BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [중국어](i18n/README.zh-CN.md)

## 🧩 각 SDK가 제공하는 것

| 능력 | 파이썬 | Node.js | 자바/코틀린 | .그물 | 루비 | PHP | 가다 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 응답 캐시(LRU + TTL) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 블룸 필터 | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 회로 차단기 | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Gzip / Zstd 압축 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTML 축소 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| JSON 검증 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP 미들웨어(압축, ETag, CORS, 속도 제한, 보안 헤더, 압축 해제, 상태 확인) | ✅ | 표현하다 | — | ASP.NET | 고문 | 라라벨 | — |
| Zstd 감압 | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 백그라운드 작업(Redis 없음, Celery 없음) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Brotli 압축 | ✅ | — | — | — | — | — | — |
| 축소(CSS/JS) + HTML→마크다운 | ✅ | — | — | — | — | — | — |
| JWT 검증 | ✅ | — | — | — | — | — | — |
| JSON 엔진 3.1~5.0배 더 빠름 | ✅ | — | — | — | — | — | — |
| Django ORM / DRF / SQLAlchemy 가속기 | ✅ | — | — | — | — | — | — |

압축 + 축소 + JSON 코어는 **모두 동일한 기본 호출입니다.
7개 언어**(1개의 C-ABI, 언어별로 계약 테스트 완료). 캐시, 피어나다
필터 및 회로 차단기는 Python, Node.js, Java 및
.그물; Ruby, PHP 및 Go 래퍼가 로드맵에 있습니다.

---

## ⚡ 성능 한눈에 보기

| 요소 | 미터법 | 대 stdlib |
|---|---|---|
| **JSON 덤프**(네이티브 엔진) | stdlib보다 3.1-5.0배 빠름 `json` | Python 표면, 2026-10-21 측정 |
| **Gzip**(네이티브) | ~1.0x 대 stdlib gzip 레벨 6 | 1MB 페이로드(기본 gzip은 레벨 4) |
| **Zstd**(기본) | ~21배 더 빠름(레벨 1 대 gzip 4) | 1MB 페이로드 |
| **브로틀리**(네이티브) | 최고의 비율, gzip보다 ~1.6배 느림 | 1MB 페이로드 |
| **DRF 시리얼라이저** | 아직 측정되지 않았습니다 | 쿼리셋 → JSON |
| **장고 ORM** | PostgreSQL 사본 | 대량 삽입 네이티브 |
| **휠 크기** | ~1.4MB | 네이티브, 컴파일러가 필요하지 않음 |
| **GIL 없음 준비** | 파이썬 3.13+ | 프리스레딩 지원 |
| **테스트** | 1253 통과 | Rust 346(lib + bin) + Python 907 및 SDK 계약 제품군 ×7 |

---

## 🚀 빠른 시작

### 하나의 명령으로 사용해 보세요(오프라인, 설정 없음)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` 엔진이 실행되는 자체 벤치마크를 실행하고
방금 측정한 내용을 인쇄합니다. 저장된 수치도, 예측도, 네트워크도 없습니다.
과거 프레임워크별 승수는 추정치로 인쇄되며 라벨이 붙습니다.
그 자체로.

넘겨줄 수 있는 파일을 선호하시나요? `bash scripts/build-demo-bundle.sh` (또는
`bash cli.sh boost bundle` 프레임워크 루트에서) 독립형을 구축합니다.
피치, 전체 매뉴얼, 바이너리 및 단일 명령이 포함된 ZIP
`demo.sh`.

### 공유 코어(Python, Node.js, Java, .NET)

응답 캐시, 블룸 필터 및 회로 차단기 — 동일한 기본 기본 요소
이 4개의 SDK입니다. 네 가지 모두에서 계약 테스트를 거쳤습니다.

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

**.그물**
```csharp
using B4N1.Boost;

using var cache = new NativeResponseCache(1024);
cache.Set("user:1", Encoding.UTF8.GetBytes("{\"id\":1}"), 200, 60);

using var seen = new NativeBloomFilter(100_000, 0.01);
bool firstTime = !seen.CheckAndSet("already-processed");

var breaker = new NativeCircuitBreaker(5, 2, 30);
if (!breaker.Allows) return Fallback();
```

**자바/코틀린**
```java
import com.b4n1.boost.NativeResponseCache;

try (NativeResponseCache cache = new NativeResponseCache(8)) {
    cache.set("user:1", "{\"id\":1}".getBytes(StandardCharsets.UTF_8), 200, 60_000);
}
```

**파이썬**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### 압축 엔진

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**.그물**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**자바/코틀린**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**루비**
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

**가다**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Express/ASP.NET 미들웨어

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 모든 언어에 대한 전체 사용법은 **[설명서](https://b4n1-com.github.io/b4n1-boost/)**.

---

## 🐍 Python 제품군(미들웨어 + 가속기)

Python 패키지는 위의 모든 항목과 HTTP를 포함한 가장 완벽한 패키지입니다.
미들웨어 제품군 및 프레임워크 가속기.

```bash
pip install b4n1-boost
```

Linux(x86_64 + aarch64), macOS(x86_64 + Apple Silicon) 및 Windows(x86_64)용으로 사전 컴파일된 기본 휠입니다. 컴파일러가 필요하지 않습니다.

**지원되는 Python 버전:** 3.10, 3.11, 3.12, 3.13

### 장고
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

### 플라스크
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### 자동 감지
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### 모든 미들웨어를 한 줄로 설치
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 기능

### JSON 직렬화(stdlib보다 3.1-5.0배 빠름) `json`)
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

### 압축(gzip 레벨 4보다 21배 빠름, GIL 없음)
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

### 콘텐츠 유형 인식 미들웨어
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 캐싱
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### 속도 제한
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### 보안 헤더
```python
from b4n1_boost.middleware import SecurityHeadersMiddleware
app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
# Adds: X-Content-Type-Options, X-Frame-Options, HSTS, X-XSS-Protection, etc.
```

### 코르스
```python
from b4n1_boost.middleware import CORSMiddleware
app.wsgi_app = CORSMiddleware(app.wsgi_app, allow_origins=["https://example.com"])
```

### 건강검진
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### 캐시 레이어
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Django ORM 가속기
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### DRF 직렬 변환기 가속기
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

### JWT 검증
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### HTML/CSS/JS 축소
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → 마크다운(에이전트)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### 원격 측정
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

### 백그라운드 작업자(zero-GIL)
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

## 🔍 상태 및 진단

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.4.3', 'native_extension': True, 'features': [...]}
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

## 🔗 링크

- 웹사이트: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- npm: https://www.npmjs.com/package/b4n1-boost
- 누겟: https://www.nuget.org/packages/B4N1.Boost
- 메이븐 센트럴: https://central.sonatype.com/artifact/com.b4n1/boost
- RubyGems: https://rubygems.org/gems/b4n1-boost
- 포장 담당자: https://packagist.org/packages/b4n1/boost
- 가다: https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- 저장소: https://github.com/B4N1-com/b4n1-boost
- 라이센스: https://b4n1.com/licensing 또는 `b4n1@b4n1.com`
- 변경 내역: [CHANGELOG.md](CHANGELOG.md)

---

## 📄 라이센스

**비즈니스 소스 라이선스 1.1(`BUSL-1.1`)** — 이것은 SPDX ID가 *아닙니다*. `BSL-1.1`, 이는 다음을 나타냅니다. Boost Software License.

- 연간 수익 **$100,000** 미만인 개발, 평가, 테스트, 개인 프로젝트 및 스타트업의 경우 **무료**입니다.
- **$100K USD** 이상의 조직, 정부 기관 및 공개 입찰에는 **상업 라이센스**가 필요합니다.
- **변경일**(4년) 이후 → **Apache License 2.0**.

[라이센스](LICENSE) 전체 텍스트의 경우.

---

_b4n1-boost: 다언어 가속기. 하나의 기본 코어, 7개의 SDK. JSON이 3~5배 더 빠릅니다. 압축은 gzip 레벨 4보다 최대 21배 빠릅니다. 미들웨어는 투명합니다. ❤️으로 제작됨 B4N1._
