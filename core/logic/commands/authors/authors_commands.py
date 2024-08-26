from dataclasses import dataclass

from core.logic.commands.base import BaseCommand


@dataclass(eq=False)
class AddAuthorCommand(BaseCommand):
    creator_id: int
    container: dict[str, str | int]


@dataclass(eq=False)
class GetAuthorsCommand(BaseCommand):
    id: int | None = None
    first_name: str | None = None
    second_name: str | None = None
    last_name: str | None = None
    creator_id: int | None = None


@dataclass(eq=False)
class DeleteAuthorCommand(BaseCommand):
    creator_id: int
    container: dict[str, str | int]
