"""
模拟行情适配器 (Simulated Market Data Adapter)
产生随机行情用于测试
"""

import asyncio
import random
from datetime import datetime, timedelta
from typing import List, Optional

from qtf.data.base import MarketDataAdapter
from qtf.data.models import Quote, Bar


class SimulatedAdapter(MarketDataAdapter):
    """
    模拟行情适配器
    生成随机漫步的行情数据
    """
    
    def __init__(self):
        super().__init__(name="simulated")
        self._prices = {}
        self._running = False
        self._task = None
    
    async def connect(self) -> bool:
        """连接"""
        self._connected = True
        print(f"[{self.name}] Connected")
        self._running = True
        self._task = asyncio.create_task(self._run_simulation())
        return True
    
    async def disconnect(self) -> None:
        """断开"""
        self._running = False
        if self._task:
            self._task.cancel()
        self._connected = False
        print(f"[{self.name}] Disconnected")
    
    async def subscribe(self, symbols: List[str]) -> bool:
        """订阅"""
        for s in symbols:
            if s not in self._prices:
                self._prices[s] = 100.0  # 初始价格
        print(f"[{self.name}] Subscribed: {symbols}")
        return True
    
    async def unsubscribe(self, symbols: List[str]) -> bool:
        """取消订阅"""
        print(f"[{self.name}] Unsubscribed: {symbols}")
        return True
    
    async def get_history(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = "1d"
    ) -> List[Bar]:
        """获取历史 (模拟)"""
        bars = []
        current = start
        price = 100.0
        while current <= end:
            price = price * (1 + random.uniform(-0.02, 0.02))
            bar = Bar(
                symbol=symbol,
                interval=interval,
                timestamp=current,
                open=price,
                high=price * 1.01,
                low=price * 0.99,
                close=price,
                volume=random.randint(1000, 10000),
                source=self.name
            )
            bars.append(bar)
            current += timedelta(days=1)
        return bars
    
    async def get_quote(self, symbol: str) -> Optional[Quote]:
        """获取快照"""
        price = self._prices.get(symbol, 100.0)
        return Quote(
            symbol=symbol,
            last_price=price,
            timestamp=datetime.now(),
            source=self.name
        )

    async def _run_simulation(self):
        """运行模拟生成器"""
        while self._running:
            for symbol in list(self._prices.keys()):
                # 随机波动
                old_price = self._prices[symbol]
                change = random.uniform(-0.005, 0.005)
                new_price = old_price * (1 + change)
                self._prices[symbol] = new_price
                
                # 生成 Quote
                quote = Quote(
                    symbol=symbol,
                    last_price=new_price,
                    open_price=old_price,
                    high_price=max(old_price, new_price),
                    low_price=min(old_price, new_price),
                    volume=random.randint(1, 100),
                    timestamp=datetime.now(),
                    source=self.name
                )
                
                # 推送
                await self._on_quote(quote)
            
            await asyncio.sleep(1)  # 1秒推送一次
