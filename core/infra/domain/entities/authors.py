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

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "last_name": self.last_name,
            "sex": self.sex,
        }
