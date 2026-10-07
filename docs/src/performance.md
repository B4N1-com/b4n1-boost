# Performance

All figures below are measured against the Python standard library on the
same machine, same input, same process. They are a starting point: your
numbers depend on payload shape, hardware and interpreter version.

## Headline numbers

| Component | Metric | Compared against |
|---|---|---|
| **JSON dumps** | **10.5x faster** | `json.dumps`, medium dicts (20 users) |
| **JSON dumps** | **8.5x faster** | `json.dumps`, large dicts (500 users) |
| **Gzip** | **1.47x faster** | `zlib` on 1 MB payloads |
| **Zstd** | **28x faster** | `gzip` on 1 MB payloads |
| **Brotli** | best ratio | 1 MB payloads |
| **DRF serializer** | **5-10x faster** | queryset → JSON |
| **Django ORM bulk insert** | **5-10x faster** | PostgreSQL COPY vs ORM path |
| **Wheel size** | ~1.4 MB | single native extension |

## Running the benchmarks yourself

```python
import b4n1_boost

report = b4n1_boost.run_benchmarks(iterations=100_000)
print(report)
```

Run it on the hardware you actually deploy on. A laptop benchmark does not
predict production throughput, and the ratio between native and stdlib paths
moves with payload size.

## What makes JSON fast

```python
from b4n1_boost import NativeJson

# Standard path — uses the fastest available backend
body = NativeJson.dumps(users)

# Direct path — skips the intermediate conversion entirely
body = NativeJson.dumps_direct(users)

# Batch: N serializations inside a single interpreter-lock acquire
bodies = NativeJson.batch_dumps([obj1, obj2, obj3])
```

`batch_dumps` is where the largest wins appear for list-shaped workloads,
because the per-call overhead that dominates small serializations is paid
once rather than N times.

## What makes compression fast

```python
from b4n1_boost import compress

wire = compress(payload, "zstd")     # 28x faster than stdlib gzip
wire = compress(payload, "gzip")     # 1.47x faster than stdlib
wire = compress(payload, "brotli")   # best ratio
```

Compression also runs **without holding the interpreter lock**, so a large
payload being compressed on a worker thread does not stall other requests.

### Choosing an algorithm

| Algorithm | Speed | Ratio | Use when |
|---|---|---|---|
| `gzip` | fast | good | widest compatibility, already-encoded responses |
| `zstd` | **fastest** | very good | API responses, JSON bodies, internal traffic |
| `brotli` | slower | **best** | static assets served from disk |

For static assets the decision is usually automatic — see
`compress_static_dir` in the [Python SDK](python.md).

## Static files

```python
from b4n1_boost import compress_static_file, compress_static_dir

compress_static_file("app/static/app.js", algorithm="zstd")
compress_static_dir("app/static/", algorithm="zstd")
```

Already-compressed formats are skipped automatically: images, video, audio,
fonts and archives are left alone, because re-compressing them costs CPU and
yields nothing.

## Measuring honestly

A few rules that keep benchmark numbers meaningful:

1. **Compare like with like.** Same payload, same machine, same process.
2. **Warm up first.** The first call pays import and allocation costs that
   do not recur.
3. **Report percentiles, not just the mean.** A 10x mean improvement with a
   worse p99 is not an improvement for a user-facing endpoint.
4. **State the payload.** "10x faster" means nothing without the size and
   shape of the input that produced it.
5. **Verify the native core loaded.** Benchmarking a fallback path measures
   the wrong thing — check `status()["native_extension"]` first.

## Next

- [Status & Diagnostics](status.md) to confirm what is actually running
- [Python SDK](python.md) for the API surface behind these numbers
