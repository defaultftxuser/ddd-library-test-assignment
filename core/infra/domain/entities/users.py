from dataclasses import dataclass

from core.infra.domain.entities.base import BaseEntity
from core.infra.domain.values.users import PasswordValue, UsernameValue


@dataclass(eq=False)
class UserEntity(BaseEntity):
    username: UsernameValue
    password: PasswordValue


@dataclass
class UserHashedPasswordEntity:
    username: str
    hashed_password: str


@dataclass
class UserIdEntity:
    id: int
    username: str
