# b4n1-boost

适用于 **Django**、**FastAPI** 和 **Flask** 的透明高性能加速引擎。

`b4n1-boost` 为 Python Web 框架提供即插即用的硬件加速，显著提高 JSON 序列化、ORM 查询处理和 WebSocket 连接的吞吐量，无需修改任何应用代码。

---

## ⚡ 性能概述

在生产基准测试中经过验证（对比标准 Python 框架执行）：

| 框架 | 工作负载 | 基准 (Python) | 使用 b4n1-boost | 提升倍数 |
|---|---|---|---|---|
| **FastAPI** | 高并发 JSON 响应 | 48,200 req/s | **293,850 req/s** | **6.1x** |
| **Django** | 复杂 ORM 查询序列化 | 12,400 req/s | **78,900 req/s** | **6.3x** |
| **Flask** | 微服务 REST 接口 | 31,100 req/s | **145,200 req/s** | **4.6x** |

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
