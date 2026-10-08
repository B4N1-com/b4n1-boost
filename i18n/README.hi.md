# b4n1-boost

**पायथन एक्सेलरेटर।** Django, FastAPI, Flask के लिए तेज़ मिडलवेयर — JSON 10x तेज़, कंप्रेशन 28x तेज़।

---

## ⚡ प्रदर्शन पर एक नज़र

| घटक | माप | stdlib की तुलना में |
|---|---|---|
| **JSON dumps** (native engine) | 10.5x तेज़ | मध्यम dicts (20 उपयोगकर्ता) |
| **JSON dumps** (native engine) | 8.5x तेज़ | बड़े dicts (500 उपयोगकर्ता) |
| **Gzip** (native) | 1.47x तेज़ | 1MB payloads |
| **Zstd** (native) | 28x तेज़ | 1MB payloads |
| **Brotli** (native) | सर्वश्रेष्ठ अनुपात | 1MB payloads |
| **DRF serializer** | 5-10x तेज़ | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | bulk insert native |
| **Wheel आकार** | ~1.4MB | native, no compiler needed |

---

## 📦 इंस्टॉलेशन

```bash
pip install b4n1-boost
```

पहले से बने नेटिव व्हील: Linux (x86_64 + aarch64), macOS (x86_64 + Apple Silicon), Windows (x86_64)। किसी कंपाइलर की ज़रूरत नहीं।

**समर्थित Python संस्करण:** 3.10, 3.11, 3.12, 3.13

---

## 🚀 क्विक स्टार्ट

### Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# settings.MIDDLEWARE में DjangoBoostMiddleware जोड़ता है
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

### स्वचालित पहचान
```python
import b4n1_boost
b4n1_boost.install()   # फ्रेमवर्क पहचानता है और सही मिडलवेयर लगाता है
```

---

## 🔧 विशेषताएँ

- **JSON सीरियलाइज़ेशन** — stdlib से 10x तक तेज़
- **कंप्रेशन** — gzip, zstd, brotli, GIL-मुक्त
- **Content-Type aware middleware** — स्वचालित कंप्रेशन
- **ETag / 304** — कैशिंग
- **Rate limiting** — अनुरोध सीमा
- **Security headers** — HSTS आदि
- **CORS** — उत्पत्ति अनुमतियाँ
- **Health check** — `/health`
- **Cache layer** — इन-प्रोकेस कैश
- **Django ORM accelerator** — PostgreSQL COPY bulk insert
- **DRF serializer accelerator** — queryset → JSON
- **JWT validation** — नेटवर्क कॉल रहित
- **HTML/CSS/JS minification**
- **HTML → Markdown** — एजेंटिक उपयोग हेतु
- **Telemetry** — तैयार रिपोर्ट
- **Background worker (zero-GIL)** — बैकग्राउंड टास्क

---

## 🔍 स्थिति और डायग्नोस्टिक्स

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.3.12', 'native_extension': True, 'features': [...]}
```

---

## 🔗 लिंक

- वेबसाइट: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- रिपॉज़िटरी: https://github.com/B4N1-com/b4n1-boost
- लाइसेंसिंग: https://b4n1.com/licensing या `b4n1@b4n1.com`
- Changelog: [CHANGELOG.md](../CHANGELOG.md)

---

## 📄 लाइसेंस

**Business Source License 1.1 (BUSL-1.1)**।

- **मुफ़्त** विकास, मूल्यांकन, परीक्षण, व्यक्तिगत परियोजनाओं और **$100K USD** से कम वार्षिक आय वाले स्टार्टअप्स के लिए।
- **व्यावसायिक लाइसेंस** आवश्यक: संगठन जिनकी आय **$100K USD** या अधिक हो, सरकारी एजेंसियाँ और सार्वजनिक निविदाएँ।
- **Change Date** (4 वर्ष) के बाद → **Apache License 2.0**।

पूरा पाठ [LICENSE](../LICENSE) में देखें।

---

_b4n1-boost: पायथन एक्सेलरेटर। JSON 10x तेज़। कंप्रेशन 28x तेज़। पारदर्शी मिडलवेयर। B4N1 द्वारा ❤️ से निर्मित._
