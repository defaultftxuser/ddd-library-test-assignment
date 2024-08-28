from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from core.api.schemas.user_schemas import UserInSchema, TokenSchema
from core.common.exceptions.base import AppException
from core.infra.domain.entities.users import UserEntity
from core.infra.domain.values.users import UsernameValue, PasswordValue
from core.infra.services.jwt_service import JWTService
from core.logic.commands.users.users_commands import (
    CreateUserCommand,
    CreateTokenUserCommand,
    DeactivateUserCommand,
)
from core.logic.container import resolve_mediator, resolve_auth
from core.logic.mediator import Mediator

router = APIRouter(prefix="/users")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user_entity: UserInSchema, mediator: Mediator = Depends(resolve_mediator)
) -> None:
    try:
        await mediator.handle_command(
            CreateUserCommand(
                **UserEntity(
                    username=UsernameValue(value=user_entity.username),
                    password=PasswordValue(value=user_entity.password),
                ).to_dict()
            )
        )
    except AppException as e:
        raise HTTPException(status_code=404, detail=e.message)

    return


@router.post("/login")
async def login_user(
    user_entity: UserInSchema, mediator: Mediator = Depends(resolve_mediator)
) -> dict[str, str]:
    try:
        tokens_dict: list[dict[str, str]] = await mediator.handle_command(
            CreateTokenUserCommand(**user_entity.dict())
        )
    except AppException as e:
        raise HTTPException(status_code=404, detail=e.message)
    return tokens_dict[0]


@router.patch("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def deactivate_user(
    access_token: TokenSchema,
    mediator: Mediator = Depends(resolve_mediator),
    auth_service: JWTService = Depends(resolve_auth),
) -> None:
    try:
        if user_info := auth_service.verify_token(access_token.access_token):
            await mediator.handle_command(DeactivateUserCommand(user_info.get("id")))

    except AppException as e:
        raise HTTPException(status_code=404, detail=e.message)
