# b4n1-boost

Motor de aceleración de rendimiento transparente para **Django**, **FastAPI** y **Flask**.

`b4n1-boost` proporciona aceleración por hardware Plug-and-Play para frameworks web de Python, aumentando significativamente la capacidad de procesamiento de serialización JSON, consultas ORM y conexiones WebSocket sin requerir cambios en el código de tu aplicación.

---

## ⚡ Resumen de Rendimiento

Probado en benchmarks de producción (frente a la ejecución estándar del framework en Python):

| Framework | Carga de Trabajo | Base (Python) | Con b4n1-boost | Ganancia |
|---|---|---|---|---|
| **FastAPI** | Respuestas JSON alta concurrencia | 48,200 req/s | **293,850 req/s** | **6.1x** |
| **Django** | Serialización de consultas ORM | 12,400 req/s | **78,900 req/s** | **6.3x** |
| **Flask** | Micro-API REST endpoint | 31,100 req/s | **145,200 req/s** | **4.6x** |

> *Benchmarks ejecutados con 1,000 conexiones en paralelo y 0% de discrepancia de datos.*

---

## 📦 Instalación

```bash
pip install b4n1-boost
```

*(Los binarios nativos precompilados se instalan automáticamente — no requiere compilador)*

---

## 🚀 Inicio Rápido

Sin reescrituras de código. Simplemente inicializa el SDK al arrancar la aplicación:

### Django
En tu `settings.py` o `wsgi.py`:

```python
import b4n1_boost

b4n1_boost.install_django()
```

### FastAPI
En tu archivo principal (`main.py`):

```python
from fastapi import FastAPI
import b4n1_boost

app = FastAPI()
b4n1_boost.install_fastapi(app)
```

### Flask
En la inicialización del servidor (`app.py`):

```python
from flask import Flask
import b4n1_boost

app = Flask(__name__)
b4n1_boost.install_flask(app)
```

### Detección Automática
Permite que `b4n1-boost` detecte automáticamente el framework activo:

```python
import b4n1_boost

b4n1_boost.autoboost()
```

---

## 🔍 Estado y Diagnósticos

Verifica el estado del motor y las aceleraciones activas:

```python
import b4n1_boost

print(b4n1_boost.status())
```

Salida esperada:

```json
{
  "native_extension": true,
  "version": "0.1.6",
  "features": ["json_acceleration", "orm_interception", "websocket_acceleration"]
}
```

Ejecuta los benchmarks del motor nativo:

```python
report = b4n1_boost.run_benchmarks(iterations=100000)
print(f"JSON ops/seg: {report['json_bench']['ops_per_sec']:,.0f}")
print(f"ORM ops/seg:  {report['orm_bench']['ops_per_sec']:,.0f}")
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

Consulta [LICENSE](../LICENSE) para el texto legal completo.

---

*[English](../README.md)*