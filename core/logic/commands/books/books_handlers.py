from dataclasses import dataclass
from typing import Any

from core.infra.repositories.books.books_repository import (
    BookRepository,
    BookAuthorRepository,
)
from core.logic.commands.base import BaseHandler
from core.logic.commands.books.books_commands import (
    GetBookCommand,
    DeleteBookCommand,
    AddBookCommand,
    LinkBookAuthorCommand,
)


@dataclass(eq=False)
class GetBookCommandHandler(BaseHandler):
    repository: BookRepository

    async def handle(self, command: GetBookCommand) -> list[Any]:
        result_entity = {key: value for key, value in command.__dict__.items() if value}
        return await self.repository.get_books(book_entity=result_entity)


@dataclass(eq=False)
class DeleteBookCommandHandler(BaseHandler):
    repository: BookRepository

    async def handle(self, command: DeleteBookCommand) -> None:
        await self.repository.delete_book(book_entity=command.__dict__)


@dataclass(eq=False)
class AddBookCommandHandler(BaseHandler):
    repository: BookRepository

    async def handle(self, command: AddBookCommand) -> None:
        await self.repository.add_book(book_entity=command.__dict__)


@dataclass(eq=False)
class LinkBookAuthorCommandHandler(BaseHandler):
    repository: BookAuthorRepository

    async def handle(self, command: LinkBookAuthorCommand) -> None:
        await self.repository.author_book_link(
            book_id=command.book_id, authors_id_list=command.authors_id_list
        )
