// B4N1-Boost Go SDK — link flags for linux/amd64.
// The native core ships bundled inside the module (native/<platform>/) so
// `go get` + `go build` needs no external setup. rpath makes the resulting
// binary find the same bundled copy at runtime.
//go:build linux && amd64

package boost

// #cgo LDFLAGS: -L${SRCDIR}/native/linux-x64 -lb4n1_boost -Wl,-rpath,${SRCDIR}/native/linux-x64
import "C"
