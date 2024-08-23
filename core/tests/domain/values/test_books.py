import pytest

from core.common.exceptions.common_exceptions import UnexpectedTypeException
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
    assert occurred_exception.value.length == 100


def test_book_description_too_short():

    with pytest.raises(TooShortBookDescriptionException) as occurred_exception:
        desc = BookDescription(value="A")
        desc.validate()
    assert occurred_exception.value.length == 5


def test_book_name_too_short():

    with pytest.raises(TooShortBookNameException) as occurred_exception:
        name = BookName(value="")
        name.validate()
    assert occurred_exception.value.length == 1


def test_book_name_too_long():

    with pytest.raises(TooLongBookNameException) as occurred_exception:
        name = BookName(value="A" * 51)
        name.validate()
    assert occurred_exception.value.length == 50


def test_book_name_valid():
    name = BookName(value="Valid Name")
    name.validate()


def test_book_theme_valid():
    theme = BookTheme(value=ThemesEnums.fiction)
    theme.validate()


def test_book_theme_invalid_type():
    with pytest.raises(UnexpectedTypeException) as occurred_exception:
        theme = BookTheme(value="Invalid Theme")  # noqa
        theme.validate()
    assert occurred_exception.value.value == "Invalid Theme"
