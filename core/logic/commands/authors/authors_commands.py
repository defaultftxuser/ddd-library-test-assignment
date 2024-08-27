from dataclasses import dataclass
from typing import Any

from core.infra.domain.entities.enums import SexEnum
from core.logic.commands.base import BaseCommand


@dataclass(eq=False)
class AddAuthorCommand(BaseCommand):
    creator_id: int
    first_name: str
    second_name: str
    last_name: str
    sex: SexEnum | None


@dataclass(eq=False)
class GetAuthorsCommand(BaseCommand):
    id: int | None = None
    first_name: str | None = None
    second_name: str | None = None
    last_name: str | None = None
    creator_id: int | None = None


@dataclass(eq=False)
class DeleteAuthorCommand(BaseCommand):
    creator_id: int | Any
    first_name: str | None = None
    second_name: str | None = None
    last_name: str | None = None
