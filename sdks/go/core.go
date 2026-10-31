// B4N1-Boost Go SDK — core primitives: response cache, bloom filter,
// circuit breaker. Business Source License 1.1 (BUSL-1.1).
// Thin FFI wrapper over the proprietary B4N1 native core. ALL logic (LRU
// eviction, TTL, bloom hashing, circuit thresholds) lives in the native core
// and is shared with Python, Node.js, .NET and Java through the same C-ABI.
// The native binary is licensed separately under the B4N1 EULA (EULA.txt).
// Copyright (c) 2026 B4N1. All rights reserved.
package boost

/*
#include <stdlib.h>
#include <stdint.h>

// NOTE: b4n1_boost_free_buffer is already declared in boost.go's preamble;
// cgo merges all preambles of the package into one translation unit, so
// re-declaring it here would be an "inconsistent definitions" build error.
uint64_t b4n1_cache_new(int32_t capacity);
int32_t b4n1_cache_get(uint64_t handle, const char* key, uint8_t** out_body, size_t* out_len, uint16_t* out_status);
int32_t b4n1_cache_set(uint64_t handle, const char* key, const char* body, size_t len, uint16_t status, uint64_t ttl_secs);
int32_t b4n1_cache_invalidate(uint64_t handle, const char* key);
void b4n1_cache_clear(uint64_t handle);
void b4n1_cache_free(uint64_t handle);
uint64_t b4n1_bloom_new(uint64_t expected_items, uint64_t fp_rate_bits);
int32_t b4n1_bloom_check_and_set(uint64_t handle, const char* item);
void b4n1_bloom_free(uint64_t handle);
uint64_t b4n1_circuit_new(int32_t threshold, int32_t success_threshold, uint64_t timeout_secs);
int32_t b4n1_circuit_allows(uint64_t handle);
void b4n1_circuit_record_success(uint64_t handle);
void b4n1_circuit_record_failure(uint64_t handle);
void b4n1_circuit_free(uint64_t handle);
*/
import "C"
import (
	"errors"
	"math"
	"unsafe"
)

// CachedResponse is a cache hit: the body bytes (already copied out of
// native memory) and the stored HTTP status.
type CachedResponse struct {
	Body   []byte
	Status uint16
}

// ResponseCache is an LRU + TTL response cache backed by the native core.
type ResponseCache struct {
	handle uint64
}

// NewResponseCache creates a cache holding up to capacity entries (LRU
// eviction). An out-of-bounds capacity (max 1,000,000) is an error, never a
// silent clamp: the core preallocates and would abort on absurd values.
func NewResponseCache(capacity int) (*ResponseCache, error) {
	h := C.b4n1_cache_new(C.int(capacity))
	if uint64(h) == 0 {
		return nil, errors.New("b4n1-boost: response cache capacity out of bounds (max 1000000)")
	}
	return &ResponseCache{handle: uint64(h)}, nil
}

// Get looks up a key. ok is false on a miss (or on a stale/closed handle).
func (c *ResponseCache) Get(key string) (*CachedResponse, bool) {
	if c == nil || c.handle == 0 {
		return nil, false
	}
	cKey := C.CString(key)
	defer C.free(unsafe.Pointer(cKey))
	var outPtr *C.uint8_t
	var outLen C.size_t
	var outStatus C.uint16_t
	if C.b4n1_cache_get(C.uint64_t(c.handle), cKey, &outPtr, &outLen, &outStatus) != 1 {
		return nil, false
	}
	// Copy before releasing: the core owns that buffer.
	body := C.GoBytes(unsafe.Pointer(outPtr), C.int(outLen))
	freeBuffer(outPtr, outLen)
	return &CachedResponse{Body: body, Status: uint16(outStatus)}, true
}

// Set stores a response. ttlSecs == 0 means never expires.
func (c *ResponseCache) Set(key string, body []byte, status uint16, ttlSecs uint64) error {
	if c == nil || c.handle == 0 {
		return errors.New("b4n1-boost: cache handle is closed")
	}
	cKey := C.CString(key)
	defer C.free(unsafe.Pointer(cKey))
	var bodyPtr *C.uint8_t
	if len(body) > 0 {
		bodyPtr = (*C.uint8_t)(unsafe.Pointer(&body[0]))
	}
	if rc := C.b4n1_cache_set(C.uint64_t(c.handle), cKey, (*C.char)(unsafe.Pointer(bodyPtr)), C.size_t(len(body)), C.uint16_t(status), C.uint64_t(ttlSecs)); rc != 0 {
		return errors.New("b4n1-boost: cache set failed (stale handle?)")
	}
	return nil
}

// Invalidate removes a key; true when it existed.
func (c *ResponseCache) Invalidate(key string) bool {
	if c == nil || c.handle == 0 {
		return false
	}
	cKey := C.CString(key)
	defer C.free(unsafe.Pointer(cKey))
	return C.b4n1_cache_invalidate(C.uint64_t(c.handle), cKey) == 1
}

// Clear drops every entry.
func (c *ResponseCache) Clear() {
	if c == nil || c.handle == 0 {
		return
	}
	C.b4n1_cache_clear(C.uint64_t(c.handle))
}

// Close releases the cache. Idempotent; further use is declined.
func (c *ResponseCache) Close() {
	if c == nil || c.handle == 0 {
		return
	}
	C.b4n1_cache_free(C.uint64_t(c.handle))
	c.handle = 0
}

// BloomFilter is a probabilistic set for rate limiting / dedup.
type BloomFilter struct {
	handle uint64
}

// NewBloomFilter sizes the filter for expectedItems at fpRate false-positive
// rate (the core clamps the rate and rejects counts above 10,000,000).
func NewBloomFilter(expectedItems uint64, fpRate float64) (*BloomFilter, error) {
	h := C.b4n1_bloom_new(C.uint64_t(expectedItems), C.uint64_t(math.Float64bits(fpRate)))
	if uint64(h) == 0 {
		return nil, errors.New("b4n1-boost: bloom expected items out of bounds (max 10000000)")
	}
	return &BloomFilter{handle: uint64(h)}, nil
}

// CheckAndSet records the item; true when it was ALREADY present (duplicate).
func (b *BloomFilter) CheckAndSet(item string) bool {
	if b == nil || b.handle == 0 {
		return false
	}
	cItem := C.CString(item)
	defer C.free(unsafe.Pointer(cItem))
	return C.b4n1_bloom_check_and_set(C.uint64_t(b.handle), cItem) == 1
}

// Close releases the filter. Idempotent.
func (b *BloomFilter) Close() {
	if b == nil || b.handle == 0 {
		return
	}
	C.b4n1_bloom_free(C.uint64_t(b.handle))
	b.handle = 0
}

// CircuitBreaker fails closed: Allows() is false while the circuit is open
// and for any closed (freed) breaker.
type CircuitBreaker struct {
	handle uint64
}

// NewCircuitBreaker opens the circuit after threshold consecutive failures;
// it closes again after successThreshold successes once timeoutSecs passed.
func NewCircuitBreaker(threshold, successThreshold int, timeoutSecs uint64) (*CircuitBreaker, error) {
	h := C.b4n1_circuit_new(C.int(threshold), C.int(successThreshold), C.uint64_t(timeoutSecs))
	if uint64(h) == 0 {
		return nil, errors.New("b4n1-boost: circuit breaker handle invalid")
	}
	return &CircuitBreaker{handle: uint64(h)}, nil
}

// Allows reports whether a call may go through. A closed breaker must fail
// CLOSED, never resurrect through the C-ABI's 0-handle legacy path.
func (cb *CircuitBreaker) Allows() bool {
	if cb == nil || cb.handle == 0 {
		return false
	}
	return C.b4n1_circuit_allows(C.uint64_t(cb.handle)) == 1
}

// RecordSuccess counts a good call.
func (cb *CircuitBreaker) RecordSuccess() {
	if cb == nil || cb.handle == 0 {
		return
	}
	C.b4n1_circuit_record_success(C.uint64_t(cb.handle))
}

// RecordFailure counts a bad call.
func (cb *CircuitBreaker) RecordFailure() {
	if cb == nil || cb.handle == 0 {
		return
	}
	C.b4n1_circuit_record_failure(C.uint64_t(cb.handle))
}

// Close releases the breaker. Idempotent.
func (cb *CircuitBreaker) Close() {
	if cb == nil || cb.handle == 0 {
		return
	}
	C.b4n1_circuit_free(C.uint64_t(cb.handle))
	cb.handle = 0
}
