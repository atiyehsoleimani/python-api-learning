from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.models.base import Base


engine = create_engine(
    settings.database_url, 
    connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

#Base.metadata.create_all(bind=engine)