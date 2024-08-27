from dataclasses import dataclass
from typing import Any

from core.infra.domain.values.enums import ThemesEnums
from core.logic.commands.base import BaseCommand


@dataclass(eq=False)
class GetBookCommand(BaseCommand):
    id: int | None = None
    name: str | None = None
    description: str | None = None
    theme: ThemesEnums | None = None


@dataclass(eq=False)
class DeleteBookCommand(BaseCommand):
    creator_id: int | Any
    name: str | None = None
    description: str | None = None
    theme: ThemesEnums | None = None


@dataclass(eq=False)
class AddBookCommand(BaseCommand):
    creator_id: int | Any
    name: str | None = None
    description: str | None = None
    theme: ThemesEnums | None = None


@dataclass(eq=False)
class LinkBookAuthorCommand(BaseCommand):
    book_id: int
    authors_id_list: list[int]
