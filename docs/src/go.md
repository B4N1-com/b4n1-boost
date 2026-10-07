# Go SDK

A small, dependency-free wrapper over the shared native core.

```go
import "github.com/B4N1-com/b4n1-boost/polyglot/go"
```

## API

Four functions, all in the package root:

```go
package main

import (
    "fmt"

    boost "github.com/B4N1-com/b4n1-boost/polyglot/go"
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
