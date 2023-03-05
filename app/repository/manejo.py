import pandas as pd

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