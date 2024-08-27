from dataclasses import dataclass


@dataclass(eq=False)
class LimitOffsetFilter:
    limit: int = 10
    offset: int = 0
