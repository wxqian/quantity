"""
策略基类 (Base Strategy)
定义策略的抽象接口
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from qtf.engine.context import StrategyContext
    from qtf.core.events import Event
    from qtf.data.models import Quote, Bar
    from qtf.execution.models import Order


class BaseStrategy(ABC):
    """
    策略抽象基类
    所有交易策略都需要继承此类
    """
    
    def __init__(self, name: str = "", params: Dict[str, Any] = None):
        self.name = name
        self.params = params or {}
        self.context: Optional["StrategyContext"] = None
        self._initialized: bool = False
        self._running: bool = False
    
    @property
    def initialized(self) -> bool:
        """是否已初始化"""
        return self._initialized
    
    @property
    def running(self) -> bool:
        """是否运行中"""
        return self._running
    
    def set_context(self, context: "StrategyContext") -> None:
        """设置策略上下文"""
        self.context = context
    
    # ============ 生命周期钩子 ============
    
    @abstractmethod
    def on_init(self) -> None:
        """
        策略初始化
        在策略启动前调用，用于订阅行情、初始化变量等
        """
        pass
    
    @abstractmethod
    def on_start(self) -> None:
        """
        策略启动
        策略正式开始运行时调用
        """
        pass
    
    @abstractmethod
    def on_stop(self) -> None:
        """
        策略停止
        策略停止时调用，用于清理资源
        """
        pass
    
    # ============ 事件处理 ============
    
    def on_tick(self, quote: "Quote") -> None:
        """
        处理实时行情
        Args:
            quote: 实时行情数据
        """
        pass
    
    def on_bar(self, bar: "Bar") -> None:
        """
        处理K线数据
        Args:
            bar: K线数据
        """
        pass
    
    def on_order(self, order: "Order") -> None:
        """
        处理订单回报
        Args:
            order: 订单数据
        """
        pass
    
    def on_trade(self, trade: Any) -> None:
        """
        处理成交回报
        Args:
            trade: 成交数据
        """
        pass
    
    def on_timer(self, timer_id: str) -> None:
        """
        处理定时器事件
        Args:
            timer_id: 定时器ID
        """
        pass
    
    def on_event(self, event: "Event") -> None:
        """
        处理自定义事件
        Args:
            event: 事件对象
        """
        pass
    
    # ============ 交易接口 ============
    
    def buy(
        self,
        symbol: str,
        price: float,
        volume: int,
        order_type: str = "LIMIT"
    ) -> Optional[str]:
        """
        买入
        Args:
            symbol: 标的代码
            price: 价格
            volume: 数量
            order_type: 订单类型
        Returns:
            Optional[str]: 订单ID
        """
        if self.context:
            return self.context.buy(symbol, price, volume, order_type)
        return None
    
    def sell(
        self,
        symbol: str,
        price: float,
        volume: int,
        order_type: str = "LIMIT"
    ) -> Optional[str]:
        """
        卖出
        Args:
            symbol: 标的代码
            price: 价格
            volume: 数量
            order_type: 订单类型
        Returns:
            Optional[str]: 订单ID
        """
        if self.context:
            return self.context.sell(symbol, price, volume, order_type)
        return None
    
    def cancel(self, order_id: str) -> bool:
        """
        撤单
        Args:
            order_id: 订单ID
        Returns:
            bool: 是否成功
        """
        if self.context:
            return self.context.cancel_order(order_id)
        return False
