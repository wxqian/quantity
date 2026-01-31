# 规范驱动开发 (SDD) 指南

本项目采用 **规范驱动开发 (Spec-Driven Development)** 模式。这意味着我们在编写实现代码 *之前*，先定义数据模型、API 和策略配置。

## 工作流 (Workflow)

1.  **设计 (Design)**: 识别新功能或数据结构的需求。
2.  **规范 (Spec)**: 在 `specs/` 目录下编写规范。
    - **模型 (Models)**: 在 `specs/models/` 下使用 JSON Schema 或 Markdown 表格定义。
    - **API**: 在 `specs/api/` 下使用 OpenAPI (Swagger) 或 Protocol Buffers 定义。
    - **策略 (Strategies)**: 在 `specs/strategies/` 下定义策略配置结构。
3.  **评审 (Review)**: 评审规范以确保覆盖所有需求。
4.  **实现 (Implement)**: 编写 Python 代码以匹配规范。

## 目录结构

- `api/`: API 定义 (REST/WebSocket)。
- `models/`: 核心领域数据模型 (行情 Quote, 订单 Order, 成交 Trade)。
- `strategies/`: 策略参数定义。

## 优势

- **清晰性**: 编码前对数据结构达成一致。
- **一致性**: 不同模块 (回测、实盘) 使用相同的数据结构。
- **文档化**: 规范文件本身即为实时文档。
