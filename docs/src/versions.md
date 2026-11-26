# Release history

Notable changes per release. Every entry says what changed for you, and a
version you install is the same version on every channel. The current release
is **0.6.4**.

## [0.6.4]

Version alignment across the seven packages.

## [0.6.3]

Every package now carries the Business Source License 1.1 text and the
prebuilt accelerator for its platform, so installing one channel gives you the
same terms and the same binary as the rest.

## [0.6.2]

Version alignment, and each registry page shows a README written for its own
language instead of one shared introduction.

## [0.6.1]

Documentation release; the accelerator itself is unchanged.

- **PHP developers get PHP answers:** the Packagist page now opens with the PHP
  installation command instead of a Python one.
- **The .NET package ships a readme**, so the registry page explains what the
  package does.
- **C# and Java have their own README** with their install command and the
  bundled accelerator.

## [0.6.0]

An accelerator that fails quietly is worse than one that fails loudly, because
nobody knows to look. This release makes a degraded compression path countable
and fixes the request-killing path that made it look fine.

- **Compression failures are visible.** Serving a response uncompressed when the
  accelerator raises stays the right behaviour — boost is optional and never
  fails a request — but it now leaves a trace: `CompressionMetrics` counts
  `failed_compressions` and `failures_by_algorithm` and derives
  `failure_rate_pct`, exported to Prometheus and OpenTelemetry.
- **A codec can no longer take the request down:** an unpatched binding or a
  compressor replaced by the application degrades the response instead of
  answering 500.
- **The failure counter reads correctly for the whole request.**

## [0.5.0]

Three capabilities the configuration surface promised and now delivers, plus a
throughput gain:

- **WebSocket compression (RFC 7692 permessage-deflate):**
  `enable_websocket_acceleration` is now backed by
  `WebSocketCompressionMiddleware` instead of being a flag with nothing behind
  it.
- **Prometheus / OpenTelemetry export:** the counters `CompressionMetrics` has
  always kept are scrapeable at `/metrics` and readable as JSON
  (`?format=otel`), from one source of truth.
- **gzip up to 2.3x faster:** 1 MB HTML at level 4 goes 0.10 → 0.15 GB/s and at
  level 6 0.06 → 0.14 GB/s, with the compression ratio unchanged.

## [0.4.7]

**Every platform ships in every release.** All five platform packages (Linux
x64/arm64, macOS Intel/Apple Silicon, Windows x64) are published together; a
version missing one of them is not released, so no platform is left on an older
version while the documentation promises the full set.

## [0.4.6]

- **`zstd` decompression in Ruby, PHP and Go.** Those packages could compress
  and not decompress what they produced. Both directions are covered by
  round-trip tests now.
- **Ruby: the documented entry points load.** `require 'b4n1_boost'` and
  `require 'b4n1_boost/rack'` used to raise `LoadError`; both load, and the
  middleware no longer shadows the real `rack` package.
- **Docs corrected against the code:** the capability matrix marked Ruby, PHP
  and Go as missing cache/bloom/breaker (they shipped them) and claimed a Python
  bloom filter (its limiter is an exact per-IP window). The Go import path and
  the PHP class name in the docs were wrong too.

## [0.4.5]

- **PHP and Go follow the same published repository as the other channels,** so
  a release reaches every channel at the same version instead of leaving PHP and
  Go on the previous one.

## [0.4.4]

Seven channels, seven SDKs. RubyGems, Packagist and the Go module proxy join
PyPI, npm, NuGet and Maven Central — every SDK wraps the same accelerator and is
contract-tested per language. The Ruby, PHP and Go packages bundle the
precompiled core for Linux, macOS and Windows, so they install and run with no
compiler.

Core fixes in this release: the JSON writer is byte-compatible with the standard
library writer, the background worker revives cleanly after shutdown, and the
smallest signed 64-bit integer serialises correctly.

## [0.4.0] — 2026-10-14

Polyglot release. One engine, seven language SDKs — Node.js, Ruby, PHP, Go, Java
and .NET alongside Python — published across the seven channels.

## [0.3.15]

Java SDK available as `com.b4n1:boost`.

## [0.3.11]

**Packaging corrections.** The metadata of every package matches its contents
exactly, so each channel installs the full set it advertises.

## [0.3.0] — 2026-09-01

The middleware and accelerator release.

### Added

**Middleware**
- `SecurityHeadersMiddleware` — `X-Content-Type-Options`, `X-Frame-Options`,
  `Strict-Transport-Security`, `X-XSS-Protection`, `Referrer-Policy`,
  `Permissions-Policy`
- `CORSMiddleware` with configurable origins, methods and headers
- `HealthCheckMiddleware` — `GET /health` returns 200 JSON
- `DecompressionMiddleware` — accepts gzip/brotli/zstd request bodies
- `CacheMiddleware` backed by `ResponseCache` (LRU + TTL)
- `RequestLoggingMiddleware` and its ASGI variant
- `ETagMiddleware` with 304 handling
- `RateLimitMiddleware` — token bucket per client IP
- Content-Type aware compression
- `CompressionMetrics` — bytes in/out, request count, ratio
- `detect_proxy()` — forwarded-header trust detection
- `boost_all()` — install the common set in one call

**Acceleration**
- `NativeJson.batch_dumps()` — N serializations in a single lock acquire
- Worker thread for compression, minification and JWT — heavy work off the
  calling thread
- `fast_serialize()` + `FastSerializerMixin` — 5-10x faster queryset → JSON
- `bulk_insert_native()` (PostgreSQL `COPY`) + `FastModelMixin` — 5-10x faster
  bulk writes
- `html_to_markdown()` — HTML to clean Markdown for LLM consumption
- `minify_html()`, `minify_css()`, `minify_js()`
- JWT validation with an HMAC-SHA256/512 path and a fallback
- `ResponseCache` (LRU, TTL), `BloomRateLimiter`, `CircuitBreaker`
- `compress_static_file()` / `compress_static_dir()`
- Telemetry bindings: init, capture_error, log_info, log_phase, flush

### Changed

- JSON path moved to a substantially faster backend — 10.5x over `json.dumps` on
  medium payloads
- Middleware refactored onto unified WSGI/ASGI base classes

### Fixed

- Middleware installs are idempotent — a double install no longer stacks
  duplicates
- Native JSON path used directly in middleware, removing an intermediate
  conversion
- README installation URL

## [0.2.0] — 2026-08-28

### Added

- Zstd compression — 28x faster than the standard library gzip
- Content-Type aware middleware
- ETag generation and 304 caching
- Rate limiting (token bucket)
- Proxy detection headers
- Compression metrics collection

### Changed

- Improved middleware architecture

## [0.1.0]

Initial release: native JSON serialization, gzip/brotli compression, and the
Django / FastAPI / Flask installers.

## See also

- [Status & Diagnostics](status.md) — how to check your installed version
- [License](license.md)
