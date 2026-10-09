<p align="center">
  <img src="../docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

# b4n1-boost

**مسرّع بايثون.** وسيط أصلي سريع لـ Django وFastAPI وFlask — JSON أسرع 10 مرات، وضغط أسرع 28 مرة.

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

## ⚡ لمحة عن الأداء

| المكوّن | القياس | مقارنة بـ stdlib |
|---|---|---|
| **JSON dumps** (native engine) | أسرع 10.5x | قوائم متوسطة (20 مستخدماً) |
| **JSON dumps** (native engine) | أسرع 8.5x | قوائم كبيرة (500 مستخدم) |
| **Gzip** (أصلي) | أسرع 1.47x | حزم 1MB |
| **Zstd** (أصلي) | أسرع 28x | حزم 1MB |
| **Brotli** (أصلي) | أفضل نسبة ضغط | حزم 1MB |
| **DRF serializer** | أسرع 5-10x | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | إدراج دفعة واحد |
| **حجم العجلة (wheel)** | ~1.4MB | native, no compiler needed |

---

## 📦 التثبيت

```bash
pip install b4n1-boost
```

عجلات مبنية مسبقاً لأنظمة Linux (x86_64 + aarch64)، وmacOS (x86_64 + Apple Silicon)، وWindows (x86_64). لا حاجة لأي مترجم.

**إصدارات بايثون المدعومة:** 3.10، 3.11، 3.12، 3.13

---

## 🚀 البدء السريع

### Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# يضيف DjangoBoostMiddleware إلى إعدادات settings.MIDDLEWARE
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

### كشف تلقائي
```python
import b4n1_boost
b4n1_boost.install()   # يكتشف الإطار تلقائياً ويثبّت الوسيط المناسب
```

---

## 🔧 الميزات

- **تسلسل JSON** — أسرع حتى 10 مرات من stdlib
- **ضغط** — gzip وzstd وbrotli بدون GIL
- **وسائط حسب Content-Type** — ضغط وتشفير تلقائي
- **ETag / 304** — تخزين مؤقت للنسخ
- **تحديد المعدل** — حماية من الإفراط في الطلبات
- **رؤوس الأمان** — HSTS و-content-type وغيرها
- **CORS** — إدارة صلاحيات النطاقات
- **فحص الصحة** — نقطة `/health`
- **طبقة التخزين** — ذاكرة داخلية سريعة
- **تسريع Django ORM** — PostgreSQL COPY للإدراج الدفعي
- **تسريع DRF Serializer** — تحويل queryset إلى JSON
- **التحقق من JWT** — بدون استدعاءات شبكة
- **تصغير HTML/CSS/JS** — ضغط في الموضع
- **HTML → Markdown** — مناسب للوكلاء
- **قياس النشاط** — تقارير جاهزة
- **عامل خلفي (zero-GIL)** — مهام خلفية لا تعطّل بايثون

---

## 🔍 الحالة والتشخيص

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.3.13', 'native_extension': True, 'features': [...]}
```

---

## 🔗 روابط

- الموقع: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- المستودع: https://github.com/B4N1-com/b4n1-boost
- الترخيص: https://b4n1.com/licensing أو `b4n1@b4n1.com`
- سجل التغييرات: [CHANGELOG.md](../CHANGELOG.md)

---

## 📄 الترخيص

**Business Source License 1.1 (BUSL-1.1)**.

- **مجاني** للتطوير والتقييم والاختبار والمشاريع الشخصية والشركات الناشئة التي يتجاوز دخلها السنوي **100 ألف دولار أمريكي**.
- يلزم **رخصة تجارية** للمؤسسات التي تبلغ **100 ألف دولار أمريكي** أو أكثر، وللجهات الحكومية والمناقصات العامة.
- بعد **تاريخ التغيير** (4 سنوات) → **Apache License 2.0**.

راجع [LICENSE](../LICENSE) للنص الكامل.

---

_b4n1-boost: مسرّع بايثون. JSON أسرع 10 مرات. ضغط أسرع 28 مرة. وسيط شفاف. صُنع بـ ❤️ من B4N1._
