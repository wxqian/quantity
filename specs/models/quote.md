# 行情模型规范 (Quote Model Spec)

## 描述
代表特定标的的市场数据快照 (Tick)。

## Schema (Draft)

```json
{
  "symbol": "string",       // 标的代码, 例如 "000001.SZ"
  "datetime": "string",     // 时间, ISO 8601 格式
  "open": "float",          // 开盘价
  "high": "float",          // 最高价
  "low": "float",           // 最低价
  "close": "float",         // 最新价
  "volume": "float",        // 成交量
  "last_close": "float",    // 昨收价
  "bid_prices": ["float"],  // 买一到买五价格列表
  "bid_volumes": ["float"], // 买一到买五量列表
  "ask_prices": ["float"],  // 卖一到卖五价格列表
  "ask_volumes": ["float"], // 卖一到卖五量列表
  "extra": "object"         // 数据源特定字段
}
```
