import pytest

from core.exceptions.domain.books import (
    TooShortBookNameException,
    TooLongBookNameException,
    TooLongBookDescriptionException,
    TooShortBookDescriptionException,
)
from core.infra.domain.values.books import BookDescription, BookName, BookTheme
from core.infra.domain.values.enums import ThemesEnums


def test_book_description_valid():
    desc = BookDescription(value="A short description")
    desc.validate()


def test_book_description_too_long():
    with pytest.raises(TooLongBookDescriptionException) as occurred_exception:
        desc = BookDescription(value="A" * 101)
        desc.validate()


def test_book_description_too_short():
    with pytest.raises(TooShortBookDescriptionException) as occurred_exception:
        desc = BookDescription(value="A")
        desc.validate()


def test_book_name_too_short():
    with pytest.raises(TooShortBookNameException) as occurred_exception:
        name = BookName(value="")
        name.validate()


def test_book_name_too_long():
    with pytest.raises(TooLongBookNameException) as occurred_exception:
        name = BookName(value="A" * 51)
        name.validate()


def test_book_name_valid():
    name = BookName(value="Valid Name")
    name.validate()


def test_book_theme_valid():
    theme = BookTheme(value=ThemesEnums.fiction)
    theme.validate()
