package boost

import (
	"bytes"
	"testing"
)

// ── Response cache ─────────────────────────────────────────────────────────

func TestCacheRoundTrip(t *testing.T) {
	c, err := NewResponseCache(8)
	if err != nil {
		t.Fatalf("new: %v", err)
	}
	defer c.Close()
	if err := c.Set("user:1", []byte(`{"id":1}`), 200, 60); err != nil {
		t.Fatalf("set: %v", err)
	}
	hit, ok := c.Get("user:1")
	if !ok || !bytes.Equal(hit.Body, []byte(`{"id":1}`)) || hit.Status != 200 {
		t.Fatalf("round-trip mismatch: %+v ok=%v", hit, ok)
	}
}

func TestCacheMiss(t *testing.T) {
	c, _ := NewResponseCache(8)
	defer c.Close()
	if _, ok := c.Get("nope"); ok {
		t.Fatal("expected miss")
	}
}

func TestCacheOverwrite(t *testing.T) {
	c, _ := NewResponseCache(8)
	defer c.Close()
	_ = c.Set("k", []byte("old"), 200, 60)
	_ = c.Set("k", []byte("new"), 201, 60)
	hit, ok := c.Get("k")
	if !ok || string(hit.Body) != "new" || hit.Status != 201 {
		t.Fatalf("overwrite mismatch: %+v", hit)
	}
}

func TestCacheTTLZeroNeverExpires(t *testing.T) {
	c, _ := NewResponseCache(4)
	defer c.Close()
	_ = c.Set("k", []byte("x"), 204, 0)
	if _, ok := c.Get("k"); !ok {
		t.Fatal("TTL 0 must mean never expires")
	}
}

func TestCacheLRUEviction(t *testing.T) {
	c, _ := NewResponseCache(2)
	defer c.Close()
	_ = c.Set("a", []byte("1"), 200, 60)
	_ = c.Set("b", []byte("2"), 200, 60)
	_ = c.Set("c", []byte("3"), 200, 60)
	if _, ok := c.Get("a"); ok {
		t.Fatal("oldest entry should be evicted")
	}
	if _, ok := c.Get("b"); !ok {
		t.Fatal("b should still be cached")
	}
	if _, ok := c.Get("c"); !ok {
		t.Fatal("c should still be cached")
	}
}

func TestCacheInvalidateAndClear(t *testing.T) {
	c, _ := NewResponseCache(8)
	defer c.Close()
	_ = c.Set("k", []byte("x"), 200, 60)
	if !c.Invalidate("k") {
		t.Fatal("invalidate existing should be true")
	}
	if c.Invalidate("nope") {
		t.Fatal("invalidate nonexistent should be false")
	}
	_ = c.Set("a", []byte("1"), 200, 60)
	_ = c.Set("b", []byte("2"), 200, 60)
	c.Clear()
	if _, ok := c.Get("a"); ok {
		t.Fatal("clear should remove a")
	}
	if _, ok := c.Get("b"); ok {
		t.Fatal("clear should remove b")
	}
}

func TestCacheBinaryBody(t *testing.T) {
	c, _ := NewResponseCache(8)
	defer c.Close()
	blob := []byte{0x00, 0xFF, 0x10}
	_ = c.Set("bin", blob, 200, 60)
	hit, ok := c.Get("bin")
	if !ok || !bytes.Equal(hit.Body, blob) {
		t.Fatalf("binary body mismatch: %v ok=%v", hit, ok)
	}
}

func TestCacheOversizedCapacityRejected(t *testing.T) {
	if _, err := NewResponseCache(2000000); err == nil {
		t.Fatal("capacity over max must be an error")
	}
}

func TestCacheGetAfterCloseDeclined(t *testing.T) {
	c, _ := NewResponseCache(8)
	_ = c.Set("k", []byte("x"), 200, 60)
	c.Close()
	c.Close() // idempotent
	if _, ok := c.Get("k"); ok {
		t.Fatal("use after close must be declined")
	}
}

// ── Bloom filter ───────────────────────────────────────────────────────────

func TestBloomDuplicates(t *testing.T) {
	b, _ := NewBloomFilter(1000, 0.01)
	defer b.Close()
	if b.CheckAndSet("user-1") {
		t.Fatal("first sight must be new (false)")
	}
	if !b.CheckAndSet("user-1") {
		t.Fatal("second sight must be duplicate (true)")
	}
}

func TestBloomIndependentItems(t *testing.T) {
	b, _ := NewBloomFilter(1000, 0.01)
	defer b.Close()
	if b.CheckAndSet("a") || b.CheckAndSet("b") {
		t.Fatal("distinct items must be new")
	}
	if !b.CheckAndSet("a") {
		t.Fatal("a must now be a duplicate")
	}
}

func TestBloomOversizedRejected(t *testing.T) {
	if _, err := NewBloomFilter(20000000, 0.01); err == nil {
		t.Fatal("items over max must be an error")
	}
}

func TestBloomAfterCloseDeclined(t *testing.T) {
	b, _ := NewBloomFilter(1000, 0.01)
	b.Close()
	b.Close() // idempotent
	if b.CheckAndSet("x") {
		t.Fatal("use after close must be declined")
	}
}

// ── Circuit breaker ────────────────────────────────────────────────────────

func TestCircuitLifecycle(t *testing.T) {
	cb, _ := NewCircuitBreaker(2, 1, 60)
	defer cb.Close()
	if !cb.Allows() {
		t.Fatal("fresh breaker must be closed (allows)")
	}
	cb.RecordFailure()
	if !cb.Allows() {
		t.Fatal("one failure must stay closed")
	}
	cb.RecordFailure()
	if cb.Allows() {
		t.Fatal("breaker must open at threshold")
	}
}

func TestCircuitSuccessKeepsClosed(t *testing.T) {
	cb, _ := NewCircuitBreaker(2, 1, 60)
	defer cb.Close()
	cb.RecordSuccess()
	cb.RecordSuccess()
	cb.RecordFailure()
	if !cb.Allows() {
		t.Fatal("successes must keep the circuit closed")
	}
}

func TestCircuitFailsClosedAfterClose(t *testing.T) {
	cb, _ := NewCircuitBreaker(2, 1, 60)
	cb.Close()
	cb.Close() // idempotent
	if cb.Allows() {
		t.Fatal("a closed breaker must fail CLOSED")
	}
}
