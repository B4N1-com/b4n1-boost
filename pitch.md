# b4n1-boost — Pitch

## What it is
Native Rust acceleration for Django/FastAPI/Flask. JSON, compression, ORM,
and WebSocket acceleration — measured, not promised. Thin SDKs over the same
C-ABI core in 7 languages.

## Who it is for
Python web developers running Django/FastAPI/Flask who want native-speed
JSON parsing, compression, and ORM without rewriting their app.

## Pain it removes
- Slow JSON serialization in Python web apps.
- GIL-bound compression bottlenecks.
- ORM query overhead on large datasets.

## Value bullets
1. Drop-in middleware: `pip install b4n1-boost`, one line of config.
2. Measured speedups: `b4n1-boost bench` shows live numbers on YOUR machine.
3. Polyglot: same core in Python, Node, Java, C#, Ruby, PHP, Go.

## Demonstrable metric
`b4n1-boost demo` — live JSON parse/compress/ORM numbers on this machine.

## Call to action
`b4n1-boost docs` for the full manual. `b4n1-boost demo` for live numbers.