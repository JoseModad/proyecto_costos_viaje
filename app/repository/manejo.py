import pandas as pd


df1 = pd.read_csv('./app/db/consumo.csv', sep=',', encoding='utf-8')

df = df1[['marca', 'modelo', 'cilindrada', 'transmision', 'combustible', 'urbano', 'ruta', 'mixto']]

data1 = df.to_dict('records')

llaves_marca = [d.get('marca') for d in data1 if d.get('marca')]

marcas = list(set(llaves_marca))