// B4N1-Boost Go SDK — link flags for darwin/arm64.
//go:build darwin && arm64

package boost

// #cgo LDFLAGS: -L${SRCDIR}/native/macos-arm64 -lb4n1_boost -Wl,-rpath,${SRCDIR}/native/macos-arm64
import "C"
