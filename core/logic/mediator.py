from collections import defaultdict
from dataclasses import dataclass, field
from typing import Sequence, Type

from core.logic.commands.base import BaseCommand, BaseHandler, CommandResult


@dataclass(eq=False)
class Mediator:  # TODO: написать events, query и хэндлеры
    commands_map: dict[Type[BaseCommand], list[BaseHandler]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def register_command(
        self, command: Type[BaseCommand], handlers: Sequence[BaseHandler]
    ) -> None:
        self.commands_map[command].extend(handlers)

    async def handle_command(self, command: BaseCommand) -> list[CommandResult]:
        command_type = command.__class__
        results = []
        for handlers in self.commands_map[command_type]:
            results.append(await handlers.handle(command))
        return results
