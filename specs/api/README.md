# API 规范指南 (API Specs)

本目录用于存放系统对外或模块间的接口定义。

## 推荐格式

我们推荐使用 **RESTful 风格** (针对 HTTP) 或 **AsyncAPI** (针对 WebSocket/MQ)。
在简单的文档驱动开发中，可以使用 Markdown 表格描述。

## 示例: 历史K线接口

### GET /api/v1/history/bars

获取指定标的的历史 K 线数据。

**请求参数 (Query Parameters)**:

| 参数名 | 类型 | 必选 | 描述 | 示例 |
| :--- | :--- | :--- | :--- | :--- |
| `symbol` | string | 是 | 标的代码 | `000001.SZ` |
| `interval` | string | 否 | K线周期 (1m, 1d) | `1d` |
| `start_time` | string | 是 | 开始时间 (ISO8601) | `2023-01-01T00:00:00` |
| `end_time` | string | 是 | 结束时间 (ISO8601) | `2023-01-31T00:00:00` |

**响应 (Response)**:

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "datetime": "2023-01-01T09:30:00",
      "open": 10.0,
      "high": 10.5,
      "low": 9.8,
      "close": 10.2,
      "volume": 10000
    }
  ]
}
```

## 规范检查点
1.  URL 命名是否符合 REST 风格 (名词复数)？
2.  状态码是否规范 (200, 400, 404, 500)？
3.  时间格式是否统一 (推荐 ISO 8601)？
