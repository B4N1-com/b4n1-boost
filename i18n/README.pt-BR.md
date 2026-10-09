<p align="center">
  <img src="../docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

# b4n1-boost

Engine de aceleración de desempeño transparente para **Django**, **FastAPI** e **Flask**.

`b4n1-boost` fornece aceleração de hardware Plug-and-Play para frameworks web Python, aumentando significativamente a capacidade de processamento de serialização JSON, consultas ORM e conexões WebSocket sem exigir alterações no código da sua aplicação.

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
