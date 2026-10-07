# License

b4n1-boost uses a **dual-layer license**. Two artifacts, two instruments —
read both before you distribute anything.

## 1. SDK wrapper source — Business Source License 1.1

The per-language SDK wrappers (the thin bindings for Python, Node.js, .NET,
Java, Go, PHP and Ruby) are licensed under
**Business Source License 1.1 (`BUSL-1.1`)**, with the full text in `LICENSE`
at the repository root.

### Parameters

| Field | Value |
|---|---|
| **Licensor** | B4N1 (b4n1.com) |
| **Licensed Work** | b4n1-boost — Python SDK and native acceleration libraries for Django, FastAPI, Flask, WSGI and ASGI |
| **Additional Use Grant** | Production use is free of charge, provided your organization's total annual gross revenue does not exceed **USD $100,000** |
| **Change Date** | Four years after the first publicly available distribution |
| **Change License** | Apache License, Version 2.0 |

### What that means in practice

- **You may use it in production for free** if your organization's total
  annual gross revenue is at or below USD $100,000.
- **Above that threshold**, or if you want to resell or provide b4n1-boost as
  a managed commercial service, you need a commercial license from the
  Licensor.
- **On the Change Date**, the Licensed Work converts to the Apache License
  2.0 and becomes openly licensed.
- You may study and modify the source for any purpose; the production
  restriction above is the binding term.

> `BUSL-1.1` is the correct SPDX identifier for Business Source License 1.1.
> Note that `BSL-1.1` in SPDX denotes an unrelated permissive license —
> always check which one a manifest actually declares.

## 2. Native binaries — End User License Agreement

The **precompiled native binaries** are licensed separately under a EULA that
ships *inside* every binary artifact:

- the compiled native libraries (`libb4n1_boost.so`, `b4n1_boost.dylib`,
  `b4n1_boost.dll`)
- the packaged per-language bindings (`*.node`, `*.jar`, `*.nupkg`, `*.gem`,
  `*.phar`, platform wheels)
- the `b4n1-boost` standalone executable

The `EULA.txt` travels with each artifact — a wheel, npm tarball, NuGet
package, Maven artifact or gem each carry their own copy. There is no separate
download step, and an artifact without its EULA is incomplete.

## 3. Combining the two

| If you are… | You are governed by… |
|---|---|
| Reading or modifying the SDK source | `LICENSE` (BUSL-1.1) |
| Installing from a registry and running it | the `EULA.txt` inside that artifact |
| Redistributing either | both — carry `LICENSE` and `EULA.txt` unchanged |

Any redistribution must keep **both** documents intact, together with all
copyright and trademark notices. Removing or altering the license metadata of
a published artifact is not permitted.

## 4. Trademarks

"Business Source License" is a trademark of MariaDB Corporation Ab; the
license text is copyright (c) 2017 MariaDB Corporation Ab, All Rights
Reserved, and is used here under its published terms. The B4N1 name, logos
and marks remain the property of B4N1.

## 5. No warranty

Both instruments are provided **as is**, without warranty of any kind,
express or implied, including but not limited to the warranties of
merchantability, fitness for a particular purpose and non-infringement. In no
event shall the Licensor be liable for any claim, damages or other liability
arising from use of the software.

## Commercial licensing

For licensing terms beyond the Additional Use Grant — enterprise deployment,
managed service delivery, or redistribution arrangements — contact
**dev@b4n1.com**.

## See also

- [Introduction](introduction.md)
- [Installation](installation.md)
- [Changelog](changelog.md)
