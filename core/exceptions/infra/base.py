from dataclasses import dataclass

from core.common.exceptions.base import AppException


@dataclass(eq=False)
class BaseInfraException(AppException):
    value: str

    @property
    def message(self) -> str:
        return "Unknown infra exception"
