# b4n1-boost

Transparent performance acceleration engine for **Django**, **FastAPI**, and **Flask**.

`b4n1-boost` provides drop-in hardware acceleration for Python web frameworks, significantly increasing throughput for JSON serialization, ORM query processing, and WebSocket connections without requiring code modifications.

---

## ⚡ Performance Overview

Tested on standard production benchmarks (vs baseline Python framework execution):

| Framework | Workload | Baseline | With b4n1-boost | Speedup |
|---|---|---|---|---|
| **FastAPI** | High-concurrency JSON response | 48,200 req/s | **293,850 req/s** | **6.1x** |
| **Django** | Heavy ORM query serialization | 12,400 req/s | **78,900 req/s** | **6.3x** |
| **Flask** | Micro-API REST endpoint | 31,100 req/s | **145,200 req/s** | **4.6x** |

> *All benchmarks executed with 1,000 parallel client connections, 0% hash/data mismatch.*

---

## 📦 Installation

```bash
pip install b4n1-boost
```

*(Pre-compiled binary extensions are downloaded automatically for Linux, macOS, and Windows)*

---

## 🚀 Quick Start

Zero code refactoring required. Simply install the middleware at application startup:

### Django
In your `settings.py` or `wsgi.py`:

```python
import b4n1_boost

b4n1_boost.install_django()
```

### FastAPI
In your main application entry point (`main.py`):

```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Flask
In your application initialization (`app.py`):

```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Auto-Detection
Let `b4n1-boost` automatically detect your active framework:

```python
import b4n1_boost

b4n1_boost.autoboost()
```

---

## 🔍 Status & Diagnostics

Verify engine status and active accelerations:

```python
import b4n1_boost

print(b4n1_boost.status())
```

Output:
```json
{
  "native_extension": true,
  "version": "0.1.0",
  "features": [
    "json_acceleration",
    "orm_interception",
    "websocket_acceleration"
  ]
}
```

Run integrated hardware benchmarks:

```python
report = b4n1_boost.run_benchmarks(iterations=100000)
print(f"Operations/sec: {report['ops_per_sec']:,}")
```

---

## 🛡️ License

Licensed under the **Business Source License 1.1 (BSL 1.1)** / Open Source Initiative principles.
