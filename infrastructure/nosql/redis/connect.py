from pydantic_settings import BaseSettings#type: ignore
from persistent.db.base import Base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import os
from dotenv import load_dotenv#type:ignore
import asyncio


load_dotenv()

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    @property
    def DATABASE_URL_aioredis(self):
        return f"redis+aioredis://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
settings = Settings(DB_HOST = os.getenv("DB_HOST_REDIS"), DB_PORT = os.getenv("DB_PORT_REDIS"), DB_USER = os.getenv("DB_USER_REDIS"), DB_PASS = os.getenv("DB_PASS_REDIS"), DB_NAME = os.getenv("DB_NAME_REDIS"))


def create_connection() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(settings.DATABASE_URL_aioredis)
    
    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables() -> None:
    engine = create_async_engine(settings.DATABASE_URL_aioredis)
    
    async def init_models() -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
    asyncio.run(init_models())