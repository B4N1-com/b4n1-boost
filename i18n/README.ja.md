<p align="center">
  <img src="../docs/cover.png" alt="B4N1 Boost — More speed. More power. Greater potential." width="100%" />
</p>

# b4n1-boost

**Django**、**FastAPI**、**Flask**のための透過的超高速アクセラレーションエンジン。

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-mdBook-blue)](https://b4n1-com.github.io/b4n1-boost/)
[![PyPI](https://badge.fury.io/py/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![Python versions](https://img.shields.io/pypi/pyversions/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![PyPI downloads](https://img.shields.io/pypi/dm/b4n1-boost.svg)](https://pypi.org/project/b4n1-boost/)
[![Pepy downloads](https://img.shields.io/pepy/dt/b4n1-boost.svg)](https://pepy.tech/project/b4n1-boost)
[![npm](https://img.shields.io/npm/v/b4n1-boost.svg)](https://www.npmjs.com/package/b4n1-boost)
[![npm downloads](https://img.shields.io/npm/dm/b4n1-boost.svg)](https://www.npmjs.com/package/b4n1-boost)
[![NuGet](https://img.shields.io/nuget/v/B4N1.Boost.svg)](https://www.nuget.org/packages/B4N1.Boost)
[![NuGet downloads](https://img.shields.io/nuget/dt/B4N1.Boost.svg)](https://www.nuget.org/packages/B4N1.Boost)
[![Maven Central](https://img.shields.io/maven-central/v/com.b4n1/boost.svg)](https://central.sonatype.com/artifact/com.b4n1/boost)
[![RubyGems](https://img.shields.io/gem/v/b4n1-boost.svg)](https://rubygems.org/gems/b4n1-boost)
[![Packagist](https://img.shields.io/packagist/v/b4n1/boost.svg)](https://packagist.org/packages/b4n1/boost)
[![Go Reference](https://pkg.go.dev/badge/github.com/B4N1-com/b4n1-boost/sdks/go.svg)](https://pkg.go.dev/github.com/B4N1-com/b4n1-boost/sdks/go)
[![Tests](https://img.shields.io/badge/tests-948%20passing-brightgreen)](https://pypi.org/project/b4n1-boost/)

`b4n1-boost`は、Python Webフレームワーク向けにプラグアンドプレイのハードウェアアクセラレーションを提供します。アプリケーションのコードを変更することなく、JSONシリアライズ、ORMクエリ処理、WebSocket接続のスループットを大幅に向上させます。

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
