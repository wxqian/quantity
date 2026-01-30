"""
策略上下文 (Strategy Context)
为策略提供数据和交易接口
"""

from typing import Dict, Any, Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from qtf.data.base import MarketDataAdapter
    from qtf.execution.base import BrokerDriver
    from qtf.execution.models import Account, Position, Order


class StrategyContext:
    """
    策略运行上下文
    提供策略运行所需的数据查询和交易接口
    """
    
    def __init__(
        self,
        strategy_id: str,
        data_adapter: Optional["MarketDataAdapter"] = None,
        broker: Optional["BrokerDriver"] = None,
    ):
        self.strategy_id = strategy_id
        self.data_adapter = data_adapter
        self.broker = broker
        
        self._variables: Dict[str, Any] = {}
        self._timers: Dict[str, Any] = {}
    
    # ============ 数据查询 ============
    
    def get_current_time(self) -> datetime:
        """获取当前时间"""
        return datetime.now()
    
    def get_account(self) -> Optional["Account"]:
        """获取账户信息"""
        if self.broker:
            return self.broker.account
        return None
    
    async def get_positions(self) -> List["Position"]:
        """获取所有持仓"""
        if self.broker:
            return await self.broker.get_positions()
        return []
    
    async def get_position(self, symbol: str) -> Optional["Position"]:
        """获取指定标的持仓"""
        if self.broker:
            return await self.broker.get_position(symbol)
        return None
    
    async def get_orders(
        self,
        symbol: Optional[str] = None,
        status: Optional[str] = None
    ) -> List["Order"]:
        """获取订单列表"""
        if self.broker:
            return await self.broker.get_orders(symbol, status)
        return []
    
    # ============ 交易接口 ============
    
    def buy(
        self,
        symbol: str,
        price: float,
        volume: int,
        order_type: str = "LIMIT"
    ) -> Optional[str]:
        """
        买入下单
        Returns:
            Optional[str]: 订单ID
        """
        # TODO: 实现下单逻辑
        return None
    
    def sell(
        self,
        symbol: str,
        price: float,
        volume: int,
        order_type: str = "LIMIT"
    ) -> Optional[str]:
        """
        卖出下单
        Returns:
            Optional[str]: 订单ID
        """
        # TODO: 实现下单逻辑
        return None
    
    def cancel_order(self, order_id: str) -> bool:
        """
        撤单
        Returns:
            bool: 是否成功
        """
        # TODO: 实现撤单逻辑
        return False
    
    # ============ 变量管理 ============
    
    def set_var(self, key: str, value: Any) -> None:
        """设置策略变量"""
        self._variables[key] = value
    
    def get_var(self, key: str, default: Any = None) -> Any:
        """获取策略变量"""
        return self._variables.get(key, default)
    
    # ============ 定时器 ============
    
    def set_timer(self, timer_id: str, interval_seconds: int) -> None:
        """
        设置定时器
        Args:
            timer_id: 定时器ID
            interval_seconds: 间隔秒数
        """
        # TODO: 实现定时器逻辑
        pass
    
    def cancel_timer(self, timer_id: str) -> None:
        """取消定时器"""
        if timer_id in self._timers:
            del self._timers[timer_id]
    
    # ============ 日志 ============
    
    def log(self, message: str, level: str = "INFO") -> None:
        """
        记录日志
        Args:
            message: 日志内容
            level: 日志级别 (DEBUG, INFO, WARNING, ERROR)
        """
        # TODO: 实现日志记录
        print(f"[{self.strategy_id}] [{level}] {message}")
