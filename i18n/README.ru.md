<p align="center">
  <img src="../docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

# b4n1-boost

**Ускоритель Python.** Быстрый нативный middleware для Django, FastAPI и Flask — JSON в 10 раз быстрее, сжатие в 28 раз быстрее.

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

## ⚡ Производительность

| Компонент | Метрика | относительно stdlib |
|---|---|---|
| **JSON dumps** (native engine) | в 10.5x быстрее | средние dict (20 пользователей) |
| **JSON dumps** (native engine) | в 8.5x быстрее | большие dict (500 пользователей) |
| **Gzip** (нативный) | в 1.47x быстрее | payload 1 МБ |
| **Zstd** (нативный) | в 28x быстрее | payload 1 МБ |
| **Brotli** (нативный) | лучшее сжатие | payload 1 МБ |
| **DRF serializer** | в 5-10x быстрее | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | пакетная вставка |
| **Размер wheel** | ~1.4 МБ | native, no compiler needed |

---

## 📦 Установка

```bash
pip install b4n1-boost
```

Предварительно собранные нативные wheel для Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon) и Windows (x86_64). Компилятор не требуется.

**Поддерживаемые версии Python:** 3.10, 3.11, 3.12, 3.13

---

## 🚀 Быстрый старт

### Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# Добавляет DjangoBoostMiddleware в settings.MIDDLEWARE
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

### Автоопределение
```python
import b4n1_boost
b4n1_boost.install()   # определяет фреймворк и ставит нужный middleware
```

---

## 🔧 Возможности

- **Сериализация JSON** — до 10x быстрее stdlib
- **Сжатие** — gzip, zstd, brotli без GIL
- **Middleware по Content-Type** — автоматическое сжатие
- **ETag / 304** — кэширование ответов
- **Rate limiting** — защита от перегрузки
- **Security headers** — HSTS и другие
- **CORS** — управление источниками
- **Health check** — эндпоинт `/health`
- **Cache layer** — внутрипроцессный кэш
- **Ускоритель Django ORM** — пакетная вставка через PostgreSQL COPY
- **Ускоритель DRF Serializer** — queryset → JSON
- **Проверка JWT** — без сетевых вызовов
- **Минификация HTML/CSS/JS**
- **HTML → Markdown** — для агентных сценариев
- **Telemetry** — готовые отчёты
- **Фоновый воркер (zero-GIL)** — фоновые задачи, не блокируя Python

---

## 🔍 Состояние и диагностика

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.3.13', 'native_extension': True, 'features': [...]}
```

---

## 🔗 Ссылки

- Сайт: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- Репозиторий: https://github.com/B4N1-com/b4n1-boost
- Лицензирование: https://b4n1.com/licensing или `b4n1@b4n1.com`
- Changelog: [CHANGELOG.md](../CHANGELOG.md)

---

## 📄 Лицензия

**Business Source License 1.1 (BUSL-1.1)**.

- **Бесплатно** для разработки, оценки, тестирования, личных проектов и стартапов с годовым доходом **менее 100 тыс. долларов США**.
- **Коммерческая лицензия** обязательна для организаций с доходом **от 100 тыс. долларов США**, государственных учреждений и публичных торгов.
- После **Change Date** (4 года) → **Apache License 2.0**.

Полный текст — в [LICENSE](../LICENSE).

---

_b4n1-boost: Ускоритель Python. JSON в 10 раз быстрее. Сжатие в 28 раз быстрее. Прозрачный middleware. Сделано B4N1 с ❤️._
