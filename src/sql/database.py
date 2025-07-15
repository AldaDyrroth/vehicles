from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from src.sql.config import settings

class Engines:

    sync_engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=True,
        # pool_size=5,
        # max_overflow=10

    )

    async_engine = create_async_engine(
        url=settings.DATABASE_URL_asyncpg,
        echo=True,
        # pool_size=5,
        # max_overflow=10

    )

    sync_session_factory = sessionmaker(sync_engine)
    async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass


