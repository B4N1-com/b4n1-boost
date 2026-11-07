# Changelog

Notable changes per release, following
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The full detail lives in `CHANGELOG.md` in the repository. This page is the
curated view.

## [0.4.7] — current

**PyPI ships every platform again.** 0.4.4, 0.4.5 and 0.4.6 were published with
a single linux x86_64 wheel, so macOS, Windows and arm64 kept resolving 0.4.3
while the documentation promised the full matrix. 0.4.7 publishes all five
wheels (linux x64/arm64, macos x64/arm64, win x64) and the release step now
refuses to upload a version missing one of them.

## [0.4.6]

- **`zstd decompression` in Ruby, PHP and Go.** The C symbol was already
exported and declared in those bindings but never wrapped, so those SDKs could
compress and not decompress what they produced. Round-trips are contract-tested.
- **Ruby: documented entry points.** `require 'b4n1_boost'` and
`require 'b4n1_boost/rack'` used to raise `LoadError` (the gem only shipped
root files); both now load, and the middleware entry point no longer shadows
the real `rack` gem.
- **Docs corrected against the code:** the capability matrix marked Ruby, PHP
and Go as missing cache/bloom/breaker (they shipped them) and claimed a Python
bloom filter (its `BloomRateLimiter` is an exact per-IP window). The Go import
path and the PHP class name in the docs were wrong too.

## [0.4.5]

Packagist and the Go module proxy index the published repository itself, not a
copy: `public-repos/b4n1-boost` is now a submodule of
`B4N1-com/b4n1-boost`, so the tag a registry reads and the tree the SDK is
built from are the same commit. Before this, 0.4.5 announced the new version
while PHP and Go served the previous one.

## [0.4.4]

Seven registries, seven SDKs. Ruby (RubyGems), PHP (Packagist) and Go
(module proxy) join PyPI, npm, NuGet and Maven Central — every SDK wraps the
same native core, contract-tested per language. The Ruby, PHP and Go packages
bundle the precompiled core for linux/macos/windows, so they install and run
with no compiler.

Core fixes in this release: the canonical JSON writer is byte-compatible with
the standard library writer, the background worker revives cleanly after
shutdown, and `i64::MIN` serializes correctly.

## [0.4.0] — 2026-10-14

Polyglot release. One C-ABI, seven language SDKs — Node.js, Ruby, PHP, Go,
Java and .NET alongside Python. Published to PyPI, npm, NuGet and Maven
Central.

## [0.3.15]

Fourth registry released: the Java SDK is now on Maven Central as
`com.b4n1:boost`, alongside PyPI, npm and NuGet. Release verification suite:
38 checks passing.

## [0.3.11]

Packaging and record-correctness fixes across the published artifacts:
wheel metadata now matches its archive contents exactly, so registries
accept uploads without post-hoc warnings.

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
- `bulk_insert_native()` (PostgreSQL `COPY`) + `FastModelMixin` — 5-10x
  faster bulk writes
- `html_to_markdown()` — HTML to clean Markdown for LLM consumption
- `minify_html()`, `minify_css()`, `minify_js()`
- JWT validation with an HMAC-SHA256/512 path and a fallback
- `ResponseCache` (LRU, TTL), `BloomRateLimiter`, `CircuitBreaker`
- `compress_static_file()` / `compress_static_dir()`
- Telemetry bindings: init, capture_error, log_info, log_phase, flush

### Changed

- JSON path moved to a substantially faster backend — 10.5x over `json.dumps`
  on medium payloads
- Middleware refactored onto unified WSGI/ASGI base classes

### Fixed

- Middleware installs are idempotent — a double install no longer stacks
  duplicates
- Native JSON path used directly in middleware, removing an intermediate
  conversion
- README installation URL

## [0.2.0] — 2026-08-28

### Added

- Zstd compression — 28x faster than stdlib gzip
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
