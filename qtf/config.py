from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Quant Trading Framework"
    VERSION: str = "0.1.0"
    DEBUG: bool = True
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Database
    DATABASE_URL: Optional[str] = "postgresql+asyncpg://user:password@localhost/quant_db"
    REDIS_URL: Optional[str] = "redis://localhost:6379/0"
    
    # LLM
    OPENAI_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
