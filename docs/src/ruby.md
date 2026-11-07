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
| `decompress_zstd` | `(data)` — inverse of `compress_zstd` |
| `json_valid?` | `(json)` → `true` / `false` |

The trailing `?` on `json_valid?` follows Ruby convention: the method returns
a boolean and is safe to use in a conditional.

## Response cache, Bloom filter, circuit breaker

These bind the same native core as the other SDKs (`require 'b4n1_boost'`
loads them; they live in `core.rb`):

```ruby
cache = B4N1::Boost::ResponseCache.new(1024)
cache.set('GET:/users', body, 200, 300)   # ttl_secs 0 = never expires
hit = cache.get('GET:/users')             # => { body:, status: } or nil
cache.close

bloom = B4N1::Boost::BloomFilter.new(10_000, 0.01)
already_seen = bloom.check_and_set(item)
bloom.close

breaker = B4N1::Boost::CircuitBreaker.new(5, 1, 30)
breaker.allows? ? call_upstream : fail_fast
breaker.close
```

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
