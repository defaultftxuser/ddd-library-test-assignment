from dataclasses import dataclass

from core.exceptions.domain.base import BaseDomainException


@dataclass(eq=False)
class TooShortUsernameException(BaseDomainException):
    length: int

    @property
    def message(self) -> str:
        return f"Too short username {self.length} < 5"


@dataclass(eq=False)
class TooShortPasswordException(BaseDomainException):
    length: int

    @property
    def message(self) -> str:
        return f"Too short username {self.length} < 5"
