# .NET SDK

```bash
dotnet add package B4N1.Boost
```

Package ID: **`B4N1.Boost`** · NuGet.

## Platform support

Native binaries are bundled for every supported runtime:

| Runtime identifier | Status |
|---|---|
| `linux-x64` | ✅ included |
| `linux-arm64` | ✅ included |
| `osx-x64` | ✅ included |
| `osx-arm64` | ✅ included |
| `win-x64` | ✅ included |

## Compression

```csharp
using B4N1.Boost;

byte[] gz  = NativeBoost.CompressGzipManaged(data, level: 4);
byte[] zst = NativeBoost.CompressZstdManaged(data, level: 3);
```

The `Managed` overloads take and return plain `byte[]` and handle allocation
and freeing for you. The raw `CompressGzip` / `CompressZstd` P/Invoke
signatures are also available if you are working with pinned buffers.

```csharp
string compact = NativeBoost.MinifyHtmlManaged(html);
bool   ok      = NativeBoost.IsJsonValidManaged(json);
```

## Response cache

```csharp
using var cache = new NativeResponseCache(capacity: 1024);

cache.Set("GET:/users", body, status: 200, ttlSeconds: 300);

if (cache.Get("GET:/users") is (byte[] hit, ushort status))
{
    // serve directly
}
```

`capacity` is a hard bound — the cache never grows past it. `Invalidate(key)`
removes a single entry, `Clear()` drops everything, and `Dispose()` releases
the native handle.

```csharp
cache.Invalidate("GET:/users");
cache.Clear();
```

Because the type implements `IDisposable`, prefer `using` or an explicit
`Dispose()`. Leaked handles keep native memory alive past the request.

## Bloom filter

```csharp
using var bloom = new NativeBloomFilter(expectedItems: 10_000, fpRate: 0.01);

if (!bloom.CheckAndSet(item))
{
    // first time we have seen this item
}
```

`CheckAndSet` returns `true` if the item was **already** present, `false` if
it was absent and has now been recorded. Size the filter with
`expectedItems` up front: a filter sized for 100 items will produce false
positives quickly under a real workload.

A Bloom filter can report that an item is present when it is not. It never
reports an absent item as present. Use it to skip expensive work, not to
decide correctness on its own.

## Circuit breaker

```csharp
using var breaker = new NativeCircuitBreaker(
    threshold: 5, successThreshold: 1, timeoutSeconds: 30);

if (breaker.Allows)
{
    try { CallDependency(); breaker.RecordSuccess(); }
    catch { breaker.RecordFailure(); }
}
```

After `threshold` consecutive failures the breaker stops allowing calls for
`timeoutSeconds`. A success during the half-open probe reopens it.

## Background tasks

```csharp
var handle = Background.Run(() => BuildReport(userId), journal: "tasks.jsonl");

var result = handle.Result();          // blocking
var task    = handle.AsTask();         // or await it
```

Passing a `journal` path makes each submission durable across restarts.
`Background.PendingTasks(journal)` returns what was interrupted, for replay.

## ASP.NET middleware

```csharp
app.UseMiddleware<BoostMiddleware>();
```

Applies compression and optional HTML minification. Constructor options:
`minifyHtml` (default `true`) and `gzipLevel` (default `4`).

## Unload safety

Cache, Bloom filter and circuit breaker wrappers own native handles. Always
dispose them — a long-running process that creates and abandons them will
grow its native memory without bound.

## See also

- [Status & Diagnostics](status.md) — verifying the native core
- [Background Tasks](background.md) — the shared task model
