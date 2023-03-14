from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.schemas import Categoria, Marca_modelo, Datos_vehiculos, Datos_coche, Datos_todos

from app.repository.manejo import obtener_marcas, obtener_modelos, obtener_cilindrada, obtener_transmision, obtener_combustible, obtener_tipo_recorrido

from app.db.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(include_in_schema = False)

url = "http://localhost:8000"


templates = Jinja2Templates(directory="app/templates")




@router.get("/", response_class=HTMLResponse)
def mostrar_formulario(request: Request, db: Session = Depends(get_db)):
    marcas = obtener_marcas(db)   
    return templates.TemplateResponse("index.html", {"request": request, "marcas": marcas})   


@router.post('/procesar')
async def procesar_categoria(categoria: Categoria, db: Session = Depends(get_db)): 
    modelos_vehiculos = obtener_modelos(categoria, db) 
    return modelos_vehiculos     
       

@router.post('/procesar-cilindrada')
async def procesar_cilindrada(marca_modelo: Marca_modelo, db: Session = Depends(get_db)):
    cilindradas = obtener_cilindrada(marca_modelo, db)    
    return {'cilindradas': cilindradas} 


@router.post('/procesar-transmision')
async def procesar_transmision(datos_vehiculo: Datos_vehiculos, db: Session = Depends(get_db)):
    transmisiones = obtener_transmision(datos_vehiculo, db)
    return {'transmisiones': transmisiones}


@router.post('/procesar-combustible')
async def procesar_combustible(datos_coche: Datos_coche, db: Session = Depends(get_db)):
    combustible = obtener_combustible(datos_coche, db)   
    return {'combustible': combustible}


@router.post('/procesar-cheked')
async def procesar_todo(datos_todos: Datos_todos, db: Session = Depends(get_db)):
    valores_columna = obtener_tipo_recorrido(datos_todos, db)       
    return {"consumo": valores_columna}