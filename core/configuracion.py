import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float


env_path = Path(".") / ".env"

load_dotenv(dotenv_path = env_path)

class Settings:
    PROYECT_NAME: str = "PROYECTO-CONSUMO-VEHICULAR-FASTAPI"
    PROYECT_VERSION: str = "1.0"
    POSTGRES_DB :str = os.getenv("POSTGRES_DB")
    POSTGRES_USER :str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD :str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER :str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT :str = os.getenv("POSTGRES_PORT")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    

settings = Settings()

engine = create_engine(Settings.DATABASE_URL) 

Base = declarative_base() 


class Autos(Base):
    __tablename__ = 'autos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String)
    modelo = Column(String)
    cilindrada = Column(Integer)
    transmision = Column(String)
    combustible = Column(String)
    urbano = Column(Float)
    ruta = Column(Float)
    mixto = Column(Float)  
    

Base.metadata.create_all(bind = engine)