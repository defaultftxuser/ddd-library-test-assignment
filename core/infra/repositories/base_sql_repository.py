import asyncio
from abc import ABC

from sqlalchemy import select, Row, insert, update

from core.infra.db.sql_db.base import SQLBaseModel
from core.infra.repositories.database_config import Database


class SQLAlchemyRepository:
    model: SQLBaseModel
    database: Database

    async def get_one_or_none(self, **filters) -> Row:
        async with self.database.create_async_session() as session:
            query = select(self.model).filter_by(**filters)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def add_object(self, **entity) -> int:
        async with self.database.create_async_session() as session:
            query = insert(self.model).values(**entity).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            result = result.fetchone()
            return result

    async def update_object(self, entity) -> None:
        async with self.database.create_async_session() as session:
            query = (
                update(self.model).where(self.model.id == entity.id).values(**entity)
            )
            await session.execute(query)
            await session.commit()
