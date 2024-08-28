from dataclasses import dataclass

from core.exceptions.domain.users import (
    TooShortUsernameException,
    TooShortPasswordException,
)
from core.infra.domain.values.base import BaseValue


@dataclass(eq=False)
class UsernameValue(BaseValue):
    value: str

    def validate(self) -> None:
        if len(self.value) < 5:
            raise TooShortUsernameException(value=self.value)


@dataclass(eq=False)
class PasswordValue(BaseValue):
    value: str

    def validate(self) -> None:
        if len(self.value) < 5:
            raise TooShortPasswordException(value=self.value)
