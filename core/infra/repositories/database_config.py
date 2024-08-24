from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from core.common.settings.config import Settings


class Database:
    def __init__(self, url):
        self.engine = create_async_engine(url=url)
        self.async_session = async_sessionmaker(
            bind=self.engine, expire_on_commit=False
        )

    @asynccontextmanager
    async def create_async_session(self) -> AsyncSession:
        session = self.async_session()
        try:
            yield session
        except SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.commit()
            await session.close()
