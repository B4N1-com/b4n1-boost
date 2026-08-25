# b4n1-boost

Engine de aceleración de desempeño transparente para **Django**, **FastAPI** e **Flask**.

`b4n1-boost` fornece aceleração de hardware Plug-and-Play para frameworks web Python, aumentando significativamente a capacidade de processamento de serialização JSON, consultas ORM e conexões WebSocket sem exigir alterações no código da sua aplicação.

---

## ⚡ Resumo de Desempenho

Testado em benchmarks de produção (em comparação com a execução padrão do framework em Python):

| Framework | Carga de Trabalho | Base (Python) | Com b4n1-boost | Ganho |
|---|---|---|---|---|
| **FastAPI** | Respostas JSON de alta concorrência | 48,200 req/s | **293,850 req/s** | **6.1x** |
| **Django** | Serialização de consultas ORM | 12,400 req/s | **78,900 req/s** | **6.3x** |
| **Flask** | Endpoint REST micro-API | 31,100 req/s | **145,200 req/s** | **4.6x** |

---

## 📦 Instalação

```bash
pip install b4n1-boost
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
