# PHP SDK

```bash
composer require b4n1/boost
```

## API

Static methods on the `Boost` class:

```php
use B4N1\Boost\Boost;

$gz   = Boost::compressGzip($data, 4);
$zst  = Boost::compressZstd($data, 3);
$html = Boost::minifyHtml($rawHtml);
$ok   = Boost::isJsonValid($json);
```

| Method | Signature |
|---|---|
| `compressGzip` | `(string $data, int $level = 4): string` |
| `compressZstd` | `(string $data, int $level = 3): string` |
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

## Testing

```bash
php test.php
```

Covers the four-state matrix: valid input, invalid input, an expected entry
that must be present, and an unknown entry that must be rejected.

## See also

- [Ruby SDK](ruby.md) — the equivalent Rack integration
- [Go SDK](go.md) — the same core from Go
