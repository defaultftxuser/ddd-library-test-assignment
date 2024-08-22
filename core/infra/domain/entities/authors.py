from dataclasses import dataclass

from core.infra.domain.entities.base import BaseEntity
from core.infra.domain.entities.enums import SexEnum


@dataclass(eq=False)
class Author(BaseEntity):
    first_name: str | None
    second_name: str | None
    last_name: str | None
    sex: SexEnum | None
