from dataclasses import dataclass
from typing import Any


@dataclass
class CommonException(BaseException):
    value: Any

    @property
    def message(self) -> str:
        return f"Base common exception"
