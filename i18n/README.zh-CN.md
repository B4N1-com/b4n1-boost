# b4n1-boost

适用于 **Django**、**FastAPI** 和 **Flask** 的透明高性能加速引擎。

`b4n1-boost` 为 Python Web 框架提供即插即用的原生 Rust 中间件：零拷贝响应直通路径、无 GIL 的原生 gzip/Brotli 压缩和原生 JSON 引擎，无需修改任何应用代码。

---

> 请在你的应用中进行端到端测量 — 实际收益取决于工作负载。

---

## 📦 安装

```bash
pip install b4n1-boost
```

---

## 🚀 快速开始

```python
import b4n1_boost

# 为 Django 启用
b4n1_boost.install_django()

# 为 FastAPI 启用
b4n1_boost.install_fastapi()

# 为 Flask 启用
b4n1_boost.install_flask()
```
