from dataclasses import dataclass

from core.infra.domain.entities.base import BaseEntity
from core.infra.domain.entities.enums import SexEnum
from core.infra.domain.values.authors import (
    AuthorLastNameValue,
    AuthorFirstNameValue,
    AuthorSecondNameValue,
)


@dataclass(eq=False)
class Author(BaseEntity):
    first_name: AuthorFirstNameValue
    second_name: AuthorSecondNameValue
    last_name: AuthorLastNameValue
    sex: SexEnum | None
