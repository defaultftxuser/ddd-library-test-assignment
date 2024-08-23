from core.logic.commands.base import BaseCommand


class GetBookByName(BaseCommand):
    book_name: str


class GetBookByAuthor(BaseCommand):
    author_first_name: str
    author_second_name: str
    author_last_name: str


class GetAuthorById(BaseCommand):
    author_id: int
