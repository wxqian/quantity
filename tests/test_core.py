"""
核心模块测试
"""

import pytest
from qtf.core.events import Event, EventType, TickEvent, OrderEvent
from qtf.core.exceptions import QTFError, OrderError, DataError


class TestEventType:
    """事件类型测试"""
    
    def test_event_types_exist(self):
        """测试事件类型枚举"""
        assert EventType.TICK.value == "tick"
        assert EventType.ORDER.value == "order"
        assert EventType.TRADE.value == "trade"
        assert EventType.TIMER.value == "timer"


class TestEvent:
    """事件基类测试"""
    
    def test_create_event(self):
        """测试创建事件"""
        event = Event(type=EventType.TICK)
        assert event.type == EventType.TICK
        assert event.data is None
        assert event.timestamp is not None
    
    def test_create_event_with_data(self):
        """测试创建带数据的事件"""
        data = {"symbol": "000001.SZ", "price": 10.5}
        event = Event(type=EventType.TICK, data=data)
        assert event.data == data


class TestTickEvent:
    """Tick 事件测试"""
    
    def test_create_tick_event(self):
        """测试创建 Tick 事件"""
        tick = TickEvent(
            type=EventType.TICK,
            symbol="000001.SZ",
            last_price=10.5,
            bid_price=10.49,
            ask_price=10.51,
        )
        assert tick.type == EventType.TICK
        assert tick.symbol == "000001.SZ"
        assert tick.last_price == 10.5


class TestExceptions:
    """异常测试"""
    
    def test_qtf_error(self):
        """测试基础异常"""
        error = QTFError("test error", code=100)
        assert str(error) == "test error"
        assert error.code == 100
    
    def test_order_error(self):
        """测试订单异常"""
        error = OrderError("order failed")
        assert isinstance(error, QTFError)
    
    def test_data_error(self):
        """测试数据异常"""
        error = DataError("data not found")
        assert isinstance(error, QTFError)
