from abc import ABC, abstractmethod
from dataclasses import dataclass

import bcrypt


@dataclass
class BaseHashService(ABC):
    @abstractmethod
    def hash_data(self, input_data) -> str:
        ...

    @abstractmethod
    def compare_data(self, input_data, hashed_data) -> bool:
        ...


@dataclass
class BcryptHashService(BaseHashService):
    salt: bytes
    crypto_lib = bcrypt

    def hash_data(self, input_data: str | bytes) -> str:
        if not isinstance(input_data, bytes):
            input_data = input_data.encode(encoding="utf-8")
        return self.crypto_lib.hashpw(password=input_data, salt=self.salt).decode(
            encoding="utf-8"
        )

    def compare_data(self, input_data: str | bytes, hashed_data: bytes) -> bool:
        if not isinstance(input_data, bytes):
            input_data = input_data.encode(encoding="utf-8")
        return self.crypto_lib.checkpw(password=input_data, hashed_password=hashed_data)
