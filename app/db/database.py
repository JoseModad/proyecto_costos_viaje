from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from core.configuracion import settings
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL) 

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

Base = declarative_base() 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()