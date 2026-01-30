"""
券商驱动基类 (Broker Driver Base)
定义交易执行的抽象接口
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from qtf.execution.models import Order, Position, Account


class BrokerDriver(ABC):
    """
    券商驱动抽象基类
    所有券商接口适配器都需要继承此类
    """
    
    def __init__(self, name: str = "", config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}
        self._connected: bool = False
        self._account: Optional[Account] = None
    
    @property
    def connected(self) -> bool:
        """是否已连接"""
        return self._connected
    
    @property
    def account(self) -> Optional[Account]:
        """当前账户"""
        return self._account
    
    # ============ 连接管理 ============
    
    @abstractmethod
    async def connect(self) -> bool:
        """
        连接券商接口
        Returns:
            bool: 是否连接成功
        """
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        """断开连接"""
        pass
    
    # ============ 订单管理 ============
    
    @abstractmethod
    async def place_order(self, order: Order) -> str:
        """
        下单
        Args:
            order: 订单对象
        Returns:
            str: 订单ID
        """
        pass
    
    @abstractmethod
    async def cancel_order(self, order_id: str) -> bool:
        """
        撤单
        Args:
            order_id: 订单ID
        Returns:
            bool: 是否撤单成功
        """
        pass
    
    @abstractmethod
    async def get_order(self, order_id: str) -> Optional[Order]:
        """
        查询订单
        Args:
            order_id: 订单ID
        Returns:
            Optional[Order]: 订单对象
        """
        pass
    
    @abstractmethod
    async def get_orders(
        self,
        symbol: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Order]:
        """
        查询订单列表
        Args:
            symbol: 标的代码 (可选)
            status: 订单状态 (可选)
        Returns:
            List[Order]: 订单列表
        """
        pass
    
    # ============ 持仓管理 ============
    
    @abstractmethod
    async def get_positions(self) -> List[Position]:
        """
        获取持仓列表
        Returns:
            List[Position]: 持仓列表
        """
        pass
    
    @abstractmethod
    async def get_position(self, symbol: str) -> Optional[Position]:
        """
        获取指定标的持仓
        Args:
            symbol: 标的代码
        Returns:
            Optional[Position]: 持仓对象
        """
        pass
    
    # ============ 账户管理 ============
    
    @abstractmethod
    async def get_account_info(self) -> Account:
        """
        获取账户信息
        Returns:
            Account: 账户信息
        """
        pass
    
    @abstractmethod
    async def refresh_account(self) -> None:
        """刷新账户数据"""
        pass
