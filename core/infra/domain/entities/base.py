from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from core.infra.domain.events.base import BaseEvent
from core.infra.domain.values.base import BaseValue


@dataclass
class BaseEntity(ABC):
    oid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)  # noqa
    id: None | int = field(default=None, kw_only=True)  # noqa
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
    updated_at: datetime | None = field(default=None, kw_only=True)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, other: object) -> bool:  # noqa
        if not isinstance(other, BaseEntity):
            raise NotImplemented
        return self.oid == other.oid
