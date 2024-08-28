from dataclasses import dataclass

from core.common.exceptions.base import AppException


@dataclass(eq=False)
class UnexpectedTypeException(AppException, TypeError):
    value: str

    @property
    def message(self) -> str:
        return f"Wrong type {self.value}"
