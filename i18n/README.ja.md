<p align="center">
  <img src="docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

<div align="center">

#📦 b4n1-boost

**ポリグロット アクセラレータ。 1 つのネイティブ コア、7 つの SDK (Python、Node.js、Ruby、PHP、Java、.NET、Go)。 JSON は 3 ～ 5 倍高速、圧縮は最大 21 倍高速 (測定値)、すべてのコア SDK に応答キャッシュ、ブルーム フィルター、サーキット ブレーカーが搭載されています。**

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

> 📚 **完全なマニュアル (インストール、ミドルウェア、アクセラレータ、パフォーマンス):**
> **[https://b4n1-com.github.io/b4n1-boost/](https://b4n1-com.github.io/b4n1-boost/)**

</div>

## 🖥 プラットフォームのサポート

| プラットフォーム | アーキテクチャ |
|----------|---------------|
| **Linux** | x86_64、aarch64 |
| **macOS** | x86_64、arm64 (Apple シリコン) |
| **Windows** | x86_64 |

**すべてのプラットフォームおよびすべての言語向けにコンパイル済みのバイナリ** — コンパイラは不要で、すぐに使用できます。

---

## 📦 インストール — 7 レジストリ、1 コア

| レジストリ | 言語 | パッケージ | 指示 |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10以降 | `b4n1-boost` | `pip install b4n1-boost` |
| **npm** | Node.js | `b4n1-boost` | `npm install b4n1-boost` |
| **NuGet** | .NET / C# | `B4N1.Boost` | `dotnet add package B4N1.Boost` |
| **メイブン** | Java / コトリン | `com.b4n1:boost` | `implementation 'com.b4n1:boost:0.4.3'` |
| **ルビージェム** | ルビー / ラック | `b4n1-boost` | `gem install b4n1-boost` |
| **パッケージニスト** | PHP / ララベル | `b4n1/boost` | `composer require b4n1/boost` |
| **行く** | ゴー 1.23+ | `b4n1-boost/sdks/go` | `go get github.com/B4N1-com/b4n1-boost/sdks/go` |

7 つのパッケージはすべて **同じネイティブ コア** (プリコンパイル済み、コンパイラなし) を同梱しています。
必要です）。 Python ホイールにはさらに HTTP ミドルウェア スイートがバンドルされており、
Ruby/PHP/Go パッケージには、プラットフォームのネイティブ ライブラリがバンドルされています。

---

**言語:** [العربية](i18n/README.ar.md) · [ドイツ語]](i18n/README.de.md) · [スペイン語](i18n/README.es.md) ・【フランセ】](i18n/README.fr.md) · [हिन्दी]](i18n/README.hi.md) ・【イタリア語】](i18n/README.it.md) · [日本語](i18n/README.ja.md) · [한국어]](i18n/README.ko.md) · [ポルトガル語 (BR)](i18n/README.pt-BR.md) · [Русский]](i18n/README.ru.md) · [中文](i18n/README.zh-CN.md)

## 🧩 各 SDK が提供するもの

| 能力 | パイソン | Node.js | Java / コトリン | 。ネット | ルビー | PHP | 行く |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| レスポンスキャッシュ(LRU+TTL) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| ブルームフィルター | ✅ | ✅ | ✅ | ✅ | — | — | — |
| サーキットブレーカー | ✅ | ✅ | ✅ | ✅ | — | — | — |
| Gzip / Zstd 圧縮 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTML の縮小 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| JSON検証 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP ミドルウェア (圧縮、ETag、CORS、レート制限、セキュリティ ヘッダー、解凍、ヘルス チェック) | ✅ | 急行 | — | ASP.NET | ラック | ララベル | — |
| Zstd解凍 | ✅ | ✅ | ✅ | ✅ | — | — | — |
| バックグラウンド タスク (Redis、Celery なし) | ✅ | ✅ | ✅ | ✅ | — | — | — |
| ブロトリ圧縮 | ✅ | — | — | — | — | — | — |
| 縮小化(CSS/JS)+HTML→Markdown | ✅ | — | — | — | — | — | — |
| JWTの検証 | ✅ | — | — | — | — | — | — |
| JSON エンジンが 3.1 ～ 5.0 倍高速化 | ✅ | — | — | — | — | — | — |
| Django ORM / DRF / SQLAlchemy アクセラレータ | ✅ | — | — | — | — | — | — |

圧縮 + 縮小 + JSON コアは ** すべて同じネイティブ呼び出しです
7 つの言語** (1 つの C-ABI、言語ごとに契約テスト済み)。キャッシュ、ブルーム
フィルターとサーキット ブレーカーは、Python、Node.js、Java で契約テストされており、
。ネット;彼らの Ruby、PHP、Go ラッパーはロードマップに載っています。

---

## ⚡ パフォーマンスの概要

| 成分 | メトリック | 対標準ライブラリ |
|---|---|---|
| **JSON ダンプ** (ネイティブ エンジン) | stdlib よりも 3.1 ～ 5.0 倍高速 `json` | Python 表面、2026 年 10 月 21 日に測定 |
| **Gzip** (ネイティブ) | ~1.0x 対 stdlib gzip レベル 6 | 1MB ペイロード (ネイティブ gzip はレベル 4) |
| **Zstd** (ネイティブ) | ~21 倍高速 (レベル 1 対 gzip 4) | 1MBのペイロード |
| **ブロトリ** (ネイティブ) | 最適な比率、gzip よりも最大 1.6 倍遅い | 1MBのペイロード |
| **DRF シリアライザ** | まだ測定されていません | クエリセット → JSON |
| **ジャンゴ ORM** | PostgreSQLのコピー | 一括挿入ネイティブ |
| **ホイールサイズ** | ～1.4MB | ネイティブなのでコンパイラは不要 |
| **GIL なし対応** | Python 3.13+ | フリースレッドのサポート |
| **テスト** | 1253 合格 | Rust 346 (lib + bin) + Python 907、および SDK コントラクト スイート × 7 |

---

## 🚀 クイックスタート

### 1 つのコマンドで試してみる (オフライン、セットアップなし)

```bash
pip install b4n1-boost
b4n1-boost demo          # live numbers from the engine, on your machine
b4n1-boost docs --list   # the manual, bundled inside the binary
```

`b4n1-boost demo` エンジンが実行される場所でエンジン独自のベンチマークを実行し、
測定したばかりの結果を出力します。保存された数値、投影、ネットワークはありません。
過去のフレームワークごとの乗数が推定値としてラベル付けされて出力されます。
そのような。

渡せるファイルの方がいいですか? `bash scripts/build-demo-bundle.sh` （または
`bash cli.sh boost bundle` フレームワークのルートから) 自己完結型を構築します。
ピッチ、完全なマニュアル、バイナリ、および 1 つのコマンドを含む ZIP
`demo.sh`。

### 共有コア (Python、Node.js、Java、.NET)

レスポンス キャッシュ、ブルーム フィルター、サーキット ブレーカー - 同じネイティブ プリミティブ
これら 4 つの SDK です。 4 つすべてで契約テスト済み。

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

**。ネット**
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

**パイソン**
```python
from b4n1_boost import ResponseCache

cache = ResponseCache(1024, 60)                   # capacity, default TTL (s)
cache.set("user:1", b'{"id":1}', [], 200)         # key, body, headers, status
```

### 圧縮エンジン

**Node.js**
```javascript
const boost = require('b4n1-boost');

const zstd = boost.compressZstd(payload);      // ~21x faster than gzip level 4 (1MB)
const back = boost.decompressZstd(zstd);
const min  = boost.minifyHtml(html);
```

**。ネット**
```csharp
var zstd = NativeBoost.CompressZstd(payload);
```

**Java / Kotlin**
```java
byte[] zstd = Boost.compressZstd(data, 3);
```

**ルビー**
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

**行く**
```go
import boost "github.com/B4N1-com/b4n1-boost/sdks/go"

zstd, _ := boost.CompressZstd(payload, 3)
min := boost.MinifyHTML(html)
ok := boost.IsJSONValid(body)
```

### Express / ASP.NET ミドルウェア

```javascript
const express = require('express');
const boostMiddleware = require('b4n1-boost/express');

app.use(boostMiddleware({ minifyHtml: true, gzipLevel: 4 }));
```

> 📚 各言語の完全な使用法は **[マニュアルに記載されています](https://b4n1-com.github.io/b4n1-boost/)**。

---

## 🐍 Python スイート (ミドルウェア + アクセラレータ)

Python パッケージは最も完全なパッケージです。上記のすべてに加えて HTTP
ミドルウェア スイートとフレームワーク アクセラレータ。

```bash
pip install b4n1-boost
```

Linux (x86_64 + aarch64)、macOS (x86_64 + Apple Silicon)、および Windows (x86_64) 用のプリコンパイル済みネイティブ ホイール。コンパイラは必要ありません。

**サポートされている Python バージョン:** 3.10、3.11、3.12、3.13

### ジャンゴ
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

### フラスコ
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### 自動検出
```python
import b4n1_boost
b4n1_boost.autoboost()  # Detects Django/FastAPI/Flask automatically
```

### すべてのミドルウェアを 1 行でインストール
```python
import b4n1_boost
report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS + rate limiting + health check
# Returns: {'framework': 'Django', 'applied': ['compression', 'etag', ...], 'middleware_count': 6}
```

---

## 🔧 特徴

### JSON シリアル化 (stdlib より 3.1 ～ 5.0 倍高速) `json`)
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

### 圧縮 (gzip レベル 4 より約 21 倍高速、GIL フリー)
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

### コンテンツタイプ認識ミドルウェア
```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Automatically skips: images, video, audio, fonts, archives, already-compressed
app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app, min_size=1024)

# For FastAPI/ASGI (streaming support)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 キャッシング
```python
from b4n1_boost.middleware import ETagMiddleware
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### レート制限
```python
from b4n1_boost.middleware import RateLimitMiddleware
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### セキュリティヘッダー
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

### 健康診断
```python
from b4n1_boost.middleware import HealthCheckMiddleware
app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
# GET /health → 200 {"status": "ok"}
```

### キャッシュ層
```python
from b4n1_boost.advanced import ResponseCache

cache = ResponseCache(capacity=1000, default_ttl=300)
cache.set("/users", b'{"ok":true}', [], 200)
body, headers, status = cache.get("/users")
```

### Django ORM アクセラレータ
```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — native bulk insert (speed not measured yet)
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### DRF シリアライザ アクセラレータ
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

### JWT 検証
```python
from b4n1_boost.advanced import validate_jwt

# Native HMAC-SHA256 (no PyJWT dependency required)
payload = validate_jwt(token, secret="my-secret", algorithm="HS256")
```

### HTML/CSS/JS の縮小化
```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minified = minify_html("<html>  <body>  Hello  </body>  </html>")
```

### HTML → マークダウン (エージェント)
```python
from b4n1_boost import html_to_markdown

markdown = html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# → "# Title\n\nContent with **bold**"
```

### テレメトリー
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

### バックグラウンド ワーカー (ゼロ GIL)
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

## 🔍 ステータスと診断

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

## 🔗 リンク

- Webサイト： https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- npm: https://www.npmjs.com/package/b4n1-boost
- NuGet: https://www.nuget.org/packages/B4N1.Boost
- Maven セントラル: https://central.sonatype.com/artifact/com.b4n1/boost
- RubyGems: https://rubygems.org/gems/b4n1-boost
- パッケージ担当者: https://packagist.org/packages/b4n1/boost
- 行く： https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go
- リポジトリ: https://github.com/B4N1-com/b4n1-boost
- ライセンス: https://b4n1.com/licensing または `b4n1@b4n1.com`
- 変更履歴: [CHANGELOG.md]](CHANGELOG.md)

---

## 📄 ライセンス

**ビジネス ソース ライセンス 1.1 (`BUSL-1.1`)** — これは SPDX ID ではないことに注意してください。 `BSL-1.1`を意味します。 Boost Software License。

- **年間収益 **10 万ドル** 未満の開発、評価、テスト、個人プロジェクト、スタートアップの場合は **無料**。
- **10 万ドル以上の組織、政府機関、公共入札には **商用ライセンス**が必要です。
- **日付変更**後 (4 年) → **Apache License 2.0**。

「ライセンス」を参照してください。](LICENSE) 全文については。

---

_b4n1-boost: ポリグロット アクセラレータ。 1 つのネイティブ コア、7 つの SDK。 JSON は 3 ～ 5 倍高速になります。圧縮は gzip レベル 4 よりも最大 21 倍高速です。ミドルウェアは透過的です。 ❤️ で構築 B4N1._
