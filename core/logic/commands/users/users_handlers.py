from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError

from core.common.exceptions.infra_exceptions import UsernameExistsException
from core.infra.domain.entities.users import UserHashedPasswordEntity
from core.infra.repositories.users.users_repository import UserRepository
from core.infra.services.hash_service import BcryptHashService
from core.infra.services.jwt_service import JWTService
from core.logic.commands.base import BaseHandler, CommandResult, Command
from core.logic.commands.users.users_commands import (
    CreateUserCommand,
    CreateTokenUserCommand,
    DeactivateUserCommand,
)


@dataclass(eq=False)
class CreateUserCommandHandler(BaseHandler):
    repository: UserRepository
    hash_service: BcryptHashService
    auth_service: JWTService

    async def handle(self, command: CreateUserCommand) -> tuple[str, str]:
        try:
            user_entity = UserHashedPasswordEntity(
                username=command.username,
                hashed_password=self.hash_service.hash_data(command.password),
            )
            result = await self.repository.create_user(**user_entity.__dict__)
            access_token = self.auth_service.create_access_token(result.__dict__)
            refresh_token = self.auth_service.create_access_token(result.__dict__)
            return access_token, refresh_token

        except IntegrityError:
            raise UsernameExistsException(value=command.username)


@dataclass(eq=False)
class CreateTokenUserCommandHandler(BaseHandler):
    repository: UserRepository
    hash_service: BcryptHashService
    auth_service: JWTService

    async def handle(self, command: CreateTokenUserCommand) -> dict[str, str]:
        hashed_password_entity = UserHashedPasswordEntity(
            username=command.username,
            hashed_password=self.hash_service.hash_data(command.password),
        )
        user_entity = await self.repository.get_one_or_none(
            **hashed_password_entity.__dict__
        )
        try:
            if user_entity.get("is_active", False):
                payload = {
                    "id": user_entity.get("id"),
                    "username": user_entity.get("username"),
                }
                access_token = self.auth_service.create_access_token(payload=payload)
                refresh_token = self.auth_service.create_refresh_token(payload=payload)
                return {"access_token": access_token, "refresh_token": refresh_token}
        except TypeError as e:
            raise e

        raise Exception("User not active")


@dataclass(eq=False)
class DeactivateUserCommandHandler(BaseHandler):
    repository: UserRepository
    hash_service: BcryptHashService

    async def handle(self, command: DeactivateUserCommand) -> None:
        hashed_password_entity = UserHashedPasswordEntity(
            username=command.username,
            hashed_password=self.hash_service.hash_data(command.password),
        )
        await self.repository.deactivate_user(hashed_password_entity.__dict__)
