# b4n1-boost Go SDK

High-performance native boost layer for Go: gzip/zstd compression, HTML
minification and JSON validation, backed by a bundled native core.

## Install

```bash
go get github.com/B4N1-com/b4n1-boost/sdks/go
```

The module ships the native core under `native/<platform>/` and `cgo` links
(plus `rpath`s) to that same bundled copy, so `go build` needs no external
setup.

| Platform | Bundled |
|----------|---------|
| linux-x64 | ✅ |
| linux-arm64 | ✅ |
| macos-x64 | ✅ |
| macos-arm64 | ✅ |
| windows-x64 | not yet (link flags pending) |

## Use

```go
package main

import (
	"fmt"

	boost "github.com/B4N1-com/b4n1-boost/sdks/go"
)

func main() {
	compressed, err := boost.CompressGzip([]byte("hello world"), 4)
	if err != nil {
		panic(err)
	}
	packed, _ := boost.CompressZstd([]byte("hello world"), 3)
	html := boost.MinifyHTML("<p>   hi   </p>")
	valid := boost.IsJSONValid(`{"a":1}`)

	fmt.Println(len(compressed), len(packed), html, valid)
}
```

## API

| Function | Description |
|----------|-------------|
| `CompressGzip(data []byte, level uint32) ([]byte, error)` | gzip compression |
| `CompressZstd(data []byte, level int32) ([]byte, error)` | zstd compression |
| `MinifyHTML(html string) string` | HTML minification |
| `IsJSONValid(json string) bool` | fast JSON validation |

## Test

```bash
go test ./...
```

The suite exercises the real C-ABI core (no mocks).

## License

BUSL-1.1 (see LICENSE). The native binary is licensed separately under the
B4N1 EULA (see EULA.txt).
