"""
数据库管理 (Database)
PostgreSQL/TimescaleDB 连接和会话管理
"""

from typing import Optional, AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    AsyncEngine,
    async_sessionmaker,
)
from qtf.config import settings


class Database:
    """
    数据库管理类
    负责连接池和会话管理
    """
    
    _instance: Optional["Database"] = None
    _engine: Optional[AsyncEngine] = None
    _session_factory: Optional[async_sessionmaker] = None
    
    def __new__(cls) -> "Database":
        """单例模式"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    async def initialize(cls, database_url: Optional[str] = None) -> None:
        """
        初始化数据库连接
        Args:
            database_url: 数据库连接字符串 (可选)
        """
        url = database_url or settings.DATABASE_URL
        
        cls._engine = create_async_engine(
            url,
            echo=settings.DEBUG,
            pool_size=10,
            max_overflow=20,
        )
        
        cls._session_factory = async_sessionmaker(
            bind=cls._engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
    
    @classmethod
    async def close(cls) -> None:
        """关闭数据库连接"""
        if cls._engine:
            await cls._engine.dispose()
            cls._engine = None
            cls._session_factory = None
    
    @classmethod
    async def get_session(cls) -> AsyncGenerator[AsyncSession, None]:
        """
        获取数据库会话
        Usage:
            async with Database.get_session() as session:
                ...
        """
        if cls._session_factory is None:
            raise RuntimeError("Database not initialized")
        
        async with cls._session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
    
    @classmethod
    def get_engine(cls) -> Optional[AsyncEngine]:
        """获取数据库引擎"""
        return cls._engine
