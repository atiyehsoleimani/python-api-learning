from fastapi import FastAPI
from app.routes import register_routes
from app.exceptions import register_exception_handlers

app = FastAPI()
register_routes(app)
register_exception_handlers(app)
