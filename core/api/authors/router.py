from typing import Any

from fastapi import APIRouter, Depends, Query

from core.api.schemas.author_schemas import AuthorSchema
from core.common.filters.filters import LimitOffsetFilter
from core.infra.services.jwt_service import JWTService
from core.logic.commands.authors.authors_commands import (
    GetAuthorsCommand,
    DeleteAuthorCommand,
)
from core.logic.commands.books.books_commands import AddBookCommand
from core.logic.container import resolve_mediator, resolve_auth
from core.logic.mediator import Mediator

router = APIRouter(prefix="/authors")


@router.get("/")
async def get_authors(
    id: int = Query(default=None),  # noqa
    first_name: str = Query(default=None),
    second_name: str = Query(default=None),
    last_name: str = Query(default=None),
    creator_id: int = Query(default=None),
    mediator: Mediator = Depends(resolve_mediator),
    filters: LimitOffsetFilter = Depends(),
) -> list[dict[str, Any]]:
    try:
        result: list[list[dict[str, Any]]] = await mediator.handle_command(
            GetAuthorsCommand(
                id=id,
                first_name=first_name,
                second_name=second_name,
                last_name=last_name,
                creator_id=creator_id,
            )
        )
        return result[0][filters.offset : filters.offset + filters.limit]
    except Exception as e:
        raise e


@router.post("/")
async def add_author(
    author_schema: AuthorSchema,
    access_token: str,
    mediator: Mediator = Depends(resolve_mediator),
    auth_service: JWTService = Depends(resolve_auth),
):
    try:
        if user_info := auth_service.verify_token(access_token):
            await mediator.handle_command(
                command=AddBookCommand(
                    creator_id=user_info.get("id"), **author_schema.dict()
                )
            )
            return "author added"
    except Exception as e:
        raise e


@router.delete("/")
async def delete_author(
    author_schema: AuthorSchema,
    access_token: str,
    mediator: Mediator = Depends(resolve_mediator),
    auth_service: JWTService = Depends(resolve_auth),
):
    try:
        if user_info := auth_service.verify_token(access_token):
            await mediator.handle_command(
                command=DeleteAuthorCommand(
                    creator_id=user_info.get("id"), **author_schema.dict()  # noqa
                )
            )
    except Exception as e:
        raise e
