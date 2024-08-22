from dataclasses import dataclass

from core.infra.domain.entities.authors import Author
from core.infra.domain.entities.base import BaseEntity
from core.infra.domain.values.books import BookTheme, BookName, BookDescription


@dataclass
class BookEntity(BaseEntity):
    description: BookDescription
    name: BookName
    theme: BookTheme
    authors: set["Author"]

    def add_author(self, author: Author):
        self.authors.add(author)
