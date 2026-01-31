# 订单模型规范 (Order Model Spec)

## 描述
代表交易订单。

## Schema (Draft)

```json
{
  "order_id": "string",     // 订单ID
  "symbol": "string",       // 标的代码
  "direction": "string",    // 方向: BUY (买), SELL (卖)
  "offset": "string",       // 开平: OPEN (开), CLOSE (平), CLOSE_TODAY (平今)
  "type": "string",         // 类型: LIMIT (限价), MARKET (市价)
  "price": "float",         // 价格
  "volume": "float",        // 总数量
  "filled_volume": "float", // 已成交数量
  "status": "string",       // 状态: SUBMITTED, ACCEPTED, PARTIAL, FILLED, CANCELED, REJECTED
  "create_time": "string",  // 创建时间
  "update_time": "string",  // 更新时间
  "message": "string"       // 错误信息或备注
}
```
