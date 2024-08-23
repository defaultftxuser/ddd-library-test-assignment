from core.infra.domain.entities.authors import Author
from core.infra.domain.entities.books import BookEntity
from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.authors import (
    AuthorFirstNameValue,
    AuthorSecondNameValue,
    AuthorLastNameValue,
)
from core.infra.domain.values.books import BookDescription, BookName, BookTheme
from core.infra.domain.values.enums import ThemesEnums


def test_book_entity_creation():
    description = BookDescription("An interesting story")
    name = BookName("Great Book")
    theme = BookTheme(ThemesEnums.fiction)
    book = BookEntity(description, name, theme)

    assert book.description.value == "An interesting story"
    assert book.name.value == "Great Book"
    assert book.theme.value == ThemesEnums.fiction
    assert len(book.authors) == 0


def test_add_author():
    description = BookDescription("An interesting story")
    name = BookName("Great Book")
    theme = BookTheme(ThemesEnums.fiction)
    book = BookEntity(description, name, theme)

    author = Author(
        first_name=AuthorFirstNameValue("John"),
        second_name=AuthorSecondNameValue("Ronald"),
        last_name=AuthorLastNameValue("Tolkien"),
        sex=SexEnum.male,
    )

    book.add_author(author)

    assert len(book.authors) == 1
    assert author in book.authors


def test_duplicate_author_not_added():
    description = BookDescription("An interesting story")
    name = BookName("Great Book")
    theme = BookTheme(ThemesEnums.fiction)
    book = BookEntity(description, name, theme)

    author = Author(
        first_name=AuthorFirstNameValue("John"),
        second_name=AuthorSecondNameValue("Ronald"),
        last_name=AuthorLastNameValue("Tolkien"),
        sex=SexEnum.male,
    )

    book.add_author(author)
    book.add_author(author)

    assert len(book.authors) == 1


def test_author_with_different_attributes():
    description = BookDescription("An interesting story")
    name = BookName("Great Book")
    theme = BookTheme(ThemesEnums.fiction)
    book = BookEntity(description, name, theme)

    author1 = Author(
        first_name=AuthorFirstNameValue("John"),
        second_name=AuthorSecondNameValue("Ronald"),
        last_name=AuthorLastNameValue("Tolkien"),
        sex=SexEnum.male,
    )

    author2 = Author(
        first_name=AuthorFirstNameValue("George"),
        second_name=AuthorSecondNameValue("Raymond"),
        last_name=AuthorLastNameValue("Martin"),
        sex=SexEnum.male,
    )

    book.add_author(author1)
    book.add_author(author2)

    assert len(book.authors) == 2
    assert author1 in book.authors
    assert author2 in book.authors
