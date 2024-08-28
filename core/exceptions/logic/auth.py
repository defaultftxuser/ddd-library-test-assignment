from jwt import ExpiredSignatureError, PyJWTError

from core.common.exceptions.base import AppException


class WrongTokenException(AppException, ExpiredSignatureError):
    value: str

    @property
    def message(self) -> str:
        return f"Wrong token {self.value[:20]}..."


class TokenExpiredException(AppException, PyJWTError):
    value: str

    @property
    def message(self) -> str:
        return f"Token expired {self.value[:20]}..."
