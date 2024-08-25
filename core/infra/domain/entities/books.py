from dataclasses import dataclass, field

from core.infra.domain.entities.authors import Author
from core.infra.domain.entities.base import BaseEntity
from core.infra.domain.values.books import BookTheme, BookName, BookDescription


@dataclass
class BookEntity(BaseEntity):
    description: BookDescription
    name: BookName
    theme: BookTheme
    authors: set["Author"] = field(default_factory=set)

    def add_author(self, author: Author) -> None:
        self.authors.add(author)
