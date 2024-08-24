from dotenv import load_dotenv, find_dotenv
from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    postgres_host: str = Field(alias="POSTGRES_HOST", default="localhost")
    postgres_user: str = Field(alias="POSTGRES_USER")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(alias="POSTGRES_DB")
    postgres_port: int = Field(alias="POSTGRES_PORT")
    db_engine: str = Field(alias="DB_ENGINE")
    secret_jwt: str = Field(alias="SECRET_JWT")
    algorithm: str = Field(alias="JWT_ALGORITHM")
    hash_salt: bytes = Field(alias="HASH_SALT")
    model_config = SettingsConfigDict(case_sensitive=True)

    @property
    def get_db_url(self):
        return (
            f"{self.db_engine}://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


def get_settings():
    return Settings()
