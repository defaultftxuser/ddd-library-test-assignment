from dataclasses import dataclass

from pydantic import BaseModel

from core.infra.domain.entities.enums import SexEnum


@dataclass(eq=False)
class GetAuthorsSchema(BaseModel):
    id: int | None = None
    first_name: str | None = None
    second_name: str | None = None
    last_name: str | None = None
    creator_id: int | None = None


@dataclass(eq=False)
class AuthorSchema(BaseModel):
    first_name: str
    second_name: str
    last_name: str
    sex: SexEnum | None
