from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, TypeVar, Generic

from core.common.exceptions.common import UnexpectedTypeException

Value = TypeVar("Value")


@dataclass
class BaseValue(Generic[Value], ABC):
    value: Value

    def __post_init__(self) -> None:
        return self.validate()

    def update_value(self, new_value: Any) -> None:
        if new_value.__class__ != self.value.__class__:
            raise UnexpectedTypeException(value=new_value)
        self.value = new_value
        self.validate()

    @abstractmethod
    def validate(self) -> None:
        ...
