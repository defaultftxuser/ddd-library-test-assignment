from fastapi import FastAPI

from core.api.users.router import router as user_router
from core.api.authors.router import router as author_router
from core.api.books.router import router as book_router


def get_app():

    app = FastAPI(title="Library API with auth")
    app.include_router(router=user_router)
    app.include_router(router=author_router)
    app.include_router(router=book_router)

    @app.get("/")
    async def main_page():
        return f"Hey there"

    return app
