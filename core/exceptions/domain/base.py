from dataclasses import dataclass


@dataclass(eq=False)
class BaseDomainException(BaseException):
    @property
    def message(self) -> str:
        return "unknown domain exception"
