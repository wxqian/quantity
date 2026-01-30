"""
交易相关数据模型 (Trading Data Models)
定义订单、持仓、账户等数据结构
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class OrderDirection(Enum):
    """订单方向"""
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    """订单类型"""
    LIMIT = "LIMIT"           # 限价单
    MARKET = "MARKET"         # 市价单
    STOP = "STOP"             # 止损单
    STOP_LIMIT = "STOP_LIMIT" # 止损限价单


class OrderStatus(Enum):
    """订单状态"""
    PENDING = "PENDING"       # 待提交
    SUBMITTED = "SUBMITTED"   # 已提交
    PARTIAL = "PARTIAL"       # 部分成交
    FILLED = "FILLED"         # 全部成交
    CANCELLED = "CANCELLED"   # 已撤销
    REJECTED = "REJECTED"     # 已拒绝
    EXPIRED = "EXPIRED"       # 已过期


@dataclass
class Order:
    """
    订单数据
    """
    symbol: str                                    # 标的代码
    direction: OrderDirection                      # 方向
    price: float                                   # 价格
    volume: int                                    # 数量
    
    order_id: str = ""                            # 订单ID
    order_type: OrderType = OrderType.LIMIT       # 订单类型
    status: OrderStatus = OrderStatus.PENDING     # 订单状态
    
    filled_volume: int = 0                        # 已成交数量
    filled_price: float = 0.0                     # 成交均价
    
    strategy_id: Optional[str] = None             # 策略ID
    account_id: Optional[str] = None              # 账户ID
    
    create_time: datetime = field(default_factory=datetime.now)
    update_time: Optional[datetime] = None
    
    # 扩展字段
    stop_price: Optional[float] = None            # 止损价
    expire_time: Optional[datetime] = None        # 过期时间
    remark: str = ""                              # 备注


@dataclass
class Position:
    """
    持仓数据
    """
    symbol: str                          # 标的代码
    volume: int                          # 持仓数量
    available: int                       # 可用数量
    
    cost_price: float = 0.0             # 成本价
    current_price: float = 0.0          # 当前价
    
    market_value: float = 0.0           # 市值
    profit: float = 0.0                 # 浮动盈亏
    profit_ratio: float = 0.0           # 盈亏比例
    
    direction: str = "LONG"             # 持仓方向 (LONG/SHORT)
    account_id: Optional[str] = None    # 账户ID
    
    update_time: datetime = field(default_factory=datetime.now)


@dataclass
class Account:
    """
    账户数据
    """
    account_id: str                      # 账户ID
    
    balance: float = 0.0                # 账户余额
    available: float = 0.0              # 可用资金
    frozen: float = 0.0                 # 冻结资金
    
    market_value: float = 0.0           # 持仓市值
    total_asset: float = 0.0            # 总资产
    
    profit: float = 0.0                 # 当日盈亏
    profit_ratio: float = 0.0           # 当日收益率
    
    currency: str = "CNY"               # 货币
    broker: str = ""                    # 券商名称
    
    update_time: datetime = field(default_factory=datetime.now)
