# Status & Diagnostics

Before you benchmark, migrate or file a performance bug, confirm what is
actually running. Most "it isn't faster" reports turn out to be a fallback
path that was never replaced.

## The one call that answers everything

```python
import b4n1_boost

print(b4n1_boost.status())
```

```python
{
    "native_extension": True,
    "version": "0.3.12",
    "features": {
        "json_acceleration": True,
        "json_canonicalize": True,
        "compression": ["gzip", "brotli", "zstd"],
        "middleware": ["django", "fastapi", "flask"],
    },
    "compression_engines": {
        "gzip": True,
        "brotli": True,
        "zstd": True,
    },
}
```

| Field | Meaning |
|---|---|
| `native_extension` | `True` only when the native core genuinely loaded |
| `version` | installed package version |
| `features` | what this build supports |
| `compression_engines` | which engines are actually live |

If `native_extension` is `False`, stop. Every performance figure in
[Performance](performance.md) is measured against the native core and does
not apply to a fallback.

## Diagnosing a failed load

Work through these in order:

**1. Confirm the wheel matched your platform**

```bash
pip show b4n1-boost
python -c "import sys; print(sys.version)"
```

The requirement is `>=3.10`. A platform without a published wheel will not
have a native core to load.

**2. Confirm the extension file exists**

```bash
python -c "import b4n1_boost, pathlib; p = pathlib.Path(b4n1_boost.__file__).parent; print(p); print(list(p.glob('_core*')))"
```

An empty list means the package installed without its native module —
usually a truncated download or an interrupted install. Reinstall:

```bash
pip install --force-reinstall --no-cache-dir b4n1-boost
```

**3. Import it directly to surface the real error**

```bash
python -c "import b4n1_boost._core"
```

An import error here prints the underlying cause, which is far more useful
than a `native_extension: False` summary.

**4. Check for a stale copy**

```bash
python -c "import b4n1_boost; print(b4n1_boost.__file__)"
```

A path outside the current virtual environment means an older global install
is shadowing the one you think you are testing.

**5. Verify after any upgrade**

```python
import b4n1_boost
assert b4n1_boost.status()["native_extension"] is True
assert b4n1_boost.__version__ == "0.3.12"
```

A cached extension from a previous version is a common source of confusing
results.

## Per-SDK availability checks

| SDK | Check | Notes |
|---|---|---|
| Python | `b4n1_boost.status()["native_extension"]` | authoritative |
| Node.js | `B4N1Boost.isAvailable()` | `true` only when genuinely bound |
| Node.js | `B4N1Boost.libraryPath()` | path of the binary actually loaded |
| .NET | see [page](csharp.md) | handles must be disposed |
| Java | see [page](java.md) | `B4N1_BOOST_LIB_PATH` validated on load |
| Go / PHP / Ruby | see their pages | thin wrappers over the same core |

Node's `libraryPath()` is particularly useful when more than one copy of the
package is installed: it names the exact binary in use, so you can tell
whether you are loading the one you edited.

## Health check as a runtime probe

```python
from b4n1_boost.middleware import HealthCheckMiddleware

app.wsgi_app = HealthCheckMiddleware(app.wsgi_app, path="/health")
```

```bash
curl -i http://localhost:8000/health
# HTTP/1.1 200 OK
# {"status": "ok"}
```

Wire this to your process supervisor. A 200 confirms the app is serving; it
does **not** confirm the native core loaded — pair it with `status()` at
startup if you want that assertion too.

## Assert at startup, not in production

Fail loudly the moment the core is missing, rather than discovering it under
load:

```python
import b4n1_boost

if not b4n1_boost.status()["native_extension"]:
    raise RuntimeError("b4n1-boost native core failed to load")
```

This is the difference between a deploy that fails immediately and one that
runs for a week at half speed.

## Reporting a problem

Include all of the following — it is the difference between a one-reply fix
and a week of questions:

1. `b4n1_boost.status()` output, verbatim
2. Python version and operating system / architecture
3. Output of `pip show b4n1-boost`
4. Output of `python -c "import b4n1_boost._core"` if it fails
5. The command you ran and what you expected

## See also

- [Installation](installation.md) — platform and version support
- [Performance](performance.md) — what the numbers assume
- [FAQ](faq.md) — common questions
