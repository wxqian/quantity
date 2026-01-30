# 架构设计方案 (Architecture Design Proposal)

## 1. 系统概览 (System Overview)
本项目采用 **微服务化/模块化** 架构，核心分为数据层、引擎层、服务层和交互层。
语言选择：**Python 3.10+** (后端/策略), **TypeScript/React** (前端).
数据库选择：**PostgreSQL (TimescaleDB extension)** (时序数据/交易记录), **Redis** (实时行情/缓存).

## 2. 模块划分 (Module Breakdown)

### 2.1 数据接入层 (Data Ingestion Layer)
负责对接不同市场和券商的数据接口。
- **MarketDataAdapter (抽象基类)**
    - `subscribe(symbol)`: 订阅行情
    - `get_history(symbol, start, end)`: 获取历史数据
- **实现类**:
    - `SinaAdapter` (A股免费行情)
    - `FutuAdapter` (港/美股)
    - `IBAdapter` (盈透证券)

### 2.2 交易执行层 (Execution Layer)
负责订单路由和账户管理。
- **BrokerDriver (抽象基类)**
    - `place_order(order)`
    - `cancel_order(order_id)`
    - `get_account_info()`
- **实现类**:
    - `RealBrokerDriver`: 对接真实券商 API.
    - `PaperBrokerDriver`: **模拟交易核心**。
        - 接收订单后，订阅对应行情的实时 Tick。
        - 根据买一/卖一价和成交量判断是否成交（Match Engine）。
        - 模拟计算滑点 (Slippage) 和 手续费 (Commission)。
        - 维护虚拟的账户资金和持仓。
- **Multi-Account Support**: 系统维护一个 `AccountManager`，映射 `Strategy` -> `Account` -> `BrokerDriver`。

### 2.3 策略引擎 (Strategy Engine)
核心事件驱动引擎。
- **EventLoop**: 处理 `EVENT_TICK`, `EVENT_ORDER`, `EVENT_TIMER` 等事件。
- **StrategyContext**: 为策略提供上下文（数据、账户权益等）。
- **BacktestEngine**: 继承自核心引擎，但时间轴由历史数据驱动，而非实时时间。支持“重放”功能。

### 2.4 AI Agent 层 (AI Integration)
- **Prompt Manager**: 管理生成量化策略的 Prompt 模板。
- **Code Generator**: 接收自然语言，通过 LLM (OpenAI/DeepSeek) 生成 Python 策略代码片段。
- **Validator**: 对生成的策略进行静态代码检查和简单的逻辑验证。

### 2.5 数据存储 (Data Storage)
- **Quotes Table**: `(timestamp, symbol, open, high, low, close, volume, source)`
- **Orders Table**: `(order_id, strategy_id, symbol, direction, price, volume, status)`
- **Trades Table**: `(trade_id, order_id, price, volume, timestamp)`
- **Strategy Table**: `(strategy_id, name, logic_code, status, parameters)`

## 3. Web 交互层 (Web Dashboard)
- **Backend API**: FastAPI 提供 RESTful API 和 WebSocket 推送。
- **Frontend**: React 单页应用。
    - **Dashboard**: P&L 曲线，实时持仓。
    - **Strategy Editor**: 在线编辑器 + 自然语言输入框 (Chat Interface)。

## 4. 开发计划 (Roadmap)
1.  **Phase 1**: 搭建基础框架，连通 A 股模拟数据源，实现简单均线策略的回测。
2.  **Phase 2**: 接入 LLM，实现“文字转策略”的原型。
3.  **Phase 3**: 实盘对接（如富途牛牛/IB），完善多账户管理系统。
4.  **Phase 4**: 完善 Web Dashboard，支持可视化回测报告。
