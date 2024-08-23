from datetime import datetime

from sqlalchemy import Column, String, DateTime, func, Enum, Integer, ForeignKey
from sqlalchemy.orm import MappedColumn, mapped_column, relationship


from enum import Enum as PyEnum

from core.infra.db.sql_db.base import SQLBaseModel
from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.enums import ThemesEnums


class Author(SQLBaseModel):
    __tablename__ = "authors"  # noqa

    first_name: MappedColumn[str] = mapped_column(String, nullable=False)
    second_name: MappedColumn[str] = mapped_column(String, nullable=False)
    last_name: MappedColumn[str] = mapped_column(String, nullable=False)
    created_at: MappedColumn[datetime] = Column(DateTime, server_default=func.now())
    updated_at: MappedColumn[datetime] = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    sex = Column(Enum(SexEnum), nullable=True)


class Book(SQLBaseModel):
    __tablename__ = "books"  # noqa

    name: MappedColumn[str] = Column(String, nullable=False)
    description: MappedColumn[str] = Column(String, nullable=False)
    theme: MappedColumn[PyEnum] = Column(Enum(ThemesEnums), nullable=False)

    authors = relationship("Author", secondary="book_author", back_populates="books")


class BookAuthor(SQLBaseModel):
    __tablename__ = "book_author"  # noqa

    book_id: MappedColumn[int] = Column(
        Integer, ForeignKey("books.id"), primary_key=True
    )
    author_id: MappedColumn[int] = Column(
        Integer, ForeignKey("authors.id"), primary_key=True
    )

    book = relationship("Book", back_populates="authors", foreign_keys=[book_id])
    author = relationship("Author", back_populates="books", foreign_keys=[author_id])
