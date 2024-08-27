from dataclasses import dataclass

from core.logic.commands.base import BaseCommand


@dataclass(eq=False)
class GetBookCommand(BaseCommand):
    book_name: str


@dataclass(eq=False)
class DeleteBookCommand(BaseCommand):
    author_id: int


@dataclass(eq=False)
class AddBookCommand(BaseCommand):
    author_id: int


@dataclass(eq=False)
class LinkBookAuthorCommand(BaseCommand):
    book_id: int
    authors_id_list: list[int]
