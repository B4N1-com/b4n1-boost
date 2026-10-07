# Node.js SDK

```bash
npm install b4n1-boost
```

```js
const B4N1Boost = require('b4n1-boost');
```

## Platform support

| Platform | Status |
|---|---|
| linux-x64, linux-arm64 | native included |
| macos-x64, macos-arm64 | native included |
| windows-x64 | native included |
| anything else | pure-JS fallback (slower, same API) |

The native core is bundled inside the package. There is no post-install
download and no compiler requirement.

## Checking that the native core loaded

```js
B4N1Boost.isAvailable();   // true only when genuinely bound, not a fallback
B4N1Boost.libraryPath();   // absolute path of the binary actually loaded
```

`isAvailable()` is the JavaScript equivalent of Python's
`status()["native_extension"]`. Check it before you benchmark anything.

## API

### `compressGzip(buffer, level = 4)`

```js
const gz = B4N1Boost.compressGzip(Buffer.from('hello'.repeat(1000)));
```

Falls back to `zlib.gzipSync` when the native core is unavailable, so this
call always works.

### `compressZstd(buffer, level = 3)`

```js
const zst = B4N1Boost.compressZstd(payload);
```

**Throws** if the native core is unavailable — there is no pure-JS Zstd.
Failing loudly here is deliberate: silently returning a different
compression format would corrupt data expectations.

### `decompressZstd(buffer)`

```js
const raw = B4N1Boost.decompressZstd(zst);
```

Also throws when the native core is unavailable.

### `minifyHtml(htmlString)`

```js
B4N1Boost.minifyHtml('<p>  hi  </p>');
```

Falls back to whitespace collapsing without the native core.

### `isJsonValid(jsonString)`

```js
B4N1Boost.isJsonValid('{"a":1}');   // true
```

Falls back to `JSON.parse` in a try/catch.

## Express middleware

```js
const express = require('express');
require('b4n1-boost/express');

const app = express();
app.use(boostMiddleware());
```

The middleware handles compression and minification for you; see
`express.js` in the package for the options it accepts.

## Background tasks

```js
const { background, pendingTasks } = require('b4n1-boost/background');

const sendReport = background(async (userId) => {
  return `report-${userId}`;
}, { journal: './b4n1-tasks.jsonl' });

const handle = sendReport(42);
const result = await handle;
console.log(pendingTasks('./b4n1-tasks.jsonl'));
```

Returns immediately; work runs in a worker thread. Every submission is
journaled to disk, so a restart never loses a record. Full details in
[Background Tasks](background.md).

## Testing

```bash
npm test
```

Runs a four-state matrix: valid input, invalid input, an expected entry that
must be present, and an unknown entry that must be rejected. It must report
4/4.

## Fallback behaviour summary

| Call | Without native core |
|---|---|
| `compressGzip` | `zlib.gzipSync` (slower, correct output) |
| `compressZstd` | **throws** |
| `decompressZstd` | **throws** |
| `minifyHtml` | whitespace collapse (approximate) |
| `isJsonValid` | `JSON.parse` in try/catch |

Nothing degrades silently into something that merely looks like success.

## See also

- [Introduction](introduction.md) — what the shared core provides
- [Status & Diagnostics](status.md) — diagnosing a failed native load
