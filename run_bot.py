"""
自动交易机器人入口 (Bot Runner)
"""
import asyncio
import signal
import sys
from qtf.engine.event_loop import EventLoop
from qtf.data.simulated import SimulatedAdapter
from qtf.core.events import EventType

# 临时策略 (可以直接写在这里，后续移动到 strategies 目录)
from qtf.engine.base import BaseStrategy

class DemoStrategy(BaseStrategy):
    def on_init(self):
        print(f"[{self.name}] Initializing...")
        self.subscribed = ["000001.SZ", "600000.SH"]
    
    def on_start(self):
        print(f"[{self.name}] Starting...")
        # 在这里订阅行情，实际应该通过 context 调用 adapter
        print(f"[{self.name}] Strategy Started. Listening for quotes...")

    def on_tick(self, quote):
        print(f"[{self.name}] On Tick: {quote.symbol} = {quote.last_price:.2f}")
        # 简单策略逻辑: 价格 > 105 买入 (模拟)
        if quote.last_price > 105:
            print(f"  >>> Signal: BUY {quote.symbol} @ {quote.last_price:.2f}")

async def main():
    print("=== Starting QTF Bot ===")
    
    # 1. 创建事件循环
    loop = EventLoop()
    
    # 2. 创建数据适配器
    adapter = SimulatedAdapter()
    
    # 3. 创建策略
    strategy = DemoStrategy(name="DemoStrategy")
    strategy.on_init()
    
    # 4. 绑定事件 (简单绑定，实际应通过 Engine 协调)
    # 将 adapter 的推送绑定到 strategy 的处理
    adapter.add_callback(lambda q: strategy.on_tick(q))
    
    # 5. 启动组件
    await loop.start()
    await adapter.connect()
    await adapter.subscribe(["000001.SZ", "600000.SH"])
    strategy.on_start()
    
    print("=== Bot Running (Ctrl+C to stop) ===")
    
    # 优雅退出处理
    stop_event = asyncio.Event()
    
    def on_stop():
        print("\nStopping...")
        stop_event.set()
    
    # Windows 下可能不支持 add_signal_handler for SIGINT with asyncio loop in some environments,
    # 但通常是可以的。或者使用简单的 try/finally
    try:
        await stop_event.wait()
    except asyncio.CancelledError:
        pass
    finally:
        await adapter.disconnect()
        await loop.stop()
        print("=== Bot Stopped ===")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
