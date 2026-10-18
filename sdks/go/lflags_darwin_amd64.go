// B4N1-Boost Go SDK — link flags for darwin/amd64.
//go:build darwin && amd64

package boost

// #cgo LDFLAGS: -L${SRCDIR}/native/macos-x64 -lb4n1_boost -Wl,-rpath,${SRCDIR}/native/macos-x64
import "C"
