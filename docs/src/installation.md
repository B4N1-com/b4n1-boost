# Installation

```bash
pip install b4n1-boost
```

Precompiled wheels are published for every supported platform. There is no
compiler step, no build backend invocation and no system dependency to install
first.

## Supported platforms

| Platform | Wheel tag | Status |
|---|---|---|
| Linux x86_64 | `manylinux2014_x86_64` | ✅ precompiled |
| Linux aarch64 | `manylinux_2_17_aarch64` | ✅ precompiled |
| macOS x86_64 | `macosx_10_13_x86_64` | ✅ precompiled |
| macOS arm64 (Apple Silicon) | `macosx_11_0_arm64` | ✅ precompiled |
| Windows x86_64 | `win_amd64` | ✅ precompiled |

## Supported Python versions

| Version | Status |
|---|---|
| 3.10 | ✅ |
| 3.11 | ✅ |
| 3.12 | ✅ |
| 3.13 | ✅ |

The requirement is `>=3.10`. Wheels are built against the stable ABI, so a
single wheel per platform covers every supported interpreter.

## Verify the install

```python
import b4n1_boost

status = b4n1_boost.status()
assert status["native_extension"] is True, (
    "native core did not load: %s" % status
)
print("b4n1-boost", status["version"], "ready")
```

If `native_extension` is `False`, pip fell back to a pure-Python path. See
[Status & Diagnostics](status.md) — do not benchmark until this reads `True`.

## Pinning a version

```bash
pip install b4n1-boost==0.3.12
```

## Upgrading

```bash
pip install --upgrade b4n1-boost
```

After an upgrade, re-run the verification snippet. A stale cached extension
from a previous version is a common source of confusing benchmark results.

## Uninstalling

```bash
pip uninstall b4n1-boost
```

No files are written outside the virtual environment, and no background
process is left running.

## Installing the other SDKs

b4n1-boost shares one native core across several language SDKs:

| SDK | Package | Page |
|---|---|---|
| Python | `b4n1-boost` (PyPI) | [Python SDK](python.md) |
| Node.js | `b4n1-boost` (npm) | [Node.js SDK](node.md) |
| .NET | `B4N1.Boost` (NuGet) | [.NET SDK](csharp.md) |
| Java | `com.b4n1:boost` (Maven Central) | [Java SDK](java.md) |
| Go | module import | [Go SDK](go.md) |
| PHP | Composer package | [PHP SDK](php.md) |
| Ruby | Gem | [Ruby SDK](ruby.md) |
