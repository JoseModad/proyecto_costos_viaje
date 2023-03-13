from pydantic import BaseModel


class Categoria(BaseModel):
    categoria: str 
     
    
class Marca_modelo(BaseModel):
    marca: str
    modelo: str 
    
    
class Datos_vehiculos(BaseModel):
    marca: str
    modelo: str
    cilindrada: str
    
    
class Datos_coche(BaseModel):
    marca: str
    modelo: str
    cilindrada: str
    transmision: str
    
    
class Datos_todos(BaseModel):
    marca: str
    modelo: str
    cilindrada: str
    transmision: str
    combustible: str
    consumo: str