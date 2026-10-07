# Ruby SDK

```bash
gem install b4n1-boost
```

## API

Class methods under the `B4N1` module namespace:

```ruby
require 'b4n1_boost'

gz   = B4N1::Boost.compress_gzip(data, level: 4)
zst  = B4N1::Boost.compress_zstd(data, level: 3)
html = B4N1::Boost.minify_html(raw_html)
ok   = B4N1::Boost.json_valid?(json)
```

| Method | Signature |
|---|---|
| `compress_gzip` | `(data, level: 4)` |
| `compress_zstd` | `(data, level: 3)` |
| `minify_html` | `(html)` |
| `json_valid?` | `(json)` → `true` / `false` |

The trailing `?` on `json_valid?` follows Ruby convention: the method returns
a boolean and is safe to use in a conditional.

## Rack middleware

```ruby
require 'b4n1_boost/rack'

use B4N1::Boost::RackMiddleware
run MyApp
```

Insert it with `use` rather than wrapping the application manually — Rack
orders middleware outermost-first, and compression belongs near the outside
of the stack so it applies to everything below it.

```ruby
use B4N1::Boost::RackMiddleware, minify_html: true, gzip_level: 4
```

| Option | Default | Meaning |
|---|---|---|
| `minify_html` | `true` | Minify HTML responses before sending |
| `gzip_level` | `4` | Compression level, 1 (fastest) – 9 (smallest) |

Turn `minify_html` off for non-HTML responses; minifying something that is
not markup wastes CPU and gains nothing.

## Concurrency

Each call is independent and holds no shared mutable state, so it is safe to
call from multiple threads. Nothing needs a global lock around it.

## Testing

```bash
ruby test.rb
```

Covers the four-state matrix: valid input, invalid input, an expected entry
that must be present, and an unknown entry that must be rejected.

## See also

- [PHP SDK](php.md) — the equivalent Composer integration
- [Middleware Reference](middleware.md) — the Python middleware stack
