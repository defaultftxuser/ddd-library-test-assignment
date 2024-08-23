from core.infra.domain.entities.authors import Author
from core.logic.commands.base import BaseCommand


class AddAuthorCommand(BaseCommand):
    author: Author


class GetAuthorByNameCommand(BaseCommand):
    first_name: str
    second_name: str
    last_name: str


class GetAuthorsListCommand(BaseCommand):
    ...
