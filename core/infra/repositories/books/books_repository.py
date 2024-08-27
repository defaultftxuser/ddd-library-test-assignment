from abc import ABC
from dataclasses import dataclass
from typing import Type

from core.infra.db.sql_db.models import Book, BookAuthor
from core.infra.repositories.base_sql_repository import SQLAlchemyRepository
from core.infra.repositories.database_config import Database


@dataclass(eq=False)
class BaseBookRepository(ABC):
    ...


@dataclass(eq=False)
class BookRepository(SQLAlchemyRepository, BaseBookRepository):
    model: Type[Book]
    database: Database

    async def get_books(self, book_entity) -> list[dict[str, str]]:
        return await self.get_many(**book_entity)

    async def delete_book(self, book_entity):
        await self.delete_object(**book_entity)

    async def add_book(self, book_entity: dict[str, str | int]):
        return await self.add_object(**book_entity)


@dataclass(eq=False)
class BaseBookAuthorRepository:
    ...


@dataclass(eq=False)
class BookAuthorRepository(SQLAlchemyRepository, BaseBookAuthorRepository):
    model: Type[BookAuthor]
    database: Database

    async def author_book_link(self, book_id: int, authors_id_list: list[int]) -> None:
        async with self.database.create_async_session() as session:  # noqa
            for author_id in authors_id_list:
                current_entity = {"book_id": book_id, "author_id": author_id}
                try:
                    await self.add_object(**current_entity)
                except Exception:  # noqa TODO: просмотреть все кейсы и написать к ним исключения
                    await session.rollback()
                    return
                await session.commit()
