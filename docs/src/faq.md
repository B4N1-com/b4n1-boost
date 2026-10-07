# Frequently Asked Questions

## Does it really work without changing my code?

Yes. `install_django()`, `install_fastapi(app)` and `install_flask(app)` wire
middleware around your application. Views, templates, models and serializers
stay as they are.

The two exceptions are the accelerators, which you opt into explicitly:
[Django & DRF Accelerators](accelerators.md) replace a specific call site
(`bulk_insert_native`, `fast_serialize`) because they produce the same result
by a different route.

## Do I need to compile anything?

No. Wheels are precompiled for Linux (x86_64, aarch64), macOS (x86_64,
arm64) and Windows x86_64. `pip install b4n1-boost` is the whole step — no
compiler, no build backend, no system libraries.

## How do I know it actually loaded?

```python
import b4n1_boost
assert b4n1_boost.status()["native_extension"] is True
```

Do this before benchmarking. See [Status & Diagnostics](status.md).

## Do I need Redis or a broker?

No, for [background tasks](background.md). Work is dispatched to a worker
thread with optional disk journaling.

You should still use a real queue when tasks must survive losing the machine,
be shared across hosts, or need scheduled delivery. Journaling gives restart
safety on one host — it is not distributed coordination.

## Which compression algorithm should I use?

| Algorithm | Choose it for |
|---|---|
| `zstd` | API responses and JSON bodies — fastest |
| `gzip` | widest compatibility |
| `brotli` | static assets — best ratio |

For static files, `compress_static_dir` skips already-compressed formats
(images, video, audio, fonts, archives) automatically.

## Will it help if my app is not CPU-bound?

Probably not. b4n1-boost removes CPU time spent on serialization, compression
and static assets. If your bottleneck is database latency, network I/O or an
external API, the headroom is elsewhere.

Measure first: if `run_benchmarks()` shows no meaningful gap against the
standard library on your payloads, there is nothing to gain.

## Is it safe to run behind a reverse proxy?

Yes. `detect_proxy()` determines whether a proxy is in front of the app so
headers like `X-Forwarded-For` are only trusted when they came from one.

```python
from b4n1_boost.middleware import detect_proxy
```

Never trust forwarded headers unconditionally — a client can forge them.

## Does it support async frameworks?

Yes. Every middleware has an ASGI variant (`ASGIETagMiddleware`,
`ASGICORSMiddleware`, `ASGISecurityHeadersMiddleware`,
`ASGIRateLimitMiddleware`, `ASGIHealthCheckMiddleware`,
`ASGIRequestLoggingMiddleware`,
`FastAPIBoostCompressionMiddleware`), and compression streams responses
rather than buffering them.

## Can I use only part of it?

Yes. The pieces are independent — compression, ETag, security headers, CORS,
rate limiting, health check and the utilities can each be used alone.
`boost_all()` installs the common set in one call; individual middleware can
be added by hand when you want a different configuration.

## What happens on an unsupported platform?

The Python package falls back to a pure-Python path: correct output, no
native speed. Node.js does the same, except for `compressZstd` and
`decompressZstd`, which **throw** rather than silently producing a different
format.

Check `status()["native_extension"]` (Python) or `isAvailable()` (Node) to
know which path you are on.

## What is the difference between `dumps` and `dumps_direct`?

| Call | Path |
|---|---|
| `NativeJson.dumps(data)` | fastest available backend, general purpose |
| `NativeJson.dumps_direct(data)` | skips the intermediate conversion entirely |
| `NativeJson.batch_dumps([...])` | N serializations inside one lock acquire |

`batch_dumps` is where the largest wins appear for list-shaped workloads,
because per-call overhead is paid once instead of N times.

## Which license applies?

The SDK wrapper source is
[Business Source License 1.1 (BUSL-1.1)](license.md). The precompiled native
binaries are covered by a separate `EULA.txt` that ships inside each artifact.

Production use is free for organizations with total annual gross revenue up
to USD $100,000. Above that, or for reselling it as a managed service, a
commercial license is required.

## Where do I report bugs?

Open an issue on
[github.com/B4N1-com/b4n1-boost](https://github.com/B4N1-com/b4n1-boost).
Include the diagnostic output listed in
[Status & Diagnostics](status.md) — status, Python version, OS/architecture
and the exact failing command.

## See also

- [Quick Start](quickstart.md)
- [Performance](performance.md)
- [License](license.md)
