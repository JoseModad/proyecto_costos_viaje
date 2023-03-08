import pandas as pd

from app.schemas import Categoria

def obtener_diccionario():
    df = pd.read_csv('./app/db/consumo.csv', sep=',', encoding='utf-8')    
    data1 = df.to_dict('records')
    return data1

def obtener_marcas():
    data1 = obtener_diccionario()    
    llaves_marca = [d.get('marca') for d in data1 if d.get('marca')]
    marcas = list(set(llaves_marca))
    return marcas


def obtener_df():
    df = pd.read_csv('./app/db/consumo.csv', sep=',', encoding='utf-8')
    return df


def obtener_modelos(categoria: Categoria):
    data1 = obtener_diccionario()
    marca = categoria.categoria
    modelos_vehiculos = [d.get('modelo') for d in data1 if d.get('marca') == marca]
    modelos_vehiculos = list(set(modelos_vehiculos))           
    return modelos_vehiculos


def obtener_cilindrada(marca_modelo: dict):
    data1 = obtener_diccionario() 
    marca = marca_modelo['marca']
    modelo = marca_modelo['modelo']    
    cilindradas = []    
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo:
            cilindradas.append(vehiculo['cilindrada'])            
    cilindradas = list(set(cilindradas))    
    return cilindradas


def obtener_transmision(datos_vehiculo: dict):
    data1 = obtener_diccionario() 
    marca = datos_vehiculo['marca']
    modelo = datos_vehiculo['modelo']
    cilindrada = datos_vehiculo['cilindrada']
    transmisiones = []   
    for vehiculo in data1:
        if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo and vehiculo['cilindrada'] == cilindrada:
            transmisiones.append(vehiculo['transmision'])
    transmisiones = list(set(transmisiones))
    return transmisiones


def obtener_combustible(datos_coche: dict):
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
    return combustible


def obtener_tipo_recorrido(datos1):
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
    return valores_columna