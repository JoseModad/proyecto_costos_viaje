from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.schemas import Categoria, Marca_modelo, Datos_vehiculos, Datos_coche, Datos_todos

from app.repository.manejo import obtener_marcas, obtener_modelos, obtener_cilindrada, obtener_transmision, obtener_combustible, obtener_tipo_recorrido



router = APIRouter(include_in_schema = False)

url = "http://localhost:8000"


templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def mostrar_formulario(request: Request):
    marcas = obtener_marcas()   
    return templates.TemplateResponse("index.html", {"request": request, "marcas": marcas})   


@router.post('/procesar')
async def procesar_categoria(categoria: Categoria): 
    modelos_vehiculos = obtener_modelos(categoria) 
    return modelos_vehiculos     
       

@router.post('/procesar-cilindrada')
async def procesar_cilindrada(marca_modelo: Marca_modelo):
    cilindradas = obtener_cilindrada(marca_modelo)    
    return {'cilindradas': cilindradas} 


@router.post('/procesar-transmision')
async def procesar_transmision(datos_vehiculo: Datos_vehiculos):
    transmisiones = obtener_transmision(datos_vehiculo)
    return {'transmisiones': transmisiones}


@router.post('/procesar-combustible')
async def procesar_combustible(datos_coche: Datos_coche):
    combustible = obtener_combustible(datos_coche)   
    return {'combustible': combustible}


@router.post('/procesar-cheked')
async def procesar_todo(datos_todos: Datos_todos):
    valores_columna = obtener_tipo_recorrido(datos_todos)       
    return {"consumo": valores_columna}