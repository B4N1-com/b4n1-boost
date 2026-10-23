# README Template — b4n1-<name>

> Copiar este archivo a `README.md` y reemplazar `<name>`, `<description>`, `<version>`, badges.

---

# b4n1-<name>

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-mdBook-blue)](https://B4N1-com.github.io/b4n1-<name>/book/)
[![PyPI](https://img.shields.io/pypi/v/b4n1-<name>)](https://pypi.org/project/b4n1-<name>/)
[![npm](https://img.shields.io/npm/v/b4n1-<name>)](https://www.npmjs.com/package/b4n1-<name>)
[![NuGet](https://img.shields.io/nuget/v/B4n1<Name>)](https://www.nuget.org/packages/B4n1<Name>)
[![Maven Central](https://img.shields.io/maven-central/v/com.b4n1/b4n1-<name>)](https://central.sonatype.com/artifact/com.b4n1/b4n1-<name>)

> **<description>** — Ultra-lightweight, zero-dependency, cross-platform.

---

## 🚀 Quick Start

### Python
```bash
pip install b4n1-<name>
```
```python
from b4n1<name> import AgentBrowser, BrowserMode

browser = AgentBrowser(mode=BrowserMode.LIGHT)
page = browser.goto("https://example.com")
print(page.markdown)
browser.close()
```

### JavaScript/TypeScript
```bash
npm install b4n1-<name>
```
```typescript
import { AgentBrowser, BrowserMode } from "b4n1-<name>";

const browser = new AgentBrowser({ mode: BrowserMode.LIGHT });
const page = await browser.goto("https://example.com");
console.log(page.markdown);
browser.close();
```

### Java (Maven)
```xml
<dependency>
    <groupId>com.b4n1</groupId>
    <artifactId>b4n1-<name></artifactId>
    <version>X.Y.Z</version>
</dependency>
```
```java
import com.b4n1.web.*;
BrowserOptions opts = new BrowserOptions();
opts.setMode(BrowserMode.LIGHT);
try (AgentBrowser b = new AgentBrowser(opts)) {
    Page p = b.goto_("https://example.com");
    System.out.println(p.getMarkdown());
}
```

### C# (.NET)
```bash
dotnet add package B4n1<Name>
```
```csharp
using B4N1.Web;
var opts = new BrowserOptions { Mode = BrowserMode.Light };
using (var b = new AgentBrowser(opts)) {
    var p = b.Goto("https://example.com");
    Console.WriteLine(p.Markdown);
}
```

---

## 🖥 Platform Support

| Platform | Architectures | Binary |
|----------|---------------|--------|
| **Linux** | x86_64, aarch64, i686 | `musl` (static, no glibc) |
| **macOS** | x86_64, arm64 | `universal` (Mach-O) |
| **Windows** | x86_64 | `gnu` (MinGW) |

**Total: 6 pre-compiled binaries** — works everywhere, no runtime dependencies.

---

## 📦 Installation

| Registry | Command |
|----------|---------|
| **PyPI** | `pip install b4n1-<name>==X.Y.Z` |
| **npm** | `npm install b4n1-<name>@X.Y.Z` |
| **NuGet** | `dotnet add package B4n1<Name> --version X.Y.Z` |
| **Maven** | `<version>X.Y.Z</version>` in `pom.xml` |

---

## 🔧 Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `B4N1_<NAME>_BIN_PATH` | Custom binary path | Auto-detect |
| `B4N1_<NAME>_DAEMON_KEY` | Daemon auth key | Random |
| `B4N1_<NAME>_DAEMON_BIND` | Daemon bind address | `127.0.0.1:0` |

---

## 📚 Documentation

📖 **Full documentation**: https://B4N1-com.github.io/b4n1-<name>/book/

- [Quickstart](https://B4N1-com.github.io/b4n1-<name>/book/quickstart.html)
- [Installation](https://B4N1-com.github.io/b4n1-<name>/book/installation.html)
- [CLI Reference](https://B4N1-com.github.io/b4n1-<name>/book/cli.html)
- [Python SDK](https://B4N1-com.github.io/b4n1-<name>/book/python.html)
- [JavaScript SDK](https://B4N1-com.github.io/b4n1-<name>/book/javascript.html)
- [Java SDK](https://B4N1-com.github.io/b4n1-<name>/book/java.html)
- [C# SDK](https://B4N1-com.github.io/b4n1-<name>/book/csharp.html)
- [Changelog](https://B4N1-com.github.io/b4n1-<name>/book/changelog.html)

---

## 🏗 Building from Source

```bash
# Requisitos: Rust 1.75+, zig 0.13, cargo-zigbuild
bash scripts/build.sh --all  # 6 targets: linux x3, macOS 2, windows 1
```

---

## 📄 License

**SDKs**: [Business Source License 1.1](LICENSE) — Free for non-production use.
**Binaries**: [EULA](EULA.txt) — Commercial license required for production.

See [MANIFEST.md](MANIFEST.md) for full interface inventory.

---

## 🤝 Enterprise & Support

For Enterprise B2B licensing, support SLA, or custom integrations:
📧 **b4n1@b4n1.com** | 🌐 **https://b4n1.com**

---

## 🔗 Links

- **GitHub**: https://github.com/B4N1-com/b4n1-<name>
- **PyPI**: https://pypi.org/project/b4n1-<name>/
- **npm**: https://www.npmjs.com/package/b4n1-<name>
- **NuGet**: https://www.nuget.org/packages/B4n1<Name>
- **Maven Central**: https://central.sonatype.com/artifact/com.b4n1/b4n1-<name>
- **Documentation**: https://B4N1-com.github.io/b4n1-<name>/book/
EOF
echo "README_TEMPLATE.md creado"