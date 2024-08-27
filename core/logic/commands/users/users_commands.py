from dataclasses import dataclass
from typing import Any

from core.logic.commands.base import BaseCommand


@dataclass(eq=False)
class CreateUserCommand(BaseCommand):
    username: str
    password: str


@dataclass(eq=False)
class CreateTokenUserCommand(BaseCommand):
    username: str
    password: str


@dataclass(eq=False)
class DeactivateUserCommand(BaseCommand):
    user_id: int | Any
