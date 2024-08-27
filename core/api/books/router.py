from fastapi import APIRouter, Query, Depends

from core.api.schemas.book_schemas import BookSchema
from core.common.filters.filters import LimitOffsetFilter
from core.infra.domain.values.enums import ThemesEnums
from core.infra.services.jwt_service import JWTService
from core.logic.commands.books.books_commands import (
    GetBookCommand,
    AddBookCommand,
    DeleteBookCommand,
)
from core.logic.container import resolve_mediator, resolve_auth
from core.logic.mediator import Mediator

router = APIRouter(prefix="/books")


@router.get("/")
async def get_books(
    id: int = Query(default=None),  # noqa
    name: str = Query(default=None),
    description: str = Query(default=None),
    theme: ThemesEnums = Query(default=None),
    mediator: Mediator = Depends(resolve_mediator),
    filters: LimitOffsetFilter = Depends(),
):
    try:
        result: list[list[dict]] = await mediator.handle_command(
            GetBookCommand(id=id, name=name, description=description, theme=theme)
        )
        return result[0][filters.offset : filters.offset + filters.limit]
    except Exception as e:
        raise e


@router.post("/")
async def add_books(
    book_schema: BookSchema,
    access_token: str,
    mediator: Mediator = Depends(resolve_mediator),
    auth_service: JWTService = Depends(resolve_auth),
) -> str:
    try:
        if user_info := auth_service.verify_token(access_token):
            await mediator.handle_command(
                command=AddBookCommand(
                    creator_id=user_info.get("id"), **book_schema.dict()
                )
            )
    except Exception as e:
        raise e
    return "book added"


@router.delete("/")
async def delete_books(
    book_schema: BookSchema,
    access_token: str,
    mediator: Mediator = Depends(resolve_mediator),
    auth_service: JWTService = Depends(resolve_auth),
) -> str:
    try:
        if user_info := auth_service.verify_token(access_token):
            await mediator.handle_command(
                DeleteBookCommand(creator_id=user_info.get("id"), **book_schema.dict())
            )
    except Exception as e:
        raise e
    return "book deleted"
