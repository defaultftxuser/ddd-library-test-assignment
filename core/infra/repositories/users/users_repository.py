from dataclasses import dataclass

from core.infra.db.sql_db.models import User
from core.infra.repositories.base_sql_repository import SQLAlchemyRepository
from core.infra.repositories.database_config import Database


@dataclass(eq=False)
class UserRepository(SQLAlchemyRepository):
    model: User
    database: Database

    async def deactivate_user(self, entity):
        user_model = await self.get_one_or_none(**entity.id)
        user_model.is_active = False
        await self.update_object(**entity)
