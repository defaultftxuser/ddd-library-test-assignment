from sqlalchemy import String, Enum, Integer, ForeignKey, Boolean, LargeBinary
from sqlalchemy.orm import MappedColumn, mapped_column, relationship

from enum import Enum as PyEnum

from core.infra.db.sql_db.base import SQLBaseModel, Base
from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.enums import ThemesEnums


class Author(SQLBaseModel):
    __tablename__ = "authors"  # noqa

    first_name: MappedColumn[str] = mapped_column(String, nullable=False)
    second_name: MappedColumn[str] = mapped_column(String, nullable=False)
    last_name: MappedColumn[str] = mapped_column(String, nullable=False)
    sex: MappedColumn[PyEnum] = mapped_column(Enum(SexEnum), nullable=True)
    creator_id: MappedColumn[int] = mapped_column(ForeignKey("users.id"))

    creator = relationship("User", back_populates="authors")
    books = relationship("Book", secondary="book_author", back_populates="authors")


class Book(SQLBaseModel):
    __tablename__ = "books"  # noqa

    name: MappedColumn[str] = mapped_column(String, nullable=False)
    description: MappedColumn[str] = mapped_column(String, nullable=False)
    theme: MappedColumn[PyEnum] = mapped_column(Enum(ThemesEnums), nullable=False)
    creator_id: MappedColumn[int] = mapped_column(
        ForeignKey("users.id"), primary_key=True
    )

    authors = relationship("Author", secondary="book_author", back_populates="books")


class BookAuthor(Base):
    __tablename__ = "book_author"  # noqa

    book_id: MappedColumn[int] = mapped_column(
        Integer, ForeignKey("books.id"), primary_key=True
    )
    author_id: MappedColumn[int] = mapped_column(
        Integer, ForeignKey("authors.id"), primary_key=True
    )


class User(SQLBaseModel):
    __tablename__ = "users"  # noqa

    username: MappedColumn[str] = mapped_column(
        String, unique=True, nullable=False, index=True
    )
    hashed_password: MappedColumn[str] = mapped_column(String, nullable=False)
    is_active: MappedColumn[bool] = mapped_column(
        Boolean, nullable=False, default=True, autoincrement=True
    )

    authors = relationship("Author", back_populates="creator")
    books = relationship("Book", backref="creator")
