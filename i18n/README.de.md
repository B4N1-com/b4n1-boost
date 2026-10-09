<p align="center">
  <img src="../docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

# b4n1-boost

Transparente Leistungsbeschleunigung für **Django**, **FastAPI** und **Flask**.

`b4n1-boost` bietet Plug-and-Play-Hardwarebeschleunigung für Python-Web-Frameworks und erhöht den Durchsatz von JSON-Serialisierung, ORM-Abfragen und WebSocket-Verbindungen erheblich, ohne dass Codeänderungen erforderlich sind.

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-mdBook-blue)](https://b4n1-com.github.io/b4n1-boost/)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![npm](https://img.shields.io/npm/v/b4n1-boost.svg)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet](https://img.shields.io/nuget/v/B4N1.Boost.svg)](https://www.nuget.org/packages/B4N1.Boost)
[![Python](https://img.shields.io/pypi/pyversions/b4n1-boost)](https://pypi.org/project/b4n1-boost/)
[![Tests](https://img.shields.io/badge/tests-772%20passing-brightgreen)](https://pypi.org/project/b4n1-boost/)

[![PyPI Downloads/month](https://img.shields.io/pypi/dm/b4n1-boost)](https://pypi.org/project/b4n1-boost/)
[![npm Downloads/month](https://img.shields.io/npm/dm/b4n1-boost)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet Downloads](https://img.shields.io/nuget/dt/B4N1.Boost)](https://www.nuget.org/packages/B4N1.Boost)
[![PyPI total](https://img.shields.io/pepy/dt/b4n1-boost)](https://pepy.tech/project/b4n1-boost)

---

## ⚡ Leistungsübersicht

Getestet in Produktions-Benchmarks (im Vergleich zur Python-Standardausführung):

| Framework | Arbeitslast | Basis (Python) | Mit b4n1-boost | Beschleunigung |
|---|---|---|---|---|
| **FastAPI** | JSON-Antworten bei hoher Parallelität | 48.200 req/s | **293.850 req/s** | **6.1x** |
| **Django** | ORM-Abfrageserialisierung | 12.400 req/s | **78.900 req/s** | **6.3x** |
| **Flask** | Mikro-API REST-Endpunkt | 31.100 req/s | **145.200 req/s** | **4.6x** |

---

## 📦 Installation

```bash
pip install b4n1-boost
```

---

## 🚀 Schnellstart

```python
import b4n1_boost

# Aktivieren für Django
b4n1_boost.install_django()

# Aktivieren für FastAPI
b4n1_boost.install_fastapi()

# Aktivieren für Flask
b4n1_boost.install_flask()
```
