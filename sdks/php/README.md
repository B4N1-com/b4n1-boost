# b4n1-boost PHP SDK

High-performance native boost layer for PHP and Laravel: gzip/zstd
compression, HTML minification and JSON validation through a bundled native
core (no compiler needed — `ext-ffi` only).

## Install

```bash
composer require b4n1/boost
```

The package ships the native core for `linux-x64`, `linux-arm64`,
`macos-x64`, `macos-arm64` and `windows-x64` under `native/<platform>/`, and
loads the correct one automatically.

## Use

```php
require 'vendor/autoload.php';

use B4N1\Boost;

$compressed = Boost::compressGzip('hello world');
$packed     = Boost::compressZstd('hello world');
$html       = Boost::minifyHtml('<p>   hi   </p>');
$valid      = Boost::isJsonValid('{"a":1}');
```

Laravel / middleware:

```php
use B4N1\Boost\BoostMiddleware;

$kernel->pushMiddleware(BoostMiddleware::class);
```

Set `B4N1_BOOST_LIB_PATH` to override the bundled native library (custom
builds or development against a local artifact).

## API

| Method | Description |
|--------|-------------|
| `Boost::compressGzip(string $data, int $level = 4): string` | gzip compression |
| `Boost::compressZstd(string $data, int $level = 3): string` | zstd compression |
| `Boost::minifyHtml(string $html): string` | HTML minification |
| `Boost::isJsonValid(string $json): bool` | fast JSON validation |
| `BoostMiddleware` | compresses + minifies responses in one drop-in |

## Test

```bash
php test.php
```

The suite exercises the real C-ABI core (no mocks).

## License

BUSL-1.1 (see LICENSE). The native binary is licensed separately under the
B4N1 EULA (see EULA.txt).
