from enum import Enum


class SexEnum(Enum):
    male = "male"
    female = "female"

    def __str__(self) -> str:
        return self.value
