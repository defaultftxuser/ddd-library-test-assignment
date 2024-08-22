from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from core.infra.domain.events.base import BaseEvent
from core.infra.domain.values.base import BaseValue


@dataclass
class BaseEntity(ABC):
    oid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    id: int = field(default=None, kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
    updated_at: datetime = field(default=None, kw_only=True)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, other: "BaseEntity") -> bool:
        return self.oid == other.oid

    def register_event(self, event: "BaseValue"):
        ...



