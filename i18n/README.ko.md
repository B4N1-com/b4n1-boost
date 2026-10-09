<p align="center">
  <img src="../docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

# b4n1-boost

**파이썬 가속기.** Django·FastAPI·Flask용 고속 네이티브 미들웨어 — JSON 10배, 압축 28배 빠릅니다.

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

## ⚡ 성능 한눈에 보기

| 구성 요소 | 지표 | stdlib 대비 |
|---|---|---|
| **JSON dumps** (native engine) | 10.5배 빠름 | 중간 dict (20명) |
| **JSON dumps** (native engine) | 8.5배 빠름 | 큰 dict (500명) |
| **Gzip** (네이티브) | 1.47배 빠름 | 1MB 페이로드 |
| **Zstd** (네이티브) | 28배 빠름 | 1MB 페이로드 |
| **Brotli** (네이티브) | 최고 압축률 | 1MB 페이로드 |
| **DRF serializer** | 5-10배 빠름 | queryset → JSON |
| **Django ORM** | PostgreSQL COPY | 네이티브 벌크 삽입 |
| **휠 크기** | ~1.4MB | native, no compiler needed |

---

## 📦 설치

```bash
pip install b4n1-boost
```

Linux(x86_64 + aarch64), macOS(x86_64 + Apple Silicon), Windows(x86_64)용 사전 빌드 네이티브 휠. 컴파일러가 필요 없습니다.

**지원 Python 버전:** 3.10, 3.11, 3.12, 3.13

---

## 🚀 빠른 시작

### Django
```python
import b4n1_boost
report = b4n1_boost.install_django()
# settings.MIDDLEWARE에 DjangoBoostMiddleware를 추가합니다
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

### 자동 감지
```python
import b4n1_boost
b4n1_boost.install()   # 프레임워크를 감지하고 알맞은 미들웨어를 설치합니다
```

---

## 🔧 기능

- **JSON 직렬화** — stdlib 대비 최대 10배
- **압축** — gzip·zstd·brotli, GIL 없이
- **Content-Type 인지 미들웨어** — 자동 압축
- **ETag / 304** — 응답 캐싱
- **Rate limiting** — 과요청 방어
- **Security headers** — HSTS 등
- **CORS** — 출처 허용
- **Health check** — `/health`
- **Cache layer** — 인프로세스 캐시
- **Django ORM 가속** — PostgreSQL COPY 벌크 삽입
- **DRF serializer 가속** — queryset → JSON
- **JWT 검증** — 네트워크 호출 없음
- **HTML/CSS/JS 축소**
- **HTML → Markdown** — 에이전트용
- **Telemetry** — 준비된 리포트
- **백그라운드 워커 (zero-GIL)** — 파이썬을 막지 않는 백그라운드 작업

---

## 🔍 상태 및 진단

```python
import b4n1_boost
print(b4n1_boost.status())
# {'version': '0.3.13', 'native_extension': True, 'features': [...]}
```

---

## 🔗 링크

- 웹사이트: https://b4n1.com
- PyPI: https://pypi.org/project/b4n1-boost
- 저장소: https://github.com/B4N1-com/b4n1-boost
- 라이선싱: https://b4n1.com/licensing 또는 `b4n1@b4n1.com`
- 변경 이력: [CHANGELOG.md](../CHANGELOG.md)

---

## 📄 라이선스

**Business Source License 1.1 (BUSL-1.1)**.

- 개발·평가·테스트·개인 프로젝트 및 연 매출 **10만 달러 미만** 스타트업은 **무료**.
- 매출 **10만 달러 이상** 조직, 정부 기관, 공개 입찰에는 **상업용 라이선스** 필요.
- **Change Date**(4년) 이후 → **Apache License 2.0**.

전문은 [LICENSE](../LICENSE)를 참조하세요.

---

_b4n1-boost: 파이썬 가속기. JSON 10배, 압축 28배. 투명한 미들웨어. B4N1이 ❤️로 만들었습니다._
