# 实现规范 (Implementation Guide)

本指南指导如何将 API 和模型规范转换为 Python 代码。

## 1. 模型实现
*   **单一事实来源**: 代码中的数据类 (Data Class/Pydantic Model) 必须严格对应 `specs/models/` 中的定义。
*   **类型注解**: 必须使用 Python Type Hint。

### 示例
**Spec**:
```json
{ "symbol": "string", "price": "float" }
```

**Code**:
```python
@dataclass
class StockData:
    symbol: str
    price: float
```

## 2. 接口实现
*   **参数校验**: 必须在入口处校验 spec 中定义的必选参数和类型。
*   **错误处理**: 必须返回 spec 中定义的标准错误码和错误信息。

## 3. 策略实现
*   **继承基类**: 所有策略必须继承自 `qtf.engine.base.BaseStrategy`。
*   **参数注入**: 策略参数应通过 `__init__` 或 `params` 字典传入，不应硬编码。

## 4. 测试驱动
*   **先写测试**: 根据 Spec 编写单元测试用例，再编写实现代码。
*   **Mock 数据**: 使用 `qtf.data.simulated` 或 Mock 对象模拟 Spec 定义的数据输入。
