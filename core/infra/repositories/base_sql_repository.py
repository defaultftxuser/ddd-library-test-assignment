from dataclasses import dataclass
from typing import Type, Any

from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import DatabaseError

from core.infra.db.sql_db.base import SQLBaseModel
from core.infra.repositories.database_config import Database


@dataclass(eq=False)
class SQLAlchemyRepository:
    model: Type[SQLBaseModel]
    database: Database

    async def get_one_or_none(self, **filters: str) -> dict:
        async with self.database.create_async_session() as session:  # noqa
            query = select(self.model.__table__.c).filter_by(**filters)
            result = await session.execute(query)
            return result.mappings().first()

    async def add_object(self, **entity: Any) -> dict:
        async with self.database.create_async_session() as session:  # noqa

            query = (
                insert(self.model).values(**entity).returning(self.model.__table__.c)
            )
            result = await session.execute(query)
            await session.commit()
            result = result.mappings().first()
            return result

    async def update_object(self, entity: dict[str, str | int]) -> dict:
        async with self.database.create_async_session() as session:  # noqa
            query = (
                update(self.model)
                .where(self.model.id == entity.get("id"))
                .values(**entity)
                .returning(self.model.__table__.c)
            )
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    async def delete_object(self, **entity: str | int) -> None:
        async with self.database.create_async_session() as session:  # noqa
            try:
                query = delete(self.model).filter_by(**entity)
                await session.execute(query)
            except DatabaseError as e:
                raise e
