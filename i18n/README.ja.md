# b4n1-boost

**Django**、**FastAPI**、**Flask**のための透過的超高速アクセラレーションエンジン。

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

4つのレジストリで利用可能（ネイティブコア + EULA同梱）:

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
