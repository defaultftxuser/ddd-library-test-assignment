from pydantic import BaseModel


class UserInSchema(BaseModel):
    username: str
    password: str


class UserOutSchema(BaseModel):
    id: int
    username: str


class TokenOutSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenSchema(BaseModel):
    access_token: str
