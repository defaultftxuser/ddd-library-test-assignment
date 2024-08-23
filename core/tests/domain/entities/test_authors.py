import pytest

from core.common.exceptions.common_exceptions import UnexpectedTypeException
from core.infra.domain.entities.authors import Author
from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.authors import (
    AuthorFirstNameValue,
    AuthorSecondNameValue,
    AuthorLastNameValue,
    SexValue,
)


def test_author_creation():
    first_name = AuthorFirstNameValue("John")
    second_name = AuthorSecondNameValue("Ronald")
    last_name = AuthorLastNameValue("Reuel")
    author = Author(first_name, second_name, last_name, SexEnum.male)

    assert author.first_name.value == "John"
    assert author.second_name.value == "Ronald"
    assert author.last_name.value == "Reuel"
    assert author.sex == SexEnum.male


def test_author_with_none_last_name():
    first_name = AuthorFirstNameValue("Jane")
    second_name = AuthorSecondNameValue("Austen")
    last_name = AuthorLastNameValue(None)
    author = Author(first_name, second_name, last_name, SexEnum.female)

    assert author.first_name.value == "Jane"
    assert author.second_name.value == "Austen"
    assert author.last_name.value is None
    assert author.sex == SexEnum.female


def test_sex_value_validation_success():
    sex_value = SexValue(SexEnum.male)
    sex_value.validate()


def test_sex_value_validation_failure():
    with pytest.raises(UnexpectedTypeException):
        sex_value = SexValue("NotASexEnum")  # noqa
        sex_value.validate()


def test_author_equality():
    first_name = AuthorFirstNameValue("John")
    second_name = AuthorSecondNameValue("Doe")
    last_name = AuthorLastNameValue("Smith")

    author1 = Author(first_name, second_name, last_name, SexEnum.male)
    author2 = Author(first_name, second_name, last_name, SexEnum.male)

    assert author1 != author2


def test_author_with_optional_sex():
    first_name = AuthorFirstNameValue("Pat")
    second_name = AuthorSecondNameValue("Morgan")
    last_name = AuthorLastNameValue("Lee")
    author = Author(first_name, second_name, last_name, None)

    assert author.sex is None


def test_first_name_value():
    name = AuthorFirstNameValue("John")
    assert name.value == "John"


def test_last_name_value():
    last_name = AuthorLastNameValue("Smith")
    assert last_name.value == "Smith"

    last_name_none = AuthorLastNameValue(None)
    assert last_name_none.value is None
