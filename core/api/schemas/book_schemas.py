from dataclasses import dataclass

from pydantic import BaseModel

from core.infra.domain.values.enums import ThemesEnums


@dataclass(eq=False)
class BookSchema(BaseModel):
    name: str | None
    description: str | None
    theme: ThemesEnums | None
