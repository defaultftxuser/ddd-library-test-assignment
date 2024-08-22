import pytest

from core.common.exceptions.common_exceptions import UnexpectedTypeException
from core.exceptions.domain.books import BookDescriptionException, TooShortBookNameException, TooLongBookNameException
from core.infra.domain.values.books import BookDescription, BookName, BookTheme
from core.infra.domain.values.enums import ThemesEnums


def test_book_description_valid():
    desc = BookDescription(value="A short description")
    desc.validate()


def test_book_description_too_long():

    with pytest.raises(BookDescriptionException) as excinfo:
        desc = BookDescription(value="A" * 101)
        desc.validate()
    assert excinfo.value.length == 100


def test_book_name_too_short():

    with pytest.raises(TooShortBookNameException) as excinfo:
        name = BookName(value="")
        name.validate()
    assert excinfo.value.length == 1


def test_book_name_too_long():

    with pytest.raises(TooLongBookNameException) as excinfo:
        name = BookName(value="A" * 51)
        name.validate()
    assert excinfo.value.length == 50


def test_book_name_valid():
    name = BookName(value="Valid Name")
    name.validate()


def test_book_theme_valid():
    theme = BookTheme(value=ThemesEnums.fiction)
    theme.validate()


def test_book_theme_invalid_type():
    with pytest.raises(UnexpectedTypeException) as excinfo:
        theme = BookTheme(value="Invalid Theme")
        theme.validate()
    assert excinfo.value.value == "Invalid Theme"
