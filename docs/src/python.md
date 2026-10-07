# Python SDK

The primary SDK. Everything here is importable directly from `b4n1_boost`.

```python
import b4n1_boost
```

## Setup helpers

| Function | What it does |
|---|---|
| `install_django()` | Appends the boost middleware to `settings.MIDDLEWARE` |
| `install_fastapi(app)` | Registers compression and boost middleware on an ASGI app |
| `install_flask(app)` | Wraps the WSGI app |
| `autoboost()` | Detects Django / FastAPI / Flask and installs for it |
| `boost_all()` | Applies compression, ETag, security headers, CORS, rate limiting and health check |

```python
import b4n1_boost

report = b4n1_boost.boost_all()
print(report["applied"], report["middleware_count"])
```

## JSON

```python
from b4n1_boost import NativeJson, canonicalize_json, validate_json

NativeJson.dumps(data)            # fastest available backend
NativeJson.dumps_direct(data)     # skips the intermediate conversion
NativeJson.batch_dumps([a, b, c]) # N serializations, one lock acquire
NativeJson.batch_loads(bodies)
NativeJson.batch_validate(bodies)

canonicalize_json({"z": 1, "a": 2})   # '{"a":2,"z":1}' — sorted, compact
validate_json('{"valid": true}')      # True
```

`canonicalize_json` accepts either a `str` or a `dict` and returns a stable,
sorted-key, compact representation. Two equivalent objects produce byte-identical
output, which is what makes it useful for cache keys and signatures.

### Batch helpers

```python
from b4n1_boost import batch_dumps, batch_dumps_direct, batch_loads, batch_validate

bodies = batch_dumps(objects)
valid  = batch_validate(bodies)
objs   = batch_loads(bodies)
```

## Compression

```python
from b4n1_boost import compress

compress(payload, "zstd")     # 28x faster than stdlib gzip
compress(payload, "brotli")   # best ratio
compress(payload, "gzip")     # 1.47x faster than stdlib
```

### Static assets

```python
from b4n1_boost import compress_static_file, compress_static_dir

compress_static_file("app/static/app.js", algorithm="zstd")
compress_static_dir("app/static/", algorithm="zstd")
```

Images, video, audio, fonts and archives are skipped automatically.

## HTML → Markdown

```python
from b4n1_boost import html_to_markdown

html_to_markdown("<h1>Title</h1><p>Content with <b>bold</b></p>")
# '# Title\n\nContent with **bold**'
```

Useful when you want to hand a page to a language model as text rather than
as markup.

## Minification

```python
from b4n1_boost.advanced import minify_html, minify_css, minify_js

minify_html("<html>  <body>  Hello  </body>  </html>")
minify_css(css_source)
minify_js(js_source)
```

## JWT validation

```python
from b4n1_boost.advanced import validate_jwt

payload = validate_jwt(token, secret=JWT_SECRET, algorithm="HS256")
```

Validates HMAC-SHA256 tokens natively, so a service does not need a separate
JWT library just to verify incoming tokens.

## Worker-thread API

```python
from b4n1_boost import worker_compress, worker_decompress
from b4n1_boost import worker_minify, worker_jwt_validate, worker_shutdown

future = worker_compress(data, "zstd")
compressed = future.result()
```

Heavy operations run on a background thread. The calling thread is not
blocked and the interpreter lock is not held for the duration of the work.

## Background tasks

```python
from b4n1_boost import background, pending_tasks, native_async
```

See [Background Tasks](background.md).

## Telemetry

```python
from b4n1_boost import telemetry_init, capture_error, log_info, log_phase, flush

telemetry_init(dsn="https://...")
capture_error(Exception("something"), context={"user": "123"})
log_info("Request processed", phase="http")
flush()
```

Telemetry is opt-in. Without an explicit `telemetry_init(...)` call nothing
is emitted.

## Introspection

```python
import b4n1_boost

b4n1_boost.__version__       # package version
b4n1_boost.status()          # engines and features actually loaded
b4n1_boost.run_benchmarks()  # hardware benchmarks on this machine
```

## Full export list

```python
import b4n1_boost
print(b4n1_boost.__all__)
```

`__all__` is the authoritative list of public names. Anything not in it is
internal and may change between minor versions.

## See also

- [Middleware Reference](middleware.md) — every middleware class in detail
- [Django & DRF Accelerators](accelerators.md) — ORM and serializer speedups
- [Status & Diagnostics](status.md) — verifying what loaded
