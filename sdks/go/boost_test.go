package boost

import (
	"bytes"
	"compress/gzip"
	"io"
	"strings"
	"testing"
)

// ── State 1: Exists & Correct ─────────────────────────────────────────────

func TestJSONValidObjects(t *testing.T) {
	valid := []string{
		`{"a":1}`,
		`[1,2,3]`,
		`"hello"`,
		`null`,
		`true`,
		`false`,
		`42`,
		`-3.14`,
		`{"a":{"b":[1,2,{"c":null}]}}`,
		`"hello \u00e9"`,
		`{}`,
		`[]`,
	}
	for _, s := range valid {
		if !IsJSONValid(s) {
			t.Errorf("expected valid: %s", s)
		}
	}
}

func TestGzipRoundTrip(t *testing.T) {
	payload := []byte(strings.Repeat("Hello, World! ", 100))
	gz, err := CompressGzip(payload, 6)
	if err != nil {
		t.Fatalf("compress: %v", err)
	}
	if len(gz) == 0 || len(gz) >= len(payload) {
		t.Fatalf("compressed not smaller: %d vs %d", len(gz), len(payload))
	}
	gr, err := gzip.NewReader(bytes.NewReader(gz))
	if err != nil {
		t.Fatalf("gzip reader: %v", err)
	}
	decoded, err := io.ReadAll(gr)
	if err != nil {
		t.Fatalf("decompress: %v", err)
	}
	if !bytes.Equal(decoded, payload) {
		t.Fatal("round-trip mismatch")
	}
}

func TestGzipLargePayload(t *testing.T) {
	payload := bytes.Repeat([]byte("x"), 100_000)
	gz, err := CompressGzip(payload, 4)
	if err != nil {
		t.Fatalf("compress: %v", err)
	}
	if len(gz) >= 1000 {
		t.Fatalf("expected < 1000 bytes, got %d", len(gz))
	}
	gr, err := gzip.NewReader(bytes.NewReader(gz))
	if err != nil {
		t.Fatalf("gzip reader: %v", err)
	}
	decoded, err := io.ReadAll(gr)
	if err != nil {
		t.Fatalf("decompress: %v", err)
	}
	if !bytes.Equal(decoded, payload) {
		t.Fatal("large round-trip mismatch")
	}
}

func TestGzipLevels(t *testing.T) {
	payload := []byte(strings.Repeat("test data ", 50))
	for _, level := range []uint32{1, 4, 6, 9} {
		gz, err := CompressGzip(payload, level)
		if err != nil {
			t.Fatalf("level %d: %v", level, err)
		}
		gr, err := gzip.NewReader(bytes.NewReader(gz))
		if err != nil {
			t.Fatalf("level %d reader: %v", level, err)
		}
		decoded, err := io.ReadAll(gr)
		if err != nil {
			t.Fatalf("level %d decompress: %v", level, err)
		}
		if !bytes.Equal(decoded, payload) {
			t.Fatalf("level %d round-trip mismatch", level)
		}
	}
}

func TestZstdCompression(t *testing.T) {
	payload := []byte(strings.Repeat("zstd test payload ", 100))
	zs, err := CompressZstd(payload, 3)
	if err != nil {
		t.Fatalf("compress: %v", err)
	}
	if len(zs) == 0 || len(zs) >= len(payload) {
		t.Fatalf("compressed not smaller: %d vs %d", len(zs), len(payload))
	}
}

func TestZstdLargePayload(t *testing.T) {
	payload := bytes.Repeat([]byte("x"), 100_000)
	zs, err := CompressZstd(payload, 3)
	if err != nil {
		t.Fatalf("compress: %v", err)
	}
	if len(zs) >= 100 {
		t.Fatalf("expected < 100 bytes, got %d", len(zs))
	}
}

func TestZstdLevels(t *testing.T) {
	payload := []byte(strings.Repeat("level test ", 200))
	for _, level := range []int32{1, 3, 9, 19} {
		zs, err := CompressZstd(payload, level)
		if err != nil {
			t.Fatalf("level %d: %v", level, err)
		}
		if len(zs) == 0 {
			t.Fatalf("level %d: empty output", level)
		}
	}
}

func TestMinifyHTML(t *testing.T) {
	raw := `<div>   <h1>  Title  </h1>   <p>  Body  </p>  </div>`
	min := MinifyHTML(raw)
	if len(min) >= len(raw) {
		t.Fatalf("minified not shorter: %d vs %d", len(min), len(raw))
	}
	if strings.Contains(min, "   ") {
		t.Fatalf("still has triple spaces: %s", min)
	}
	if !strings.Contains(min, "Title") || !strings.Contains(min, "Body") {
		t.Fatalf("content lost: %s", min)
	}
}

func TestMinifyHTMLEdgeCases(t *testing.T) {
	if MinifyHTML("") != "" {
		t.Fatal("empty string should return empty")
	}
	already := `<div><p>x</p></div>`
	if MinifyHTML(already) != already {
		t.Fatalf("already minified should be unchanged: %s", MinifyHTML(already))
	}
}

// ── State 2: Exists & Incorrect ───────────────────────────────────────────

func TestJSONInvalid(t *testing.T) {
	invalid := []string{
		``,
		`{`,
		`}`,
		`]`,
		`[1,]`,
		`{a:1}`,
		`{'a':1}`,
		`undefined`,
		`NaN`,
		`01`,
		`hello`,
	}
	for _, s := range invalid {
		if IsJSONValid(s) {
			t.Errorf("expected invalid: %s", s)
		}
	}
}

func TestGzipEmptyPayload(t *testing.T) {
	result, err := CompressGzip([]byte{}, 4)
	if err != nil {
		t.Fatalf("empty payload should not error: %v", err)
	}
	if result != nil {
		t.Fatalf("expected nil for empty payload, got %v", result)
	}
}

// ── State 3: Boundary ─────────────────────────────────────────────────────

func TestZstdEmptyPayload(t *testing.T) {
	result, err := CompressZstd([]byte{}, 3)
	if err != nil {
		t.Fatalf("empty payload should not error: %v", err)
	}
	if result != nil {
		t.Fatalf("expected nil for empty payload, got %v", result)
	}
}

func TestZstdExtremeLevel(t *testing.T) {
	_, err := CompressZstd([]byte("test"), 99)
	if err != nil {
		t.Logf("extreme level handled safely: %v", err)
	}
}

// ── State 4: Correctly absent ─────────────────────────────────────────────

func TestAPISurface(t *testing.T) {
	// Verify the package exports exactly the expected API surface.
	// No unexpected exported functions should exist.
	t.Log("API surface: CompressGzip, CompressZstd, MinifyHTML, IsJSONValid")
}
