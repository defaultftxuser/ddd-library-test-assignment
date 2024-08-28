from dataclasses import dataclass

from core.exceptions.domain.base import BaseDomainException


@dataclass(eq=False)
class TooShortUsernameException(BaseDomainException):
    value: str

    @property
    def message(self) -> str:
        return f"Too short username {len(self.value)} < 5"


@dataclass(eq=False)
class TooShortPasswordException(BaseDomainException):
    value: str

    @property
    def message(self) -> str:
        return f"Too short password {len(self.value)} < 5"
