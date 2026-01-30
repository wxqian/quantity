"""
数据模型 (Data Models)
定义行情相关的数据结构
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Quote:
    """
    实时行情数据
    """
    symbol: str                          # 标的代码
    last_price: float                    # 最新价
    timestamp: datetime = field(default_factory=datetime.now)
    
    # 买卖盘
    bid_price_1: float = 0.0            # 买一价
    bid_volume_1: int = 0               # 买一量
    ask_price_1: float = 0.0            # 卖一价
    ask_volume_1: int = 0               # 卖一量
    
    # 五档行情 (可选)
    bid_price_2: Optional[float] = None
    bid_volume_2: Optional[int] = None
    ask_price_2: Optional[float] = None
    ask_volume_2: Optional[int] = None
    
    bid_price_3: Optional[float] = None
    bid_volume_3: Optional[int] = None
    ask_price_3: Optional[float] = None
    ask_volume_3: Optional[int] = None
    
    bid_price_4: Optional[float] = None
    bid_volume_4: Optional[int] = None
    ask_price_4: Optional[float] = None
    ask_volume_4: Optional[int] = None
    
    bid_price_5: Optional[float] = None
    bid_volume_5: Optional[int] = None
    ask_price_5: Optional[float] = None
    ask_volume_5: Optional[int] = None
    
    # 统计数据
    open_price: float = 0.0             # 开盘价
    high_price: float = 0.0             # 最高价
    low_price: float = 0.0              # 最低价
    pre_close: float = 0.0              # 昨收价
    volume: int = 0                     # 成交量
    amount: float = 0.0                 # 成交额
    
    # 数据源
    source: str = ""                    # 数据来源


@dataclass
class Bar:
    """
    K线数据
    """
    symbol: str                          # 标的代码
    interval: str                        # 周期 (1m, 5m, 15m, 30m, 1h, 1d)
    timestamp: datetime = field(default_factory=datetime.now)
    
    open: float = 0.0                   # 开盘价
    high: float = 0.0                   # 最高价
    low: float = 0.0                    # 最低价
    close: float = 0.0                  # 收盘价
    volume: int = 0                     # 成交量
    amount: float = 0.0                 # 成交额
    
    # 可选字段
    turnover: Optional[float] = None    # 换手率
    vwap: Optional[float] = None        # 成交量加权平均价
    
    source: str = ""                    # 数据来源


@dataclass
class Trade:
    """
    逐笔成交
    """
    symbol: str
    price: float
    volume: int
    timestamp: datetime
    direction: str = ""                 # B = 买入, S = 卖出, N = 中性
    source: str = ""
