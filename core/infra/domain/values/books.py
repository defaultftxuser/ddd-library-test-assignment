from dataclasses import dataclass

from core.common.exceptions.common_exceptions import UnexpectedTypeException
from core.exceptions.domain.books import (
    TooShortBookNameException,
    TooLongBookNameException,
    TooShortBookDescriptionException,
    TooLongBookDescriptionException,
)
from core.infra.domain.values.base import BaseValue
from core.infra.domain.values.enums import ThemesEnums


@dataclass
class BookDescription(BaseValue):
    value: str

    def validate(self) -> None:
        if len(self.value) < 5:
            raise TooShortBookDescriptionException(length=5)
        if len(self.value) > 100:
            raise TooLongBookDescriptionException(length=100)


@dataclass
class BookName(BaseValue):
    value: str

    def validate(self) -> None:
        if len(self.value) < 1:
            raise TooShortBookNameException(length=1)
        if len(self.value) > 50:
            raise TooLongBookNameException(length=50)


@dataclass
class BookTheme(BaseValue):
    value: ThemesEnums

    def validate(self) -> None:
        if not isinstance(self.value, ThemesEnums):
            raise UnexpectedTypeException(value=self.value)
