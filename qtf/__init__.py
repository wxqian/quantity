"""
Quantitative Trading Framework (QTF)
多市场量化交易框架

支持 A股、港股、美股 的多市场、多券商量化交易框架
"""

__version__ = "0.1.0"
__author__ = "QTF Team"

# 核心模块
from qtf.core.events import Event, EventType
from qtf.core.exceptions import QTFError

# 数据层
from qtf.data.base import MarketDataAdapter
from qtf.data.models import Quote, Bar

# 执行层
from qtf.execution.base import BrokerDriver
from qtf.execution.models import Order, Position, Account

# 策略引擎
from qtf.engine.base import BaseStrategy
from qtf.engine.context import StrategyContext
from qtf.engine.backtest import BacktestEngine

# 配置
from qtf.config import settings

__all__ = [
    # 版本
    "__version__",
    "__author__",
    # 核心
    "Event",
    "EventType",
    "QTFError",
    # 数据
    "MarketDataAdapter",
    "Quote",
    "Bar",
    # 执行
    "BrokerDriver",
    "Order",
    "Position",
    "Account",
    # 策略
    "BaseStrategy",
    "StrategyContext",
    "BacktestEngine",
    # 配置
    "settings",
]
