"""
QTF Data Ingestion Layer
数据接入层：负责对接不同市场和券商的数据接口
"""

from qtf.data.base import MarketDataAdapter
from qtf.data.models import Quote, Bar

__all__ = [
    "MarketDataAdapter",
    "Quote",
    "Bar",
]
