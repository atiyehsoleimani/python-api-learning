from fastapi import FastAPI

from . import post_routes, user_routes


def register_routes(app: FastAPI) -> None:
    app.include_router(user_routes.router)
    app.include_router(post_routes.router)