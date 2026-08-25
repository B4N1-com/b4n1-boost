<div align="center">

# 📦 b4n1-boost

**Transparent native middleware acceleration layer for Python frameworks (Django, FastAPI, Flask, WSGI/ASGI).**

[![License](https://img.shields.io/badge/license-BSL%201.1-lightgrey)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)

</div>

# 🌍 Languages / Idiomas / 语言

|  |  |  |  |
|--|--|--|--|
| 🇬🇧 [English](README.md) | 🇪🇸 [Español](README.es.md) | 🇫🇷 [Français](README.fr.md) | 🇩🇪 [Deutsch](README.de.md) |
| 🇵🇹 [Português](README.pt-BR.md) | 🇨🇳 [简体中文](README.zh-CN.md) | 🇯🇵 [日本語](README.ja.md) | |

---

## 🚀 Features

- 🚀 **General Throughput Acceleration**: 3x to 11x faster request processing.
- ⚡ **JSON Serialization**: Up to 50x speedup over standard Python dynamic serialization.
- 🛡️ **Native Rust Middleware**: Zero-overhead FFI interop between Python and Rust.
- 🔐 **License Compliance**: BSL 1.1 with a clear free tier and enterprise licensing path.
- 📊 **Framework Support**: Django, FastAPI, Flask, WSGI/ASGI integration.

---

## 📦 Installation

```bash
pip install b4n1-boost
```

*Precompiled native binaries are bundled with the wheel for Linux, macOS and Windows — no compiler required.*

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
import b4n1_boost

b4n1_boost.install_fastapi()
```

### Flask
In your app initialization:

```python
import b4n1_boost

b4n1_boost.install_flask()
```

### Auto-detection
Let b4n1-boost detect the active framework automatically:

```python
import b4n1_boost

b4n1_boost.autoboost()
```

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
  "version": "0.1.4",
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