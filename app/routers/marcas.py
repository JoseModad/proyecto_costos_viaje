from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request


from fastapi.templating import Jinja2Templates


from app.schemas import Categoria

from app.repository.manejo import obtener_marcas, obtener_diccionario, obtener_df



router = APIRouter(include_in_schema = False)

url = "http://localhost:8000"


templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def mostrar_formulario(request: Request,):
    marcas = obtener_marcas()   
    return templates.TemplateResponse("index.html", {"request": request, "marcas": marcas})


@router.post('/procesar')
async def procesar_categoria(categoria: Categoria): 
    data1 = obtener_diccionario()   
    marca = categoria.categoria
    modelos_vehiculos = [d.get('modelo') for d in data1 if d.get('marca') == marca]
    modelos_vehiculos = list(set(modelos_vehiculos))           
    return modelos_vehiculos 
       

@router.post('/procesar-cilindrada')
async def procesar_cilindrada(marca_modelo: dict):
    data1 = obtener_diccionario() 
    marca = marca_modelo['marca']
    modelo = marca_modelo['modelo']    
    cilindradas = []    
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo:
            cilindradas.append(vehiculo['cilindrada'])            
    cilindradas = list(set(cilindradas))    
    return {'cilindradas': cilindradas} 


@router.post('/procesar-transmision')
async def procesar_transmision(datos_vehiculo: dict):
    data1 = obtener_diccionario() 
    marca = datos_vehiculo['marca']
    modelo = datos_vehiculo['modelo']
    cilindrada = datos_vehiculo['cilindrada']
    transmisiones = []   
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo and vehiculo['cilindrada'] == cilindrada:
            transmisiones.append(vehiculo['transmision'])
    transmisiones = list(set(transmisiones))    
    return {'transmisiones': transmisiones}


@router.post('/procesar-combustible')
async def procesar_transmision(datos_coche: dict):
    data1 = obtener_diccionario() 
    marca = datos_coche['marca']
    modelo = datos_coche['modelo']
    cilindrada = datos_coche['cilindrada']
    transmision = datos_coche['transmision']
    combustible = []    
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo and vehiculo['cilindrada'] == cilindrada and vehiculo['transmision'] == transmision:
            combustible.append(vehiculo['combustible'])
    combustible = list(set(combustible))    
    return {'combustible': combustible}


@router.post('/procesar-cheked')
async def procesar_todo(datos1: dict):
    df = obtener_df()   
    marca = datos1['marca']
    modelo = datos1['modelo']
    cilindrada = datos1['cilindrada']
    transmision = datos1['transmision']
    combustible = datos1['combustible']
    consumo = datos1['check']    
    df_filtrado = df.query("marca == @marca and modelo == @modelo and cilindrada == @cilindrada and transmision == @transmision and combustible == @combustible")
    if consumo == 'urbano':
        consumo_col = 'urbano'
    elif consumo == 'ruta':
        consumo_col = 'ruta'
    else:
        consumo_col = 'mixto'        
    valores_columna = df_filtrado[consumo_col].to_list()[0]   
    return {"consumo": valores_columna}

