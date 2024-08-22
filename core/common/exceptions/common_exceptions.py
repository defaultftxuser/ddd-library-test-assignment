from dataclasses import dataclass

from core.common.exceptions.base import CommonException


@dataclass
class UnexpectedTypeException(CommonException):

    @property
    def message(self) -> str:
        return f"Wrong value type {self.value.__class__}"
