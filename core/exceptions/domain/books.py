from dataclasses import dataclass

from core.exceptions.domain.base import BaseDomainException


@dataclass(eq=False)
class TooLongBookDescriptionException(BaseDomainException):
    value: str

    @property
    def message(self) -> str:
        return f"Length of the book description longer than expected {len(self.value)} > 100"


@dataclass(eq=False)
class TooShortBookDescriptionException(BaseDomainException):
    value: str

    @property
    def message(self) -> str:
        return (
            f"Length of the book description longer than expected {len(self.value)} < 5"
        )


@dataclass(eq=False)
class TooShortBookNameException(BaseDomainException):
    value: str

    @property
    def message(self) -> str:
        return f"Length of the book name shorter than expected {len(self.value)} < 1"


@dataclass(eq=False)
class TooLongBookNameException(BaseDomainException):
    value: str

    @property
    def message(self) -> str:
        return f"Length of the book name longer than expected {len(self.value)} > 50"
