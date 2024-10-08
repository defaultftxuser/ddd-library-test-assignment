from dataclasses import dataclass

from core.common.exceptions.base import AppException


@dataclass(eq=False)
class BaseDomainException(AppException):
    value: str

    @property
    def message(self) -> str:
        return "unknown domain exception"
