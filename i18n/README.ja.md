# b4n1-boost

**Django**、**FastAPI**、**Flask**のための透過的超高速アクセラレーションエンジン。

`b4n1-boost` は、Python Webフレームワーク向けのプラグアンドプレイ型ネイティブ Rust ミドルウェアを提供します：コピーフリーのパススルーレスポンス、GILフリーのネイティブ gzip/Brotli 圧縮、ネイティブ JSON エンジン。アプリケーションコードの変更は不要です。

---

> アクセラレーションは自身のアプリケーションでエンドツーエンドで計測してください — 実際の効果はワークロードに依存します。

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
