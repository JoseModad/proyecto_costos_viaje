from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import pandas as pd

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from pydantic import BaseModel


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


df1 = pd.read_csv('./app/db/consumo.csv', sep=',', encoding='utf-8')

df = df1[['marca', 'modelo', 'cilindrada', 'transmision', 'combustible', 'urbano', 'ruta', 'mixto']]

data1 = df.to_dict('records')

llaves_marca = [d.get('marca') for d in data1 if d.get('marca')]

marcas = list(set(llaves_marca))


class Categoria(BaseModel):
    categoria: str   

@app.get("/", response_class=HTMLResponse)
def mostrar_formulario(request: Request, form_submitted: bool = False, response_success: bool = False):
# Renderizar la plantilla HTML con las marcas en una variable    
    return templates.TemplateResponse("index.html", {"request": request, "marcas": marcas, "form_submitted": form_submitted, "response_success": response_success})

@app.post('/procesar')
async def procesar_categoria(categoria: Categoria):
    # Procesar la categoría recibida
    marca = categoria.categoria
    modelos_vehiculos = [d.get('modelo') for d in data1 if d.get('marca') == marca]
    modelos_vehiculos = list(set(modelos_vehiculos))           
    return modelos_vehiculos 
       
# Definir la ruta para procesar la cilindrada
@app.post('/procesar-cilindrada')
async def procesar_cilindrada(marca_modelo: dict):
    marca = marca_modelo['marca']
    modelo = marca_modelo['modelo']    
    cilindradas = []
    # Filtrar las cilindradas según la marca y el modelo
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo:
            cilindradas.append(vehiculo['cilindrada'])            
    cilindradas = list(set(cilindradas))
    # Retornar las cilindradas en formato JSON
    return {'cilindradas': cilindradas} 

@app.post('/procesar-transmision')
async def procesar_transmision(datos_vehiculo: dict):
    marca = datos_vehiculo['marca']
    modelo = datos_vehiculo['modelo']
    cilindrada = datos_vehiculo['cilindrada']
    transmisiones = []
    # Filtrar las transmisiones según la marca, modelo y cilindrada
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo and vehiculo['cilindrada'] == cilindrada:
            transmisiones.append(vehiculo['transmision'])
    transmisiones = list(set(transmisiones))
    
    return {'transmisiones': transmisiones}

@app.post('/procesar-combustible')
async def procesar_transmision(datos_coche: dict):
    marca = datos_coche['marca']
    modelo = datos_coche['modelo']
    cilindrada = datos_coche['cilindrada']
    transmision = datos_coche['transmision']
    combustible = []
    # Filtrar las transmisiones según la marca, modelo y cilindrada
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo and vehiculo['cilindrada'] == cilindrada and vehiculo['transmision'] == transmision:
            combustible.append(vehiculo['combustible'])
    combustible = list(set(combustible))    
    return {'combustible': combustible}

    
@app.post('/procesar-todo')
async def procesar_todo(datos: dict):
    marca = datos['marca']
    modelo = datos['modelo']
    cilindrada = datos['cilindrada']
    transmision = datos['transmision']
    combustible = datos['combustible']    
    return {'recibido'}


@app.post('/procesar-cheked')
async def procesar_todo(datos1: dict):    
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





# if __name__ == "__main__":
#     config = Config()
#     config.bind = ['localhost:8000']
#     config.use_reloader = True
#     uvicorn.run("main:app", host=config.bind[0].split(":")[0], port=int(config.bind[0].split(":")[1]), reload=True, workers=1)