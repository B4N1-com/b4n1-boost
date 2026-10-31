<?php

// B4N1-Boost PHP SDK — core primitives: response cache, bloom filter,
// circuit breaker. Business Source License 1.1 (BUSL-1.1).
// Thin FFI wrapper over the proprietary B4N1 native core. ALL logic (LRU
// eviction, TTL, bloom hashing, circuit thresholds) lives in the native core
// and is shared with Python, Node.js, .NET and Java through the same C-ABI.
// The native binary is licensed separately under the B4N1 EULA (EULA.txt).
// Copyright (c) 2026 B4N1. All rights reserved.

namespace B4N1\Boost;

final class ResponseCache {
    private int $handle = 0;
    private \FFI\CData $outPtr;
    private \FFI\CData $outLen;
    private \FFI\CData $outStatus;

    public function __construct(int $capacity = 1024) {
        $h = \B4N1\Boost::ffi()->b4n1_cache_new($capacity);
        if ($h === 0) {
            throw new \InvalidArgumentException('Response cache capacity out of bounds (max 1000000)');
        }
        $this->handle = (int) $h;
        $ffi = \B4N1\Boost::ffi();
        $this->outPtr = $ffi->new('uint8_t*');
        $this->outLen = $ffi->new('size_t');
        $this->outStatus = $ffi->new('uint16_t');
    }

    /** @return array{body: string, status: int}|null null on a miss. */
    public function get(string $key): ?array {
        $hit = \B4N1\Boost::ffi()->b4n1_cache_get(
            $this->handle, $key,
            \FFI::addr($this->outPtr), \FFI::addr($this->outLen), \FFI::addr($this->outStatus)
        );
        if ($hit !== 1) return null;
        // Copy before releasing: the core owns that buffer.
        $body = \FFI::string($this->outPtr, $this->outLen->cdata);
        \B4N1\Boost::ffi()->b4n1_boost_free_buffer($this->outPtr, $this->outLen->cdata);
        return ['body' => $body, 'status' => $this->outStatus->cdata];
    }

    /** ttlSecs == 0 means never expires (core semantics, matches Node). */
    public function set(string $key, string $body, int $status = 200, int $ttlSecs = 300): void {
        $rc = \B4N1\Boost::ffi()->b4n1_cache_set(
            $this->handle, $key, $body === '' ? null : $body, strlen($body), $status, $ttlSecs
        );
        if ($rc !== 0) throw new \RuntimeException('Response cache set failed (stale handle?)');
    }

    /** True when the key existed and was removed. */
    public function invalidate(string $key): bool {
        return \B4N1\Boost::ffi()->b4n1_cache_invalidate($this->handle, $key) === 1;
    }

    public function clear(): void {
        \B4N1\Boost::ffi()->b4n1_cache_clear($this->handle);
    }

    public function close(): void {
        if ($this->handle === 0) return;
        \B4N1\Boost::ffi()->b4n1_cache_free($this->handle);
        $this->handle = 0;
    }

    public function __destruct() {
        $this->close();
    }
}

final class BloomFilter {
    private int $handle = 0;

    public function __construct(int $expectedItems = 10000, float $fpRate = 0.01) {
        // The core reads the double from its u64 bit pattern.
        $bits = unpack('Q', pack('d', $fpRate))[1];
        $h = \B4N1\Boost::ffi()->b4n1_bloom_new($expectedItems, $bits);
        if ($h === 0) {
            throw new \InvalidArgumentException('Bloom expected items out of bounds (max 10000000)');
        }
        $this->handle = (int) $h;
    }

    /** True when the item was already present (duplicate). */
    public function checkAndSet(string $item): bool {
        return \B4N1\Boost::ffi()->b4n1_bloom_check_and_set($this->handle, $item) === 1;
    }

    public function close(): void {
        if ($this->handle === 0) return;
        \B4N1\Boost::ffi()->b4n1_bloom_free($this->handle);
        $this->handle = 0;
    }

    public function __destruct() {
        $this->close();
    }
}

final class CircuitBreaker {
    private int $handle = 0;

    public function __construct(int $threshold = 5, int $successThreshold = 1, int $timeoutSecs = 30) {
        $h = \B4N1\Boost::ffi()->b4n1_circuit_new($threshold, $successThreshold, $timeoutSecs);
        if ($h === 0) throw new \RuntimeException('Circuit breaker handle invalid');
        $this->handle = (int) $h;
    }

    /** False when calls must NOT go through (open, or the breaker was closed). */
    public function allows(): bool {
        if ($this->handle === 0) return false;
        return \B4N1\Boost::ffi()->b4n1_circuit_allows($this->handle) === 1;
    }

    public function recordSuccess(): void {
        \B4N1\Boost::ffi()->b4n1_circuit_record_success($this->handle);
    }

    public function recordFailure(): void {
        \B4N1\Boost::ffi()->b4n1_circuit_record_failure($this->handle);
    }

    public function close(): void {
        if ($this->handle === 0) return;
        \B4N1\Boost::ffi()->b4n1_circuit_free($this->handle);
        $this->handle = 0;
    }

    public function __destruct() {
        $this->close();
    }
}
