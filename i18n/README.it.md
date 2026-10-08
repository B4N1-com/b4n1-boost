# b4n1-boost

**Acceleratore Python.** Middleware nativo ad alte prestazioni per Django, FastAPI e Flask — JSON 10x più veloce, compressione 28x più veloce.

---

## ⚡ Panoramica delle prestazioni

| Componente | Metrica | rispetto a stdlib |
|---|---|---|
| **JSON dumps** (native engine) | 10.5x più veloce | dict medi (20 utenti) |
| **JSON dumps** (native engine) | 8.5x più veloce | dict grandi (500 utenti) |
| **Gzip** (nativo) | 1.47x più veloce | payload da 1MB |
| **Zstd** (nativo) | 28x più veloce | payload da 1MB |
| **Brotli** (nativo) | miglior rapporto | payload da 1MB |
| **DRF serializer** | 5-10x più veloce | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | inserimento nativo in blocco |
| **Dimensione wheel** | ~1.4MB | native, no compiler needed |

---

## 📦 Installazione

```bash
pip install b4n1-boost
```

Wheel nativi precompilati per Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) e Windows (x86_64). Nessun compilatore richiesto.

**Versioni Python supportate:** 3.10, 3.11, 3.12, 3.13

---

## 🚀 Quick Start

### Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Aggiunge DjangoBoostMiddleware a settings.MIDDLEWARE
```

### FastAPI
```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Flask
```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Rilevamento automatico
```python
import b4n1_boost
b4n1_boost.install()   # rileva il framework e installa il middleware giusto
```

---

## 🔧 Funzionalità

- **Serializzazione JSON** — fino a 10x più veloce di stdlib
- **Compressione** — gzip, zstd, brotli senza GIL
- **Middleware aware del Content-Type** — compressione automatica
- **ETag / 304** — caching delle risposte
- **Rate limiting** — protezione dalle richieste eccessive
- **Security headers** — HSTS e affini
- **CORS** — permessi di origine
- **Health check** — endpoint `/health`
- **Cache layer** — cache in processo
- **Acceleratore Django ORM** — PostgreSQL COPY per inserimenti in blocco
- **Acceleratore DRF Serializer** — queryset → JSON
- **Validazione JWT** — senza chiamate di rete
- **Minificazione HTML/CSS/JS**
- **HTML → Markdown** — adatto agli agenti
- **Telemetry** — report pronti
- **Background worker (zero-GIL)** — task in background senza bloccare Python

---

## 🔍 Stato e diagnostica

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.3.12', 'native_extension': True, 'features': [...]}
```

---

## 🔗 Link

- Sito: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- Repository: https://github.com/B4N1-com/b4n1-boost
- Licenze: https://b4n1.com/licensing oppure `b4n1@b4n1.com`
- Changelog: [CHANGELOG.md](../CHANGELOG.md)

---

## 📄 Licenza

**Business Source License 1.1 (BUSL-1.1)**.

- **Gratuito** per sviluppo, valutazione, test, progetti personali e startup con fatturato annuo inferiore a **100K USD**.
- **Licenza commerciale** richiesta per organizzazioni con fatturato >= **100K USD**, enti governativi e gare pubbliche.
- Dopo la **Change Date** (4 anni) → **Apache License 2.0**.

Testo completo in [LICENSE](../LICENSE).

---

_b4n1-boost: Acceleratore Python. JSON 10x più veloce. Compressione 28x più veloce. Middleware trasparente. Creato con ❤️ da B4N1._
