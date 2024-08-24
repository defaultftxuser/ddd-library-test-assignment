from abc import ABC, abstractmethod
from dataclasses import dataclass

import bcrypt


@dataclass
class BaseHashService(ABC):
    salt: bytes
    crypto_lib: bytes

    @abstractmethod
    def hash_data(self, input_data) -> bytes:
        ...

    @abstractmethod
    def compare_data(self, input_data, hashed_data) -> bool:
        ...


@dataclass
class BcryptHashService(BaseHashService):

    crypto_lib = bcrypt

    def hash_data(self, input_data) -> bytes:
        return self.crypto_lib.hashpw(password=input_data, salt=self.salt)

    def compare_data(self, input_data, hashed_data) -> bool:
        return self.crypto_lib.checkpw(password=input_data, hashed_password=hashed_data)
