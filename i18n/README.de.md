# b4n1-boost

Transparente Leistungsbeschleunigung für **Django**, **FastAPI** und **Flask**.

`b4n1-boost` bietet ein natives Rust-Middleware Plug-and-Play für Python-Web-Frameworks: zero-copy Pass-Through für Antworten, native gzip/Brotli-Komprimierung ohne GIL und eine native JSON-Engine – ohne Änderungen am Anwendungscode.

---

> Miss die Beschleunigung End-to-End in deiner eigenen Anwendung – der echte Gewinn hängt von deiner Workload ab.

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
