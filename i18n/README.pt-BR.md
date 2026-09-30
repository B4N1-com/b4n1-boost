# b4n1-boost

Engine de aceleración de desempeño transparente para **Django**, **FastAPI** e **Flask**.

`b4n1-boost` fornece um middleware nativo em Rust Plug-and-Play para frameworks web Python: caminho de resposta pass-through sem cópia, compressão nativa gzip/Brotli sem GIL e engine JSON nativa, sem alterações no código da sua aplicação.

---

> Meça a aceleração de ponta a ponta na sua própria aplicação — o ganho real depende da sua carga de trabalho.

---

## 📦 Instalação

Disponível nos 4 registros (núcleo nativo + EULA incluídos):

```bash
pip install b4n1-boost          # Python 3.10–3.13
npm install b4n1-boost          # Node.js
dotnet add package B4N1.Boost   # .NET
```
```xml
<dependency>
  <groupId>com.b4n1</groupId>
  <artifactId>boost</artifactId>
  <version>0.3.5</version>
</dependency>
```

---

## 🚀 Início Rápido

```python
import b4n1_boost

# Ativar para Django
b4n1_boost.install_django()

# Ativar para FastAPI
b4n1_boost.install_fastapi()

# Ativar para Flask
b4n1_boost.install_flask()
```
