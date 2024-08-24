import time
from copy import deepcopy
from dataclasses import dataclass

import jwt


@dataclass
class JWTService:
    key: str
    algorithm: str

    def verify_token(self, token: str):
        try:
            result = jwt.decode(jwt=token, key=self.key, algorithms=self.algorithm)
            print(result.get("exp_time"), int(time.time()))
            if result.get("exp_time") < time.time():
                raise jwt.exceptions.ExpiredSignatureError("Token expired")
        except jwt.exceptions.PyJWTError:
            raise jwt.exceptions.PyJWTError("Wrong token")
        return result

    def create_access_token(self, payload: dict) -> str:
        access_token_payload = deepcopy(payload)
        access_token_payload["exp_time"] = int(time.time() + (60 * 30))
        access_token = jwt.encode(
            payload=access_token_payload, key=self.key, algorithm=self.algorithm
        )
        return access_token

    def create_refresh_token(self, payload: dict) -> str:
        refresh_token_payload = deepcopy(payload)
        refresh_token_payload["exp_time"] = int(time.time() + (60 * 60 * 24 * 30))
        refresh_token = jwt.encode(
            payload=refresh_token_payload, key=self.key, algorithm=self.algorithm
        )

        return refresh_token

    def refresh_token(self, payload):
        return self.create_access_token(payload)
