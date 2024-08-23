from dataclasses import dataclass

from core.exceptions.domain.base import BaseDomainException


@dataclass(eq=False)
class TooLongBookDescriptionException(BaseDomainException):
    length: int

    @property
    def message(self) -> str:
        return (
            f"Length of the book description longer than expected {self.length} > 100"
        )


@dataclass(eq=False)
class TooShortBookDescriptionException(BaseDomainException):
    length: int

    @property
    def message(self) -> str:
        return f"Length of the book description longer than expected {self.length} < 5"


@dataclass(eq=False)
class TooShortBookNameException(BaseDomainException):
    length: int

    @property
    def message(self) -> str:
        return f"Length of the book name shorter than expected {self.length} < 1"


@dataclass(eq=False)
class TooLongBookNameException(BaseDomainException):
    length: int

    @property
    def message(self) -> str:
        return f"Length of the book name longer than expected {self.length} > 50"
