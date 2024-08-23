from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Any, Generic


@dataclass
class BaseCommand(ABC):
    ...


Command = TypeVar("Command", bound=BaseCommand)
CommandResult = TypeVar("CommandResult", bound=Any)


@dataclass
class BaseHandler(ABC, Generic[Command, CommandResult]):
    @abstractmethod
    async def handle(self, command: Command) -> CommandResult:
        ...
