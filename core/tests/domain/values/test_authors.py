import pytest

from core.common.exceptions.common_exceptions import UnexpectedTypeException
from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.authors import SexValue


def test_sex_value_valid():
    sex_value = SexValue(value=SexEnum.male)
    try:
        sex_value.validate()
    except UnexpectedTypeException:
        pytest.fail("UnexpectedTypeException was raised for valid value")


def test_sex_value_invalid_type():
    class InvalidType:
        pass

    invalid_value = InvalidType()
    with pytest.raises(UnexpectedTypeException) as excinfo:
        sex_value = SexValue(value=invalid_value)  # noqa
        sex_value.validate()
    assert excinfo.value.value == invalid_value
