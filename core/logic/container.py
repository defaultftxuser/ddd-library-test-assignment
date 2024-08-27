from functools import lru_cache

from punq import Container, Scope

from core.common.settings.config import Settings, get_settings
from core.infra.db.sql_db.models import User, Author, Book, BookAuthor
from core.infra.repositories.authors.authors_repository import (
    BaseAuthorRepository,
    AuthorRepository,
)
from core.infra.repositories.books.books_repository import (
    BaseBookRepository,
    BookRepository,
    BaseBookAuthorRepository,
    BookAuthorRepository,
)
from core.infra.repositories.database_config import Database
from core.infra.repositories.users.users_repository import (
    UserRepository,
    BaseUserRepository,
)
from core.infra.services.hash_service import BaseHashService, BcryptHashService
from core.infra.services.jwt_service import JWTService
from core.logic.commands.authors.authors_commands import (
    AddAuthorCommand,
    GetAuthorsCommand,
    DeleteAuthorCommand,
)
from core.logic.commands.authors.authors_handlers import (
    AddAuthorCommandHandler,
    GetAuthorsCommandHandler,
    DeleteAuthorCommandHandler,
)
from core.logic.commands.books.books_commands import (
    GetBookCommand,
    DeleteBookCommand,
    AddBookCommand,
    LinkBookAuthorCommand,
)
from core.logic.commands.books.books_handlers import (
    GetBookCommandHandler,
    DeleteBookCommandHandler,
    AddBookCommandHandler,
    LinkBookAuthorCommandHandler,
)
from core.logic.commands.users.users_commands import (
    CreateUserCommand,
    CreateTokenUserCommand,
    DeactivateUserCommand,
)
from core.logic.commands.users.users_handlers import (
    CreateUserCommandHandler,
    CreateTokenUserCommandHandler,
    DeactivateUserCommandHandler,
)
from core.logic.mediator import Mediator


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def resolve_mediator() -> Mediator:
    container = init_container()
    return container.resolve(Mediator)


def _init_container() -> Container:
    container = Container()

    # register common layer dependencies

    container.register(Settings, factory=get_settings, scope=Scope.singleton)

    settings: Settings = container.resolve(Settings)

    container.register(
        Database, instance=Database(url=settings.get_db_url), scope=Scope.singleton
    )

    # register infra layer dependencies

    container.register(
        BaseUserRepository,
        instance=UserRepository(model=User, database=container.resolve(Database)),
        scope=Scope.singleton,
    )

    container.register(
        BaseAuthorRepository,
        instance=AuthorRepository(model=Author, database=container.resolve(Database)),
        scope=Scope.singleton,
    )

    container.register(
        BaseBookAuthorRepository,
        instance=BookAuthorRepository(
            model=BookAuthor, database=container.resolve(Database)
        ),
        scope=Scope.singleton,
    )

    container.register(
        BaseBookRepository,
        instance=BookRepository(model=Book, database=container.resolve(Database)),
        scope=Scope.singleton,
    )

    container.register(
        JWTService,
        instance=JWTService(config=settings, algorithm=settings.algorithm),
        scope=Scope.singleton,
    )
    container.register(
        BaseHashService,
        instance=BcryptHashService(salt=settings.hash_salt),
        scope=Scope.singleton,
    )

    def init_mediator():
        mediator = Mediator()

        # handlers

        create_user_command_handler = CreateUserCommandHandler(
            repository=container.resolve(BaseUserRepository),
            hash_service=container.resolve(BaseHashService),
        )
        create_token_user_command_handler = CreateTokenUserCommandHandler(
            repository=container.resolve(BaseUserRepository),
            auth_service=container.resolve(JWTService),
            hash_service=container.resolve(BaseHashService),
        )
        deactivate_user_command_handler = DeactivateUserCommandHandler(
            repository=container.resolve(BaseUserRepository),
            hash_service=container.resolve(BaseHashService),
        )
        add_author_command_handler = AddAuthorCommandHandler(
            repository=container.resolve(BaseAuthorRepository)
        )
        get_authors_command_handler = GetAuthorsCommandHandler(
            repository=container.resolve(BaseAuthorRepository)
        )
        delete_author_command_handler = DeleteAuthorCommandHandler(
            repository=container.resolve(BaseAuthorRepository)
        )

        get_book_command_handler = GetBookCommandHandler(
            repository=container.resolve(BaseBookRepository)
        )
        delete_book_command_handler = DeleteBookCommandHandler(
            repository=container.resolve(BaseBookRepository)
        )
        doo_book_command_handler = AddBookCommandHandler(
            repository=container.resolve(BaseBookRepository)
        )
        link_book_author__command_handler = LinkBookAuthorCommandHandler(
            repository=container.resolve(BaseBookAuthorRepository)
        )

        # register user commands

        mediator.register_command(
            command=CreateUserCommand, handlers=[create_user_command_handler]
        )
        mediator.register_command(
            command=CreateTokenUserCommand, handlers=[create_token_user_command_handler]
        )
        mediator.register_command(
            command=DeactivateUserCommand, handlers=[deactivate_user_command_handler]
        )

        # register author commands

        mediator.register_command(
            command=AddAuthorCommand, handlers=[add_author_command_handler]
        )
        mediator.register_command(
            command=GetAuthorsCommand, handlers=[get_authors_command_handler]
        )
        mediator.register_command(
            command=DeleteAuthorCommand, handlers=[delete_author_command_handler]
        )

        # register book commands

        mediator.register_command(
            command=GetBookCommand, handlers=[get_book_command_handler]
        )
        mediator.register_command(
            command=DeleteBookCommand, handlers=[delete_book_command_handler]
        )
        mediator.register_command(
            command=AddBookCommand, handlers=[doo_book_command_handler]
        )

        # register book_author commands

        mediator.register_command(
            command=LinkBookAuthorCommand, handlers=[link_book_author__command_handler]
        )

        return mediator

    container.register(Mediator, factory=init_mediator, scope=Scope.singleton)
    return container
