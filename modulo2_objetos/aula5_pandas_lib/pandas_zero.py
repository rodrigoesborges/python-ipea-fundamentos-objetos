import pandas as pd


d = {
    'name': ['Joao', 'Enzo', 'Maria', 'Antonia', 'Luiza', 
             'Enzo', 'Mauro', 'Enzo', 'Diana', 'Marcela'],
    'city': ['BH', 'Brasília', 'Rio', 'Macaé', 'Porto Seguro',
             'Valparaíso', 'Londrina', 'Jequié', 'Rio', 'Santarém'],
    'id': [41, 28, 33, 34, 38, 70, 89, 100, 101, 105],
    'py-score': [88.0, 79.0, 81.0, 80, 0, 67, 54, 43, 23, 0]
    }
d = pd.DataFrame(d)

print(d)
print(d.head())
print(d.head(2))
print(d.tail())
print(d.columns)
print(d.city)
print(d.loc[0])
print(len(d))
print(d.loc[:, 'id'])
# Pausar no ponto para ver métodos disponíveis...
print(d['py-score'].mean())
print(d.info())
print(d.describe())
print(d['city'].value_counts())

# Todos valores 2025
d['ano'] = 2025

# Só linhas index de 0 a 
d.loc[:4, 'ano'] = 2024

# Filtragem por condição em uma coluna. Condição boleana dentro do colchetes da base
# base[base[coluna] condição]
d[d['py-score'] > 80]

# Na base já filtrada, podemos, por exemplo, escolher uma coluna e calcular a média 
d[d['py-score'] > 80]['py-score'].mean()

import numpy as np
data = pd.DataFrame(np.array([[1, 2, 3], 
                              [4, 5, 6], 
                              [7, 8, 9]]))

# Nomeando as colunas
data = pd.DataFrame(np.array([[1, 2, 3], 
                              [4, 5, 6], 
                              [7, 8, 9]]), 
                    columns=['x', 'y', 'z'],
                    index=['a', 'b', 'c'])

