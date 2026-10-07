# Java SDK

```xml
<dependency>
  <groupId>com.b4n1</groupId>
  <artifactId>boost</artifactId>
  <version>0.3.12</version>
</dependency>
```

Gradle:

```groovy
implementation 'com.b4n1:boost:0.3.12'
```

Published on Maven Central as **`com.b4n1:boost`**.

## Platform support

| Platform | Status |
|---|---|
| Linux x64 / arm64 | ✅ bundled |
| macOS x64 / arm64 | ✅ bundled |
| Windows x64 | ✅ bundled |

Native binaries ship inside the JAR under `runtimes/` and are selected at
load time from the OS and architecture.

## Loading the native library

The static initializer picks the library for you:

```java
// Explicit path (optional)
System.getenv("B4N1_BOOST_LIB_PATH");
```

When `B4N1_BOOST_LIB_PATH` is set, the file name is validated against the
three accepted names — `libb4n1_boost.so`, `libb4n1_boost.dylib`,
`b4n1_boost.dll`. Anything else is rejected with a `SecurityException`
rather than loaded. That check exists so an unexpected file cannot be
resolved into the JVM.

If the variable is unset, the library is resolved through the standard
`System.loadLibrary` search path.

## API

All methods are `static` on `com.b4n1.boost.Boost`:

```java
import com.b4n1.boost.Boost;

byte[]  gz  = Boost.compressGzip(data, 4);
byte[]  zst = Boost.compressZstd(data, 3);
byte[]  raw = Boost.decompressZstd(zst);
String  min = Boost.minifyHtml(html);
boolean ok  = Boost.isJsonValid(json);
```

| Method | Signature |
|---|---|
| `compressGzip` | `(byte[] data, int level)` → `byte[]` |
| `compressZstd` | `(byte[] data, int level)` → `byte[]` |
| `decompressZstd` | `(byte[] data)` → `byte[]` |
| `minifyHtml` | `(String html)` → `String` |
| `isJsonValid` | `(String json)` → `boolean` |

These are JNI calls: arguments are copied to native memory and results
copied back. For tight loops, prefer fewer larger calls over many small
ones — the marshalling cost per call can exceed the work for tiny payloads.

## Response cache, Bloom filter, circuit breaker

```java
import com.b4n1.boost.NativeResponseCache;
import com.b4n1.boost.NativeBloomFilter;
import com.b4n1.boost.NativeCircuitBreaker;
```

The three wrappers mirror the .NET API exactly:

```java
try (var cache = new NativeResponseCache(1024)) {
    cache.set("GET:/users", body, (short) 200, 300);
    var hit = cache.get("GET:/users");
}

try (var bloom = new NativeBloomFilter(10_000L, 0.01)) {
    boolean alreadySeen = bloom.checkAndSet(item);
}

try (var breaker = new NativeCircuitBreaker(5, 1, 30L)) {
    if (breaker.allows()) { /* call */ }
}
```

All three are `AutoCloseable`, so use try-with-resources. Without it the
native handle leaks until finalization — which may never run promptly enough
in a busy process.

## Background tasks

```java
import com.b4n1.boost.Background;

var handle = Background.run(() -> buildReport(userId), "tasks.jsonl");
var result = handle.result();
```

Passing a journal path makes submissions durable across restarts.

## Testing

```bash
mvn test
```

The suite covers the four-state matrix: valid input succeeds, invalid input
fails with a typed error, an expected entry missing is caught, and an unknown
entry is rejected.

## See also

- [.NET SDK](csharp.md) — the same wrappers for .NET
- [Status & Diagnostics](status.md) — diagnosing a failed native load
