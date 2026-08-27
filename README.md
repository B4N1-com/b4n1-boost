<div align="center">

# 📦 b4n1-boost

**Transparent native middleware acceleration layer for Python frameworks (Django, FastAPI, Flask, WSGI/ASGI).**

[![License](https://img.shields.io/badge/license-BSL%201.1-lightgrey)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)

</div>

# 🌍 Languages / Idiomas / 语言

|  |  |  |  |
|--|--|--|--|
| 🇬🇧 [English](README.md) | 🇪🇸 [Español](i18n/README.es.md) | 🇫🇷 [Français](i18n/README.fr.md) | 🇩🇪 [Deutsch](i18n/README.de.md) |
| 🇵🇹 [Português](i18n/README.pt-BR.md) | 🇨🇳 [简体中文](i18n/README.zh-CN.md) | 🇯🇵 [日本語](i18n/README.ja.md) | |

---

## 🚀 Features

- 🛡️ **Native Rust Middleware**: transparent WSGI/ASGI/Django middleware with a zero-copy pass-through response path.
- 🗜️ **Native Response Compression**: gzip & Brotli implemented in Rust (GIL-free), negotiated via `Accept-Encoding`.
- ⚡ **Native JSON Engine**: canonical JSON serialization available for opt-in use.
- 📊 **Framework Support**: Django, FastAPI, Flask, plain WSGI and ASGI apps.
- 🐍 **Python Support**: 3.10, 3.11, 3.12 and 3.13 (abi3).
- 🔐 **License Compliance**: BSL 1.1 with a clear free tier and enterprise licensing path.

> Measure acceleration end-to-end in your own application — actual gains depend on your workload.

---

## 📦 Installation

```bash
pip install b4n1-boost
```

*Precompiled native binaries are bundled with the wheel for Linux x86_64 (Python 3.10+). Other platforms build from source with a Rust toolchain.*

---

## 🚀 Quick Start

No code rewrites. Initialize the SDK when your app starts:

### Django
In your `settings.py` or `wsgi.py`:

```python
import b4n1_boost

b4n1_boost.install_django()
```

### FastAPI
In your main module:

```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Flask
In your app initialization:

```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Auto-detection
Let b4n1-boost detect the active framework automatically:

```python
import b4n1_boost

b4n1_boost.autoboost()
```

---

## 🗜️ Response Compression

Wrap any WSGI app (Flask, Django, plain WSGI) with native gzip/Brotli compression:

```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

app.wsgi_app = B4N1BoostCompressionMiddleware(app.wsgi_app)
```

For FastAPI/Starlette (ASGI):

```python
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware

app = FastAPIBoostCompressionMiddleware(app)
```

The middleware negotiates `Accept-Encoding` (prefers Brotli), skips payloads under 1 KB, sets `Content-Encoding`, `Content-Length` and `Vary`, and falls back to the untouched body if the native engine is unavailable.

---

## 🔍 Status & Diagnostics

Check the engine state and active accelerations:

```python
import b4n1_boost

print(b4n1_boost.status())
```

Expected output:

```json
{
  "native_extension": true,
  "version": "0.1.8",
  "features": ["json_acceleration", "orm_interception", "websocket_acceleration"]
}
```

Run the native benchmark suite:

```python
report = b4n1_boost.run_benchmarks(iterations=100_000)
print(f"JSON ops/sec: {report['json_bench']['ops_per_sec']:,.0f}")
print(f"ORM ops/sec:  {report['orm_bench']['ops_per_sec']:,.0f}")
```

---

## 🔗 Links

- Website: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- Licensing: https://b4n1.com/licensing or `b4n1@b4n1.com`

---

## 📄 License

This project is distributed under the **Business Source License 1.1 (BSL 1.1)**.

- **Free** for development, evaluation, testing, personal projects, and startups generating under **$100,000 USD** in annual gross revenue.
- **Commercial license** required for organizations with annual gross revenue **>= $100,000 USD**, government agencies, and public bidding projects.
- After the **Change Date** (4 years), the work converts to **Apache License 2.0**.

See [LICENSE](LICENSE) for the full legal text.

---

_b4n1-boost is a core component of the B4N1 sovereign computing stack, providing transparent native middleware acceleration for Python frameworks._

_Built with ❤️ by the B4N1 team._
---

## 💖 Support

Support our open-source research and systems engineering journey by sponsoring us on GitHub: https://github.com/sponsors/BaniMontoya
