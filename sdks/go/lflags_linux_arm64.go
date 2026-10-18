// B4N1-Boost Go SDK — link flags for linux/arm64.
//go:build linux && arm64

package boost

// #cgo LDFLAGS: -L${SRCDIR}/native/linux-arm64 -lb4n1_boost -Wl,-rpath,${SRCDIR}/native/linux-arm64
import "C"
