<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

#📦 b4n1-boost

**多语言加速器。一个本机核心，七个 SDK — Python、Node.js、Ruby、PHP、Java、.NET 和 Go。 JSON 速度快 3-5 倍，压缩速度快约 21 倍（测量），每个核心 SDK 中都有响应缓存、布隆过滤器和断路器。**

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

> 📚 **完整手册（安装、中间件、加速器、性能）：**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 平台支持

| 平台 | 架构 |
|----------|---------------|
| **Linux** | x86_64、aarch64 |
| **macOS** | x86_64、arm64（苹果芯片） |
| **视窗** | x86_64 |

**针对每个平台和每种语言的预编译二进制文件** - 无需编译器，开箱即用。

---

## 📦 安装 — 7 个注册表，1 个核心

| 登记处 | 语言 | 包裹 | 命令 |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET / C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **马文** | Java / 科特林 | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.5'` |
| **红宝石** | 红宝石/机架 | `b4n1-boost` | `gem install b4n1-boost` |
| **包装师** | PHP / Laravel | `b4n1/boost` | `composer require b4n1/boost` |
| **去** | 去1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

所有七个软件包都提供**相同的本机核心**（预编译，无编译器
需要）。 Python 轮还捆绑了 HTTP 中间件套件，并且
Ruby/PHP/Go 包捆绑了其平台的本机库。

---

**语言：** [阿拉伯语]](i18n/README.ar.md) · [德语](i18n/README.de.md) · [西班牙语](i18n/README.es.md) · [法语](i18n/README.fr.md) · [हिन्दी](i18n/README.hi.md) · [意大利语](i18n/README.it.md) · [日本语](i18n/README.ja.md) · [한국어]](i18n/README.ko.md) · [葡萄牙语（巴西）](i18n/README.pt-BR.md) · [ 俄罗斯 ]](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 每个 SDK 为您提供什么

| 能力 | Python | Node.js | Java / 科特林 | 。网 | 红宝石 | PHP | 去 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 响应缓存（LRU + TTL） | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 布隆过滤器 | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 断路器 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gzip / Zstd 压缩 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTML 缩小 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| JSON验证 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP中间件（压缩、ETag、CORS、速率限制、安全标头、解压、健康检查） | ✅ | 表达 | — | 网络平台 | 架子 | 拉维尔 | — |
| Zstd减压 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 后台任务（没有 Redis、没有 Celery） | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Brotli压缩 | ✅ | — | — | — | — | — | — |
| 缩小（CSS / JS）+ HTML→Markdown | ✅ | — | — | — | — | — | — |
| JWT 验证 | ✅ | — | — | — | — | — | — |
| JSON 引擎速度提高 3.1-5.0 倍 | ✅ | — | — | — | — | — | — |
| Django ORM / DRF / SQLAlchemy 加速器 | ✅ | — | — | — | — | — | — |

压缩+缩小+JSON核心是**相同的本机调用
七种语言**（一种 C-ABI，每种语言经过合同测试）。缓存，绽放
过滤器和断路器在 Python、Node.js、Java 和
。网;他们的 Ruby、PHP 和 Go 包装器已在路线图上。

---

## ⚡ 性能一览

| 成分 | 公制 | 与标准库对比 |
|---|---|---|
| **JSON 转储**（本机引擎） | 比 stdlib 快 3.1-5.0 倍 `json` | Python表面，测量2026-10-21 |
| **Gzip**（本机） | ~1.0x 与 stdlib gzip 级别 6 相比 | 1MB 有效负载（本机 gzip 为级别 4） |
| **Zstd**（本地） | 速度提高约 21 倍（1 级与 gzip 4 相比） | 1MB 有效负载 |
| **布罗特利**（本地人） | 最佳比率，比 gzip 慢约 1.6 倍 | 1MB 有效负载 |
| **DRF 串行器** | 尚未测量 | 查询集 → JSON |
| **Django ORM** | PostgreSQL 复制 | 批量插入本机 |
| **车轮尺寸** | 〜1.4MB | 原生，无需编译器 |
| **无 GIL 就绪** | Python 3.13+ | 自由线程支持 |
| **测试** | 1253 路过 | Rust 346 (lib + bin) + Python 907，加上 SDK 合约套件 ×7 |

---

## 🚀 快速入门

### 用一个命令尝试一下（离线，无需设置）

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` 运行引擎自己的基准测试，并在其中执行
打印它刚刚测量的结果——没有存储的数据，没有投影，没有网络。
历史每个框架乘数被打印为估计值，标记为
像这样。

更喜欢可以移交的文件？ `bash scripts/build-demo-bundle.sh` （或者
`bash cli.sh boost bundle` 从框架根）构建一个独立的
带音高的 ZIP、完整手册、二进制文件和一个命令
`demo.sh`。

### 共享核心（Python、Node.js、Java、.NET）

响应缓存、布隆过滤器和断路器——相同的原生原语
这四个SDK。所有四个都经过合同测试。

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

**。网**
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

### 压缩引擎

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**。网**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Java/Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**红宝石**
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

**去**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Express / ASP.NET 中间件

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 每种语言的完整用法都在 **[手册中](https://b4n1-com.github.io/b4n1-boost/)**。

---

## 🐍 Python 套件（中间件 + 加速器）

Python 包是最完整的一个：上面的所有内容，加上 HTTP
中间件套件和框架加速器。

```bash
pip install b4n1-boost
```

适用于 Linux (x86_64 + aarch64)、macOS (x86_64 + Apple Silicon) 和 Windows (x86_64) 的预编译本机轮子。无需编译器。

**支持的Python版本：** 3.10、3.11、3.12、3.13

### 姜戈
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# Report shows: {'framework': 'Django', 'middleware_installed': True, ...}
```

### 快速API
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### 烧瓶
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### 自动检测
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### 一行安装所有中间件
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 特点

### JSON 序列化（比 stdlib 快 3.1-5.0 倍） `json`）
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

### 压缩（比 gzip 4 级快约 21 倍，无 GIL）
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

### 内容类型感知中间件
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 缓存
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### 速率限制
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### 安全标头
```python
from b4n1_boost.middleware import SecurityHeadersMiddleware
app.wsgi_app = SecurityHeadersMiddleware(app.wsgi_app)
# Adds: X-Content-Type-Options, X-Frame-Options, HSTS, X-XSS-Protection, etc.
```

### 跨域资源共享
```python
from b4n1_boost.middleware import CORSMiddleware
app.wsgi_app = CORSMiddleware(app.wsgi_app, allow_origins=["https://example.com"])
```

### 健康检查
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### 缓存层
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Django ORM 加速器
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### DRF 串行器加速器
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

### JWT 验证
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### HTML/CSS/JS 缩小
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → Markdown（代理）
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### 遥测
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

### 后台工作者（零 GIL）
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

## 🔍 状态和诊断

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.4.5', 'native_extension': True, 'features': [...]}
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

## 🔗 链接

- 网站： https://b4n1.com
-PyPI： https://pypi.org/project/b4n1-boost
- npm： https://www.npmjs.com/package/b4n1-boost
- NuGet： https://www.nuget.org/packages/B4N1.Boost
- Maven 中心： https://central.sonatype.com/artifact/com.b4n1/boost
- 红宝石： https://rubygems.org/gems/b4n1-boost
- 包装师： https://packagist.org/packages/b4n1/boost
- 去： https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- 存储库： https://github.com/B4N1-com/b4n1-boost
- 许可： https://b4n1.com/licensing 或者 `b4n1@b4n1.com`
- 变更日志：[CHANGELOG.md](CHANGELOG.md)

---

## 📄 许可证

**商业源码许可证1.1（`BUSL-1.1`)** — 请注意，这*不是* SPDX id `BSL-1.1`，这表示 Boost Software License。

- **免费**用于开发、评估、测试、个人项目和年收入**10万美元**以下的初创公司。
- **商业许可证**适用于 >= **10 万美元**的组织、政府机构和公开招标。
- **更改日期**之后（4 年）→ **Apache 许可证 2.0**。

请参阅[许可证](LICENSE) 获取全文。

---

_b4n1-boost：多语言加速器。 1 个原生核心，7 个 SDK。 JSON 速度快 3-5 倍。压缩速度比 gzip 4 级快约 21 倍。中间件透明。与 ❤️ 一起构建 B4N1._
