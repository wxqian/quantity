"""
异常定义 (Exception Definitions)
定义系统中使用的各类自定义异常
"""


class QTFError(Exception):
    """QTF 框架基础异常类"""
    def __init__(self, message: str = "", code: int = 0):
        self.message = message
        self.code = code
        super().__init__(self.message)


class DataError(QTFError):
    """数据相关异常"""
    pass


class OrderError(QTFError):
    """订单相关异常"""
    pass


class StrategyError(QTFError):
    """策略相关异常"""
    pass


class BrokerError(QTFError):
    """券商接口相关异常"""
    pass


class ConnectionError(QTFError):
    """连接相关异常"""
    pass


class ConfigError(QTFError):
    """配置相关异常"""
    pass


class ValidationError(QTFError):
    """验证相关异常"""
    pass
