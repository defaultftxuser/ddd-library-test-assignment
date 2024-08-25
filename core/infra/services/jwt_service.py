import time
from copy import deepcopy
from dataclasses import dataclass

import jwt

from core.common.settings.config import Settings


@dataclass
class JWTService:
    config: Settings
    algorithm: str

    def verify_token(self, token: str) -> bool:
        try:
            result = jwt.decode(
                jwt=token, key=self.config.secret_jwt, algorithms=self.algorithm
            )
            if result.get("exp_time") < time.time():
                raise jwt.exceptions.ExpiredSignatureError("Token expired")
        except jwt.exceptions.PyJWTError:
            raise jwt.exceptions.PyJWTError("Wrong token")
        return True

    def create_access_token(self, payload: dict) -> str:
        access_token_payload = deepcopy(payload)
        access_token_payload["exp_time"] = int(time.time() + self.config.thirty_minutes)
        access_token = jwt.encode(
            payload=access_token_payload,
            key=self.config.secret_jwt,
            algorithm=self.algorithm,
        )
        return access_token

    def create_refresh_token(self, payload: dict) -> str:
        refresh_token_payload = deepcopy(payload)
        refresh_token_payload["exp_time"] = int(time.time() + self.config.one_month)
        refresh_token = jwt.encode(
            payload=refresh_token_payload,
            key=self.config.secret_jwt,
            algorithm=self.algorithm,
        )

        return refresh_token

    def refresh_token(self, payload: dict[str, str]) -> str:
        return self.create_access_token(payload)
