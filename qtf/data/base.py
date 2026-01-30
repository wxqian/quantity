"""
数据适配器基类 (Market Data Adapter Base)
定义数据接入的抽象接口
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional, Callable, Any
from qtf.data.models import Quote, Bar


class MarketDataAdapter(ABC):
    """
    市场数据适配器抽象基类
    所有数据源适配器都需要继承此类
    """
    
    def __init__(self, name: str = ""):
        self.name = name
        self._callbacks: List[Callable] = []
        self._connected: bool = False
    
    @property
    def connected(self) -> bool:
        """是否已连接"""
        return self._connected
    
    @abstractmethod
    async def connect(self) -> bool:
        """
        连接数据源
        Returns:
            bool: 是否连接成功
        """
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        """断开数据源连接"""
        pass
    
    @abstractmethod
    async def subscribe(self, symbols: List[str]) -> bool:
        """
        订阅行情
        Args:
            symbols: 标的代码列表
        Returns:
            bool: 是否订阅成功
        """
        pass
    
    @abstractmethod
    async def unsubscribe(self, symbols: List[str]) -> bool:
        """
        取消订阅
        Args:
            symbols: 标的代码列表
        Returns:
            bool: 是否取消成功
        """
        pass
    
    @abstractmethod
    async def get_history(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = "1d"
    ) -> List[Bar]:
        """
        获取历史K线数据
        Args:
            symbol: 标的代码
            start: 开始时间
            end: 结束时间
            interval: K线周期 (1m, 5m, 15m, 30m, 1h, 1d)
        Returns:
            List[Bar]: K线数据列表
        """
        pass
    
    @abstractmethod
    async def get_quote(self, symbol: str) -> Optional[Quote]:
        """
        获取实时行情快照
        Args:
            symbol: 标的代码
        Returns:
            Optional[Quote]: 行情数据
        """
        pass
    
    def add_callback(self, callback: Callable[[Any], None]) -> None:
        """注册行情回调函数"""
        if callback not in self._callbacks:
            self._callbacks.append(callback)
    
    def remove_callback(self, callback: Callable[[Any], None]) -> None:
        """移除行情回调函数"""
        if callback in self._callbacks:
            self._callbacks.remove(callback)
    
    async def _on_quote(self, quote: Quote) -> None:
        """触发行情回调"""
        for callback in self._callbacks:
            try:
                callback(quote)
            except Exception as e:
                # TODO: 添加日志记录
                pass
