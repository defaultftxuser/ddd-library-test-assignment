from punq import Container, Scope

from core.common.settings.config import Settings, get_settings
from core.infra.db.sql_db.models import User
from core.infra.repositories.base_sql_repository import SQLAlchemyRepository
from core.infra.repositories.database_config import Database
from core.infra.repositories.users.users_repository import UserRepository


def init_container():
    container = Container()

    container.register(Settings, factory=get_settings, scope=Scope.singleton)

    settings: Settings = container.resolve(Settings)

    container.register(
        Database, instance=Database(url=settings.get_db_url), scope=Scope.singleton
    )

    container.register(
        SQLAlchemyRepository,
        UserRepository(model=User, database=container.resolve(Database)),
        scope=Scope.singleton,
    )
