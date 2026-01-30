"""
事件系统 (Event System)
定义系统中使用的各类事件及事件循环
"""

from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional


class EventType(Enum):
    """事件类型枚举"""
    # 行情事件
    TICK = "tick"              # 实时行情
    BAR = "bar"                # K线数据
    
    # 交易事件
    ORDER = "order"            # 订单事件
    TRADE = "trade"            # 成交事件
    POSITION = "position"      # 持仓变化
    ACCOUNT = "account"        # 账户变化
    
    # 系统事件
    TIMER = "timer"            # 定时器事件
    LOG = "log"                # 日志事件
    ERROR = "error"            # 错误事件
    
    # 引擎事件
    ENGINE_START = "engine_start"
    ENGINE_STOP = "engine_stop"
    STRATEGY_START = "strategy_start"
    STRATEGY_STOP = "strategy_stop"


@dataclass
class Event:
    """
    事件基类
    所有事件都继承自此类
    """
    type: EventType
    data: Any = None
    timestamp: datetime = field(default_factory=datetime.now)
    source: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        if isinstance(self.type, str):
            self.type = EventType(self.type)


@dataclass
class TickEvent(Event):
    """Tick 行情事件"""
    symbol: str = ""
    last_price: float = 0.0
    bid_price: float = 0.0
    ask_price: float = 0.0
    bid_volume: int = 0
    ask_volume: int = 0
    volume: int = 0
    
    def __post_init__(self):
        self.type = EventType.TICK


@dataclass 
class OrderEvent(Event):
    """订单事件"""
    order_id: str = ""
    symbol: str = ""
    direction: str = ""  # BUY/SELL
    price: float = 0.0
    volume: int = 0
    status: str = ""     # PENDING/FILLED/CANCELLED/REJECTED
    
    def __post_init__(self):
        self.type = EventType.ORDER


@dataclass
class TradeEvent(Event):
    """成交事件"""
    trade_id: str = ""
    order_id: str = ""
    symbol: str = ""
    direction: str = ""
    price: float = 0.0
    volume: int = 0
    commission: float = 0.0
    
    def __post_init__(self):
        self.type = EventType.TRADE
