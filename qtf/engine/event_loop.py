"""
事件循环 (Event Loop)
核心事件驱动引擎
"""

import asyncio
from typing import Dict, List, Callable, Any, Optional
from collections import defaultdict
from qtf.core.events import Event, EventType


class EventLoop:
    """
    事件循环
    负责事件的分发和处理
    """
    
    def __init__(self):
        self._handlers: Dict[EventType, List[Callable]] = defaultdict(list)
        self._queue: asyncio.Queue = asyncio.Queue()
        self._running: bool = False
        self._task: Optional[asyncio.Task] = None
    
    @property
    def running(self) -> bool:
        """是否运行中"""
        return self._running
    
    # ============ 事件注册 ============
    
    def register(self, event_type: EventType, handler: Callable) -> None:
        """
        注册事件处理器
        Args:
            event_type: 事件类型
            handler: 处理函数
        """
        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)
    
    def unregister(self, event_type: EventType, handler: Callable) -> None:
        """
        注销事件处理器
        Args:
            event_type: 事件类型
            handler: 处理函数
        """
        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)
    
    def unregister_all(self, event_type: Optional[EventType] = None) -> None:
        """
        注销所有处理器
        Args:
            event_type: 事件类型 (可选，不传则注销所有)
        """
        if event_type:
            self._handlers[event_type].clear()
        else:
            self._handlers.clear()
    
    # ============ 事件发布 ============
    
    async def put(self, event: Event) -> None:
        """
        发布事件到队列
        Args:
            event: 事件对象
        """
        await self._queue.put(event)
    
    def put_nowait(self, event: Event) -> None:
        """
        非阻塞发布事件
        Args:
            event: 事件对象
        """
        self._queue.put_nowait(event)
    
    # ============ 事件处理 ============
    
    async def _process_event(self, event: Event) -> None:
        """
        处理单个事件
        Args:
            event: 事件对象
        """
        handlers = self._handlers.get(event.type, [])
        for handler in handlers:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(event)
                else:
                    handler(event)
            except Exception as e:
                # TODO: 添加错误日志
                print(f"Error handling event {event.type}: {e}")
    
    async def _run_loop(self) -> None:
        """运行事件循环"""
        while self._running:
            try:
                event = await asyncio.wait_for(
                    self._queue.get(),
                    timeout=0.1
                )
                await self._process_event(event)
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                print(f"Event loop error: {e}")
    
    # ============ 生命周期 ============
    
    async def start(self) -> None:
        """启动事件循环"""
        if self._running:
            return
        
        self._running = True
        self._task = asyncio.create_task(self._run_loop())
    
    async def stop(self) -> None:
        """停止事件循环"""
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
    
    async def wait_empty(self, timeout: float = 5.0) -> bool:
        """
        等待队列清空
        Args:
            timeout: 超时时间（秒）
        Returns:
            bool: 是否成功清空
        """
        try:
            await asyncio.wait_for(
                self._queue.join(),
                timeout=timeout
            )
            return True
        except asyncio.TimeoutError:
            return False
