# Background Tasks

Run heavy work off the request path **without standing up a queue broker**.

## Why not a broker

A task queue is the right answer when work must survive a machine failure or
be shared across many hosts. It is the wrong answer when the work is local,
frequently, and a lost task costs a retry.

b4n1-boost targets the second case: work is handed to a worker thread
immediately, and optionally journaled to disk so a restart can pick it up.

## Python

```python
from b4n1_boost import background, pending_tasks

@background
def build_report(user_id):
    # heavy work: render, aggregate, upload...
    return f"report-{user_id}"

handle = build_report(42)
result = handle.result()      # block only when you need the value
```

### Crash recovery

```python
from b4n1_boost import pending_tasks

pending = pending_tasks("./b4n1-tasks.jsonl")
for task in pending:
    ...   # re-run what a restart interrupted
```

When a journal path is configured, every submission is written before the
task runs. A process restart therefore never silently loses a record.

## Node.js

```js
const { background, pendingTasks } = require('b4n1-boost/background');

const sendReport = background(async (userId) => {
  // build PDF, send email...
  return `report-${userId}`;
}, { journal: './b4n1-tasks.jsonl' });

const handle = sendReport(42);
const result = await handle;                     // wait when you need it
console.log(pendingTasks('./b4n1-tasks.jsonl')); // crash recovery
```

Returns in about a millisecond; the heavy work runs in a worker thread.

## Worker-thread primitives

For single operations rather than whole functions:

```python
from b4n1_boost import worker_compress, worker_decompress
from b4n1_boost import worker_minify, worker_jwt_validate, worker_shutdown

future = worker_compress(data, "zstd")
compressed = future.result()
```

| Function | Purpose |
|---|---|
| `worker_compress` / `worker_decompress` | Compression off the calling thread |
| `worker_minify` | HTML/CSS/JS minification |
| `worker_jwt_validate` | Token verification |
| `worker_shutdown` | Stop the worker pool during graceful exit |

## When to reach for something else

Use an external queue instead when **any** of these hold:

- Tasks must survive losing the whole machine, not just the process
- More than one host needs to pull from the same queue
- You need delayed delivery, retries with backoff, or scheduled runs
- A lost task is unacceptable without a durable record elsewhere
- You need per-task visibility for operators

Journaling gives you restart safety on one host. It is not distributed
coordination, and it does not pretend to be.

## Graceful shutdown

Always stop the pool before the process exits, otherwise in-flight work can
be cut mid-write:

```python
from b4n1_boost import worker_shutdown

worker_shutdown()
```

Wire this to your framework's shutdown hook — see the Django and FastAPI
examples in the [Python SDK](python.md).

## See also

- [Python SDK](python.md) — where `background` and `pending_tasks` live
- [Node.js SDK](node.md) — the JavaScript surface
