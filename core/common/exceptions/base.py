from dataclasses import dataclass


@dataclass
class AppException(BaseException):
    value: str

    @property
    def message(self) -> str:
        return f"Base common exception"
