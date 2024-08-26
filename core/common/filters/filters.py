from dataclasses import dataclass


@dataclass(eq=False)
class LimitOffsetFilter:
    limit: int | None = 10
    offset: int | None = 0
