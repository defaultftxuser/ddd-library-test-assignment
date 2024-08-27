from fastapi import APIRouter, Depends, HTTPException

from core.api.schemas.user_schemas import UserInSchema, TokenSchema
from core.common.exceptions.base import CommonException
from core.common.exceptions.infra_exceptions import UsernameExistsException
from core.infra.services.jwt_service import JWTService
from core.logic.commands.users.users_commands import (
    CreateUserCommand,
    CreateTokenUserCommand,
    DeactivateUserCommand,
)
from core.logic.container import resolve_mediator, resolve_auth
from core.logic.mediator import Mediator

router = APIRouter(prefix="/users")


@router.post("/register")
async def register_user(
    user_entity: UserInSchema, mediator: Mediator = Depends(resolve_mediator)
) -> str:
    try:
        await mediator.handle_command(CreateUserCommand(**user_entity.dict()))
    except UsernameExistsException as e:
        return e.message
    return "Hehe"


@router.post("/login")
async def login_user(
    user_entity: UserInSchema, mediator: Mediator = Depends(resolve_mediator)
):
    try:
        tokens_dict: list[dict[str, str]] = await mediator.handle_command(
            CreateTokenUserCommand(**user_entity.dict())
        )
    except CommonException as e:
        raise HTTPException(status_code=404, detail=e.message)
    return tokens_dict[0]


@router.patch("/delete")
async def deactivate_user(
    access_token: TokenSchema,
    mediator: Mediator = Depends(resolve_mediator),
    auth_service: JWTService = Depends(resolve_auth),
) -> str:
    try:
        if user_info := auth_service.verify_token(access_token.access_token):
            await mediator.handle_command(DeactivateUserCommand(user_info.get("id")))

    except CommonException as e:
        raise HTTPException(status_code=404, detail=e.message)
    return "Deactivated"
