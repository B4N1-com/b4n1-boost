# PHP SDK

```bash
composer require b4n1/boost
```

## API

Static methods on the `Boost` class:

```php
use B4N1\Boost;   // class B4N1\Boost (Boost.php). Core classes live under the B4N1\Boost namespace.

$gz   = Boost::compressGzip($data, 4);
$zst  = Boost::compressZstd($data, 3);
$html = Boost::minifyHtml($rawHtml);
$ok   = Boost::isJsonValid($json);
```

| Method | Signature |
|---|---|
| `compressGzip` | `(string $data, int $level = 4): string` |
| `compressZstd` | `(string $data, int $level = 3): string` |
| `decompressZstd` | `(string $data): string` |
| `minifyHtml` | `(string $html): string` |
| `isJsonValid` | `(string $json): bool` |

The extension is loaded lazily on first use — there is no manual
`bootstrap` call to remember.

## Middleware

```php
use B4N1\Boost\Middleware\BoostMiddleware;

$app->add(new BoostMiddleware(minifyHtml: true, gzipLevel: 4));
```

The middleware compresses outgoing responses and optionally minifies HTML,
following the PSR-15 request/response flow.

```php
$middleware = new BoostMiddleware(
    minifyHtml: true,
    gzipLevel: 4,
);

$response = $middleware->handle($request, $next);
```

### Options

| Option | Default | Meaning |
|---|---|---|
| `minifyHtml` | `true` | Minify HTML responses before sending |
| `gzipLevel` | `4` | Compression level, 1 (fastest) – 9 (smallest) |

Set `minifyHtml` to `false` when responses already arrive minified, or when
the body is not HTML at all — re-minifying JSON or a binary stream wastes CPU
and can corrupt payloads that are not markup.

## Response cache, Bloom filter, circuit breaker

```php
use B4N1\Boost\ResponseCache;
use B4N1\Boost\BloomFilter;
use B4N1\Boost\CircuitBreaker;

$cache = new ResponseCache(1024);
$cache->set('GET:/users', $body, 200, 300);
$hit = $cache->get('GET:/users');   // null on miss
$cache->close();

$bloom = new BloomFilter(10_000, 0.01);
$seen = $bloom->checkAndSet($item);
$bloom->close();

$breaker = new CircuitBreaker(5, 1, 30);
if ($breaker->allows()) { /* call upstream */ }
$breaker->close();
```

## Testing

```bash
php test.php
```

Covers the four-state matrix: valid input, invalid input, an expected entry
that must be present, and an unknown entry that must be rejected.

## See also

- [Ruby SDK](ruby.md) — the equivalent Rack integration
- [Go SDK](go.md) — the same core from Go
