from sqlalchemy.orm import Session
from app.db.modelos import Autos
from app.schemas import Categoria, Marca_modelo, Datos_vehiculos, Datos_coche, Datos_todos


def obtener_marcas(db: Session):
    data = db.query(Autos.marca).distinct().all()
    data1 = [marca[0] for marca in data]    
    return data1


def obtener_modelos(categoria: Categoria, db: Session): 
    data = db.query(Autos.modelo).filter(Autos.marca == categoria.categoria).distinct().all()
    modelos_vehiculos = [modelo[0] for modelo in data]    
    return modelos_vehiculos


def obtener_cilindrada(marca_modelo: Marca_modelo, db: Session):    
    data = db.query(Autos.cilindrada).filter(Autos.marca == marca_modelo.marca, Autos.modelo == marca_modelo.modelo).distinct().all()
    cilindradas = [cilindrada[0] for cilindrada in data]    
    return cilindradas


def obtener_transmision(datos_vehiculo: Datos_vehiculos, db: Session):
    data = db.query(Autos.transmision).filter(Autos.marca == datos_vehiculo.marca, Autos.modelo == datos_vehiculo.modelo, Autos.cilindrada == datos_vehiculo.cilindrada).distinct().all()
    transmisiones = [transmision[0] for transmision in data]
    return transmisiones


def obtener_combustible(datos_coche: Datos_coche, db: Session):
    data = db.query(Autos.combustible).filter(Autos.marca == datos_coche.marca, Autos.modelo == datos_coche.modelo, Autos.cilindrada == datos_coche.cilindrada, Autos.transmision == datos_coche.transmision).distinct().all()
    combustible = [combustible[0] for combustible in data]
    return combustible


def obtener_tipo_recorrido(datos_todos: Datos_todos, db: Session):      
    if datos_todos.consumo == 'urbano':
        valores = db.query(Autos.urbano).filter(Autos.marca == datos_todos.marca, Autos.modelo == datos_todos.modelo, Autos.cilindrada == datos_todos.cilindrada, Autos.transmision == datos_todos.transmision, Autos.combustible == datos_todos.combustible).distinct().all()
        valores_columna = [recorrido[0] for recorrido in valores]        
        return valores_columna
   
    elif datos_todos.consumo == 'mixto':
        valores = db.query(Autos.mixto).filter(Autos.marca == datos_todos.marca, Autos.modelo == datos_todos.modelo, Autos.cilindrada == datos_todos.cilindrada, Autos.transmision == datos_todos.transmision, Autos.combustible == datos_todos.combustible).distinct().all()
        valores_columna = [recorrido[0] for recorrido in valores]        
        return valores_columna
    else:        
        valores = db.query(Autos.ruta).filter(Autos.marca == datos_todos.marca, Autos.modelo == datos_todos.modelo, Autos.cilindrada == datos_todos.cilindrada, Autos.transmision == datos_todos.transmision, Autos.combustible == datos_todos.combustible).distinct().all()
        valores_columna = [recorrido[0] for recorrido in valores]        
        return valores_columna
    