from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base



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