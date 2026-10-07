# Quick Start

Install, import, and the accelerator is live.

```bash
pip install b4n1-boost
```

## Django

```python
import b4n1_boost

report = b4n1_boost.install_django()
# Appends DjangoBoostMiddleware to settings.MIDDLEWARE
# {'framework': 'Django', 'middleware_installed': True, ...}
```

## FastAPI

```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

## Flask

```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

## Auto-detection

If you would rather not name the framework, `autoboost()` detects it:

```python
import b4n1_boost
b4n1_boost.autoboost()   # Detects Django/FastAPI/Flask automatically
```

## Install everything at once

```python
import b4n1_boost

report = b4n1_boost.boost_all()
# Applies: compression + ETag + security headers + CORS
#          + rate limiting + health check
# {'framework': 'Django',
#  'applied': ['compression', 'etag', ...],
#  'middleware_count': 6}
```

## Use the fast paths directly

The installers wire up middleware. The utilities are usable on their own:

```python
from b4n1_boost import NativeJson, canonicalize_json, validate_json, compress

payload = {"users": [{"id": i, "name": "user"} for i in range(500)]}

body = NativeJson.dumps(payload)          # 10x faster than json.dumps
assert validate_json(body)                # True
assert canonicalize_json({"z": 1, "a": 2}) == '{"a":2,"z":1}'

wire = compress(body, "zstd")             # 28x faster than gzip
```

## Verify it loaded

```python
import b4n1_boost

print(b4n1_boost.status())
# {'native_extension': True, 'version': '0.3.12', 'features': {...}}
```

If `native_extension` is `False`, the native core did not load — see
[Status & Diagnostics](status.md) for how to diagnose it before you
chase performance numbers that will not materialise.

## Next

- [Installation](installation.md) for platform and Python version details
- [Performance](performance.md) for the benchmark table and how to run it
- [Python SDK](python.md) for the complete API
