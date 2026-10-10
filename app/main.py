# app/main.py
from fastapi import FastAPI

#from app.models import user  # Import models FIRST
#from app.database import engine, Base
from app.routes import register_routes
from app.exceptions import register_exception_handlers

#Base.metadata.create_all(bind=engine)

app = FastAPI(title="Python API Learning")
register_routes(app)
register_exception_handlers(app)