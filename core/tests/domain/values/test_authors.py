import pytest

from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.authors import SexValue


def test_sex_value_valid():
    sex_value = SexValue(value=SexEnum.male)
    try:
        sex_value.validate()
    except TypeError:
        pytest.fail("Type Error")


def test_sex_value_invalid_type():
    class InvalidType:
        pass
