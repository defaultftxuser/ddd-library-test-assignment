from abc import ABC
from dataclasses import dataclass

from core.infra.db.sql_db.models import User
from core.infra.repositories.base_sql_repository import SQLAlchemyRepository
from core.infra.repositories.database_config import Database


@dataclass(eq=False)
class BaseUserRepository(ABC):
    ...


@dataclass(eq=False)
class UserRepository(SQLAlchemyRepository, BaseUserRepository):
    model: User
    database: Database

    async def deactivate_user(self, entity: dict[str, str]) -> None:
        if user_model := await self.get_one_or_none(**entity):
            user_model["is_active"] = False
        await self.update_object(user_model)

    async def create_user(self, **entity) -> dict:
        async with self.database.create_async_session() as session:  # noqa
            dict_row = await self.add_object(**entity)
            return dict_row

    async def get_user(self, **entity) -> dict:
        async with self.database.create_async_session() as session:  # noqa
            dict_row = await self.get_one_or_none(**entity)
            return dict_row
