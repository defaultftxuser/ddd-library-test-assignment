from dataclasses import dataclass


@dataclass(eq=False)
class CreateUserCommand:
    username: str
    password: str


@dataclass(eq=False)
class CreateTokenUserCommand:
    username: str
    password: str


@dataclass(eq=False)
class DeactivateUserCommand:
    username: str
    password: str
