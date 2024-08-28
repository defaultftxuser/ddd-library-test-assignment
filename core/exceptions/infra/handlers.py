from core.exceptions.infra.base import BaseInfraException


class UserNotFoundException(BaseInfraException):
    value: str

    @property
    def message(self) -> str:
        return f"User not found"


class UserNotActiveException(BaseInfraException):
    value: str

    @property
    def message(self) -> str:
        return f"User with username {self.value} is not active"


class UsernameExistsException(BaseInfraException):
    value: str

    @property
    def message(self) -> str:
        return f"User with username {self.value} already exists"
