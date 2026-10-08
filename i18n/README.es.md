# b4n1-boost

**El Acelerador de Python.** JSON 10x más rápido. Compresión 28x más rápida. Middleware transparente.

`b4n1-boost` proporciona aceleración nativa Plug-and-Play para frameworks web de Python, aumentando significativamente el rendimiento de serialización JSON, compresión nativa (gzip/brotli/zstd) y soporte para Django, FastAPI y Flask.

---

## Resumen de Rendimiento (v0.3.4)

| Componente | Métrica | vs stdlib |
|---|---|---|
| **JSON dumps** (orjson) | 10.5x más rápido | Dicts medianos (20 usuarios) |
| **JSON dumps** (orjson) | 8.5x más rápido | Dicts grandes (500 usuarios) |
| **Gzip** (nativo) | 1.47x más rápido | Payloads de 1MB |
| **Zstd** (nativo) | 28x más rápido | Payloads de 1MB |
| **Brotli** (nativo) | 0.0% ratio | Mejor ratio de compresión |
| **DRF serializer** | 5-10x más rápido | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | bulk insert nativo |
| **Tamaño wheel** | 1.4MB | simd-json + zstd |
| **PyO3** | 0.28 | Free-threading soportado |
| **Tests** | 86 total | 75 Python + 11 Rust |

---

## 📦 Instalación

```bash
pip install b4n1-boost
```

*(Los binarios nativos precompilados se instalan automáticamente — no requiere compilador)*

---

## 🚀 Inicio Rápido

### Django
```python
import b4n1_boost
b4n1_boost.install_django()
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

### Detección Automática
```python
import b4n1_boost
b4n1_boost.autoboost()
```

---

## 🔧 Referencia de API

### Serialización JSON

```python
from b4n1_boost import NativeJson, canonicalize_json, validate_json

# JSON rápido (usa orjson cuando está disponible, 10x más rápido)
result = NativeJson.dumps({"users": [...]})

# Ruta directa PyO3 (sin conversión intermedia)
result = NativeJson.dumps_direct(data)

# Canonicalizar: keys ordenadas, forma compacta (acepta str o dict)
canonicalize_json({"z": 1, "a": 2})  # '{"a":2,"z":1}'
canonicalize_json('{"z":1,"a":2}')   # '{"a":2,"z":1}'

# Validación JSON rápida
validate_json('{"valid": true}')  # True
validate_json('{bad json}')       # False
```

### Compresión Nativa (GIL-free)

```python
from b4n1_boost.middleware import _native_gzip, _native_brotli, _native_zstd

_compressed = _native_zstd(payload)    # 28x más rápido que stdlib gzip
_compressed = _native_brotli(payload)  # Mejor ratio (0.0% en 1MB)
_compressed = _native_gzip(payload)    # 1.47x más rápido que stdlib
```

### Middleware con Detección de Content-Type

```python
from b4n1_boost.middleware import B4N1BoostCompressionMiddleware

# Salta automáticamente: imágenes, video, audio, fuentes, archivos comprimidos
app.wsgi_app = B4N1BoostCompressionMiddleware(
    app.wsgi_app,
    min_size=1024,
    fast_mode=False  # True = prefiere zstd sobre brotli (velocidad > ratio)
)

# Para FastAPI/ASGI (soporte streaming)
from b4n1_boost.middleware import FastAPIBoostCompressionMiddleware
app.add_middleware(FastAPIBoostCompressionMiddleware)
```

### ETag / 304 Caching

```python
from b4n1_boost.middleware import ETagMiddleware

# Genera ETags automáticamente del body de respuesta
# Retorna 304 Not Modified cuando el cliente envía If-None-Match coincidente
app.wsgi_app = ETagMiddleware(app.wsgi_app)
```

### Rate Limiting

```python
from b4n1_boost.middleware import RateLimitMiddleware

# Token bucket: 100 requests/min por IP de cliente
app.wsgi_app = RateLimitMiddleware(app.wsgi_app, max_requests=100, window_seconds=60)
```

### Detección de Proxy

```python
from b4n1_boost.middleware import detect_proxy

if detect_proxy(environ):
    # Saltar compresión — upstream ya comprimió
    return body
```

### Métricas de Compresión

```python
from b4n1_boost.middleware import metrics

snapshot = metrics.get_snapshot()
# {"total_bytes_in": 1024000, "total_bytes_out": 12288, "total_requests": 150, ...}
```

### Acelerador Django ORM

```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

# PostgreSQL COPY — 5-10x más rápido que Django ORM
bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
])
```

### Acelerador DRF Serializer

```python
from b4n1_boost.drf_accelerator import fast_serialize, FastSerializerMixin

# queryset → JSON sin overhead de DRF (5-10x más rápido)
json_bytes = fast_serialize(queryset, fields=["id", "name", "email"])

# Mixin para serializers existentes
class MySerializer(FastSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ["id", "name"]
```

---

## 📊 Comparativa de Compresión

```
10KB payload:
Original:     10,000 bytes (100%)
gzip:            120 bytes (1.2%)   ← 1.47x más rápido que stdlib
brotli:            0 bytes (0.0%)   ← Mejor ratio
zstd:             70 bytes (0.7%)   ← 8x más rápido que gzip

1MB payload (2000 iteraciones):
gzip py:     15.993s (125 ops/s)
gzip rust:   10.894s (184 ops/s) = 1.47x más rápido
zstd rust:    0.569s (3,513 ops/s) = 28x más rápido que gzip py
```

---

## 🔗 Enlaces

- Sitio web: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- Licencias: https://b4n1.com/licensing o `b4n1@b4n1.com`

---

## 🛡️ Licencia

Distribuido bajo **Business Source License 1.1 (BSL 1.1)**.

- **Gratis** para desarrollo, evaluación, testing, proyectos personales y startups con ingresos anuales inferiores a **USD $100,000**.
- **Licencia comercial** requerida para organizaciones con ingresos anuales **>= USD $100,000**, agencias gubernamentales y licitaciones públicas.
- Tras la **Change Date** (4 años), el trabajo pasa a **Apache License 2.0**.

Consulta [LICENSE](LICENSE) para el texto legal completo.

---

*[English](README.md)*

_b4n1-boost: El Acelerador de Python. JSON 10x más rápido. Compresión 28x más rápida. Middleware transparente._
