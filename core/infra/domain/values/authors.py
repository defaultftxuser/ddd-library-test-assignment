from dataclasses import dataclass

from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.base import BaseValue


@dataclass
class AuthorFirstNameValue:
    value: str


@dataclass
class AuthorSecondNameValue:
    value: str


@dataclass
class AuthorLastNameValue:
    value: str | None


@dataclass
class SexValue(BaseValue):
    value: SexEnum

    def validate(self) -> None:
        if not isinstance(self.value, SexEnum):
            raise TypeError
