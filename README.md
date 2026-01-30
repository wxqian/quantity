# Quantitative Trading Framework (QTF)

## 简介 (Introduction)
本项目旨在打造一个支持 **A股、港股、美股** 的多市场、多券商量化交易框架。它专为灵活策略设计，支持从自然语言策略生成到实盘交易的全流程。

The goal of this project is to build a quantitative trading framework that supports **A-shares, Hong Kong stocks, and US stocks**. It is designed for flexible strategies, supporting the entire process from natural language strategy generation to live trading.

## 核心特性 (Key Features)
1.  **多市场支持 (Multi-market Support)**: 覆盖 A股 (CN), 港股 (HK), 美股 (US).
2.  **多券商接入 (Multi-broker Access)**: 通过适配器模式支持不同券商的数据获取与交易接口.
3.  **策略引擎 (Strategy Engine)**:
    -   支持不同账号、不同市场的独立策略运行.
    -   支持策略热更新 (Hot Reload).
    -   **模拟交易 (Paper Trading)**: 提供高保真模拟环境，验证策略在实时行情下的表现，包含滑点和手续费模拟.
    -   **策略重放/回测 (Replay/Backtesting)**: 支持修改策略后基于历史数据进行验证.
4.  **可视化面板 (Dashboard)**: 实时展示各账户交易记录、持仓及盈亏情况.
5.  **AI 驱动 (AI-Powered)**:
    -   **自然语言策略生成**: 直接通过自然语言描述添加交易原则和策略.
    -   **大模型集成**: 内置 LLM 接口，将自然语言转化为可执行代码或配置.
6.  **现代化技术栈 (Modern Tech Stack)**:
    -   后端: Python (FastAPI) + TimescaleDB.
    -   前端: React + Vite + Ant Design.

## 快速开始 (Quick Start)
*(Coming Soon)*

## 文档 (Documentation)
详细的设计文档和开发指南请参考 `docs/` 目录：
- [架构设计 (Architecture Design)](docs/design.md)
