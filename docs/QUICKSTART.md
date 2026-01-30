# 快速开始 (Quickstart Guide)

本指南将帮助您快速部署和运行 QTF 量化交易框架。

## 前置要求 (Prerequisites)

*   **Python**: 3.10 或更高版本
*   **Git**: 用于代码版本控制
*   **Docker & Docker Compose** (推荐): 用于快速部署
*   **Redis**: 4.5.0+ (如果不使用 Docker)
*   **PostgreSQL (TimescaleDB)**: 2.0+ (如果不使用 Docker)

---

## 1. Docker 部署 (推荐)

这是最简单、最快捷的运行方式，包含数据库和中间件。

### 1.1 克隆仓库
```bash
git clone https://github.com/your-username/qtf.git
cd qtf
```

### 1.2 启动服务
确保您已安装 Docker 和 Docker Compose。在项目根目录下运行：

```bash
docker-compose up -d
```

此命令将启动三个容器：
*   `qtf-app`: QTF 核心服务 (端口 8000)
*   `qtf-db`: TimescaleDB 数据库 (端口 5432)
*   `qtf-redis`: Redis 缓存 (端口 6379)

可以使用 `docker-compose logs -f` 查看日志。

### 1.3 停止服务
```bash
docker-compose down
```

---

## 2. Linux / 本地环境源码部署

如果您希望在本地进行开发或在没有 Docker 的 Linux 服务器上部署。

### 2.1 克隆仓库
```bash
git clone https://github.com/your-username/qtf.git
cd qtf
```

### 2.2 创建虚拟环境 (可选但推荐)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.3 安装依赖
```bash
pip install .
# 或者安装开发依赖
pip install -e ".[dev]"
```

### 2.4 配置环境
1. 启动 **PostgreSQL (TimescaleDB)** 和 **Redis**。
2. 复制环境变量示例文件：
   ```bash
   cp .env.example .env
   ```
3. 编辑 `.env` 文件，配置数据库连接：
   ```ini
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/quant_db
   REDIS_URL=redis://localhost:6379/0
   ```

### 2.5 启动服务
```bash
python main.py
```
或者直接使用 uvicorn:
```bash
uvicorn qtf.api.server:app --host 0.0.0.0 --port 8000 --reload
```

---

## 3. 验证部署 (Verification)

部署成功后，可以通过以下步骤验证系统是否正常运行。

### 3.1 健康检查 / API 文档
打开浏览器访问：
*   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
*   **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

如果能看到 API 接口文档页面，说明 Web 服务已成功启动。

### 3.2 简单连接测试 (CLI)
可以使用 `curl` 测试根路径（假设根路径有返回，或者测试健康检查接口）：

```bash
curl http://localhost:8000/docs
```

### 3.3 运行单元测试 (可选)
如果是源码部署，可以以此验证环境完整性：
```bash
pytest tests/
```
