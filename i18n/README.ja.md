<p align="center">
  <img src="../docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

# b4n1-boost

**Django**、**FastAPI**、**Flask**のための透過的超高速アクセラレーションエンジン。

`b4n1-boost`は、Python Webフレームワーク向けにプラグアンドプレイのハードウェアアクセラレーションを提供します。アプリケーションのコードを変更することなく、JSONシリアライズ、ORMクエリ処理、WebSocket接続のスループットを大幅に向上させます。

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-mdBook-blue)](https://b4n1-com.github.io/b4n1-boost/)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![npm](https://img.shields.io/npm/v/b4n1-boost.svg)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet](https://img.shields.io/nuget/v/B4N1.Boost.svg)](https://www.nuget.org/packages/B4N1.Boost)
[![Python](https://img.shields.io/pypi/pyversions/b4n1-boost)](https://pypi.org/project/b4n1-boost/)
[![Tests](https://img.shields.io/badge/tests-772%20passing-brightgreen)](https://pypi.org/project/b4n1-boost/)

[![Total downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FB4N1-com%2Fpublic-repos%2Fmaster%2Fb4n1-boost%2Fbadges%2Fdownloads.json&query=%24.total&label=total%20downloads&color=blue)](https://pypi.org/project/b4n1-boost/)
[![PyPI Downloads/month](https://img.shields.io/pypi/dm/b4n1-boost)](https://pypi.org/project/b4n1-boost/)
[![npm Downloads/month](https://img.shields.io/npm/dm/b4n1-boost)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet Downloads](https://img.shields.io/nuget/dt/B4N1.Boost)](https://www.nuget.org/packages/B4N1.Boost)
[![PyPI total](https://img.shields.io/pepy/dt/b4n1-boost)](https://pepy.tech/project/b4n1-boost)

---

## ⚡ パフォーマンス概要

本番ベンチマークでの計測結果（標準Pythonフレームワーク実行との比較）:

| フレームワーク | ワークロード | ベースライン | b4n1-boost適用時 | 高速化 |
|---|---|---|---|---|
| **FastAPI** | 高並列JSONレスポンス | 48,200 req/s | **293,850 req/s** | **6.1x** |
| **Django** | ORMクエリシリアライズ | 12,400 req/s | **78,900 req/s** | **6.3x** |
| **Flask** | マイクロAPI RESTエンドポイント | 31,100 req/s | **145,200 req/s** | **4.6x** |

---

## 📦 インストール

```bash
pip install b4n1-boost
```

---

## 🚀 クイックスタート

```python
import b4n1_boost

# Django用に有効化
b4n1_boost.install_django()

# FastAPI用に有効化
b4n1_boost.install_fastapi()

# Flask用に有効化
b4n1_boost.install_flask()
```
