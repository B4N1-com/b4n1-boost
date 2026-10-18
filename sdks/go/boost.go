// B4N1-Boost Go SDK — Business Source License 1.1 (BUSL-1.1).
// Thin FFI wrapper over the proprietary B4N1 native core.
// The native binary is licensed separately under the B4N1 EULA (EULA.txt).
// Copyright (c) 2026 B4N1. All rights reserved.
package boost

/*
#include <stdlib.h>
#include <stdint.h>

int32_t b4n1_boost_compress_gzip(const uint8_t* data, size_t len, uint8_t** out_ptr, size_t* out_len, uint32_t level);
int32_t b4n1_boost_compress_zstd(const uint8_t* data, size_t len, uint8_t** out_ptr, size_t* out_len, int32_t level);
int32_t b4n1_boost_decompress_zstd(const uint8_t* data, size_t len, uint8_t** out_ptr, size_t* out_len);
void b4n1_boost_free_buffer(uint8_t* ptr, size_t len);
char* b4n1_boost_minify_html(const char* input);
int32_t b4n1_boost_json_validate(const char* input);
void b4n1_boost_free_string(char* ptr);
*/
import "C"
import (
	"errors"
	"unsafe"
)

// CompressGzip compresses byte slice using Rust flate2 engine
func CompressGzip(data []byte, level uint32) ([]byte, error) {
	if len(data) == 0 {
		return nil, nil
	}
	var outPtr *C.uint8_t
	var outLen C.size_t

	res := C.b4n1_boost_compress_gzip(
		(*C.uint8_t)(unsafe.Pointer(&data[0])),
		C.size_t(len(data)),
		&outPtr,
		&outLen,
		C.uint32_t(level),
	)
	if res != 0 {
		return nil, errors.New("b4n1-boost gzip compression failed")
	}
	defer C.b4n1_boost_free_buffer(outPtr, outLen)

	output := C.GoBytes(unsafe.Pointer(outPtr), C.int(outLen))
	return output, nil
}

// CompressZstd compresses byte slice using Rust zstd engine
func CompressZstd(data []byte, level int32) ([]byte, error) {
	if len(data) == 0 {
		return nil, nil
	}
	var outPtr *C.uint8_t
	var outLen C.size_t

	res := C.b4n1_boost_compress_zstd(
		(*C.uint8_t)(unsafe.Pointer(&data[0])),
		C.size_t(len(data)),
		&outPtr,
		&outLen,
		C.int32_t(level),
	)
	if res != 0 {
		return nil, errors.New("b4n1-boost zstd compression failed")
	}
	defer C.b4n1_boost_free_buffer(outPtr, outLen)

	output := C.GoBytes(unsafe.Pointer(outPtr), C.int(outLen))
	return output, nil
}

// MinifyHTML minifies raw HTML string
func MinifyHTML(htmlStr string) string {
	cStr := C.CString(htmlStr)
	defer C.free(unsafe.Pointer(cStr))

	outStr := C.b4n1_boost_minify_html(cStr)
	if outStr == nil {
		return htmlStr
	}
	defer C.b4n1_boost_free_string(outStr)

	return C.GoString(outStr)
}

// IsJSONValid validates JSON string using Rust engine
func IsJSONValid(jsonStr string) bool {
	cStr := C.CString(jsonStr)
	defer C.free(unsafe.Pointer(cStr))

	res := C.b4n1_boost_json_validate(cStr)
	return res == 1
}
