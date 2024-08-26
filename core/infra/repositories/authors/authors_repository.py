from abc import ABC
from dataclasses import dataclass
from typing import Type

from sqlalchemy import select

from core.infra.db.sql_db.models import Author
from core.infra.repositories.base_sql_repository import SQLAlchemyRepository
from core.infra.repositories.database_config import Database


@dataclass(eq=False)
class BaseAuthorRepository(ABC):
    ...


@dataclass(eq=False)
class AuthorRepository(SQLAlchemyRepository, BaseAuthorRepository):
    model: Type[Author]
    database: Database

    async def create_author(
        self, user_id: int, entity: dict[str, str | int]
    ) -> dict[str, str | int]:
        async with self.database.create_async_session() as session:  # noqa
            entity["creator_id"] = user_id
            return await self.add_object(**entity)

    async def delete_author(self, user_id: int, entity: dict[str, str | int]) -> None:
        async with self.database.create_async_session() as session:  # noqa
            entity["creator_id"] = user_id
            return await self.delete_object(**entity)

    async def get_authors(self, entity: dict[str, str]):
        async with self.database.create_async_session() as session:  # noqa
            query = select(
                self.model.id,
                self.model.first_name,
                self.model.second_name,
                self.model.last_name,
            ).filter_by(**entity)
            result = await session.execute(query)
            if result:
                return result.mappings().fetchall()

    async def get_all_authors(self):
        async with self.database.create_async_session() as session:  # noqa
            query = select(
                self.model.first_name, self.model.second_name, self.model.last_name
            )
            result = await session.execute(query)
            if result:
                return result.mappings().fetchall()
