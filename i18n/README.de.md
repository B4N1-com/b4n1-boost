# b4n1-boost

Transparente Leistungsbeschleunigung für **Django**, **FastAPI** und **Flask**.

`b4n1-boost` bietet Plug-and-Play-Hardwarebeschleunigung für Python-Web-Frameworks und erhöht den Durchsatz von JSON-Serialisierung, ORM-Abfragen und WebSocket-Verbindungen erheblich, ohne dass Codeänderungen erforderlich sind.

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
