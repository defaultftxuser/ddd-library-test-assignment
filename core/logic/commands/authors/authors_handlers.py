from dataclasses import dataclass
from typing import Any

from core.infra.repositories.authors.authors_repository import AuthorRepository
from core.logic.commands.authors.authors_commands import (
    AddAuthorCommand,
    DeleteAuthorCommand,
    GetAuthorsCommand,
)
from core.logic.commands.base import BaseHandler


@dataclass(eq=False)
class AddAuthorCommandHandler(BaseHandler):
    repository: AuthorRepository

    async def handle(self, command: AddAuthorCommand) -> dict[str, str | int]:
        return await self.repository.create_author(entity=command.__dict__)


@dataclass(eq=False)
class GetAuthorsCommandHandler(BaseHandler):
    repository: AuthorRepository

    async def handle(self, command: GetAuthorsCommand) -> list[Any] | None:
        result_entity = {key: value for key, value in command.__dict__.items() if value}
        return await self.repository.get_authors(entity=result_entity)


@dataclass(eq=False)
class DeleteAuthorCommandHandler(BaseHandler):
    repository: AuthorRepository

    async def handle(self, command: DeleteAuthorCommand) -> None:
        return await self.repository.delete_author(entity=command.__dict__)
