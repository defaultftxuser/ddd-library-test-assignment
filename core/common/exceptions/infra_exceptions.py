from dataclasses import dataclass

from core.common.exceptions.base import CommonException


@dataclass(eq=False)
class UsernameExistsException(CommonException):
    value: str

    @property
    def message(self) -> str:
        return f"User with that username already exists {self.value}"
