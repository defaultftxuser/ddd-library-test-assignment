from dataclasses import dataclass

from core.common.exceptions.base import AppException


@dataclass(eq=False)
class BaseLogicException(AppException):
    value: str

    @property
    def message(self) -> str:
        return "unknown logic exception"
