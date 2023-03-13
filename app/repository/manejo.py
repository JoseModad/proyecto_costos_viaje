import pandas as pd

from app.schemas import Categoria, Marca_modelo, Datos_vehiculos, Datos_coche, Datos_todos

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
    modelos_vehiculos = [d.get('modelo') for d in data1 if d.get('marca') == categoria.categoria]
    modelos_vehiculos = list(set(modelos_vehiculos))           
    return modelos_vehiculos


def obtener_cilindrada(marca_modelo: Marca_modelo):    
    data1 = obtener_diccionario()       
    cilindradas = []    
    for vehiculo in data1:
        if vehiculo['marca'] == marca_modelo.marca and vehiculo['modelo'] == marca_modelo.modelo :
            cilindradas.append(vehiculo['cilindrada'])            
    cilindradas = list(set(cilindradas))    
    return cilindradas


def obtener_transmision(datos_vehiculo: Datos_vehiculos):
    data1 = obtener_diccionario() 
    transmisiones = []   
    for vehiculo in data1:
        if vehiculo['marca'] == datos_vehiculo.marca and vehiculo['modelo'] == datos_vehiculo.modelo and vehiculo['cilindrada'] == datos_vehiculo.cilindrada:
            transmisiones.append(vehiculo['transmision'])
    transmisiones = list(set(transmisiones))
    return transmisiones


def obtener_combustible(datos_coche: Datos_coche):
    data1 = obtener_diccionario() 
    combustible = []    
    for vehiculo in data1:
        if vehiculo['marca'] == datos_coche.marca and vehiculo['modelo'] == datos_coche.modelo and vehiculo['cilindrada'] == datos_coche.cilindrada and vehiculo['transmision'] == datos_coche.transmision:
            combustible.append(vehiculo['combustible'])
    combustible = list(set(combustible))
    return combustible


def obtener_tipo_recorrido(datos_todos: Datos_todos):    
    df = obtener_df()       
    df_filtrado = df.query("marca == @datos_todos.marca and modelo == @datos_todos.modelo and cilindrada == @datos_todos.cilindrada and transmision == @datos_todos.transmision and combustible == @datos_todos.combustible")
    if datos_todos.consumo == 'urbano':
        consumo_col = 'urbano'
    elif datos_todos.consumo == 'ruta':
        consumo_col = 'ruta'
    else:
        consumo_col = 'mixto'        
    valores_columna = df_filtrado[consumo_col].to_list()[0]
    return valores_columna