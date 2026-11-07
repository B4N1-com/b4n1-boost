# Go SDK

A small, dependency-free wrapper over the shared native core.

```go
import "github.com/B4N1-com/b4n1-boost/sdks/go"
```

## API

Four functions, all in the package root:

```go
package main

import (
    "fmt"

    boost "github.com/B4N1-com/b4n1-boost/sdks/go"
)

func main() {
    gz, err := boost.CompressGzip(data, 4)
    if err != nil {
        // handle
    }

    zst, err := boost.CompressZstd(data, 3)
    if err != nil {
        // handle
    }

    html := boost.MinifyHTML(rawHTML)

    ok := boost.IsJSONValid(body)
    fmt.Println(ok)
}
```

| Function | Signature |
|---|---|
| `CompressGzip` | `(data []byte, level uint32) ([]byte, error)` |
| `CompressZstd` | `(data []byte, level int32) ([]byte, error)` |
| `DecompressZstd` | `(data []byte) ([]byte, error)` |
| `MinifyHTML` | `(htmlStr string) string` |
| `IsJSONValid` | `(jsonStr string) bool` |

### Error handling

Both compression functions return `([]byte, error)` rather than panicking.
A failure inside the native core — an invalid level, an allocation problem —
surfaces as an ordinary Go error, so callers can handle it without recovering
from a panic.

`MinifyHTML` and `IsJSONValid` return values directly because they have no
meaningful failure mode at this layer: an unminifiable document returns
unchanged, and an invalid JSON string returns `false`.

### Levels

| Function | Default / typical level |
|---|---|
| `CompressGzip` | `4` |
| `CompressZstd` | `3` |

Levels outside the valid range produce an error rather than being clamped
silently — a caller who asks for level `99` has a bug worth surfacing.

## Response cache, Bloom filter, circuit breaker

The primitives live in `core.go` and bind the same native core as the other
SDKs. Every handle is a file descriptor-like resource: close it.

```go
cache, err := boost.NewResponseCache(1024)
if err != nil { /* handle */ }
_ = cache.Set("GET:/users", body, 200, 300)   // ttlSecs 0 = never expires
hit, ok := cache.Get("GET:/users")
cache.Close()

bloom, err := boost.NewBloomFilter(10_000, 0.01)
seen := bloom.CheckAndSet(item)
bloom.Close()

breaker, err := boost.NewCircuitBreaker(5, 1, 30)
if breaker.Allows() { /* call upstream */ }
breaker.Close()
```

## Testing

```bash
go test ./...
```

The test file encodes the four-state matrix as `TestState1ExistsAndCorrect`,
`TestState2ExistsAndIncorrect`, `TestState3ShouldExistAndMissing` and
`TestState4ShouldNotExistAndCorrectlyAbsent`, so a regression in any of the
four shows up by name.

## Design notes

- **Plain Go types at the boundary.** Callers work with ordinary `[]byte`
  and `string` values; marshalling happens inside the wrapper.
- **No hidden global state.** Each call is independent, so the package is
  safe for concurrent use from multiple goroutines.
- **Errors, not panics.** Native failures become Go errors.

## See also

- [PHP SDK](php.md) and [Ruby SDK](ruby.md) — the other thin wrappers
- [Status & Diagnostics](status.md) — verifying the core loaded
