# Chama a biblioteca
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cria uma DataFrame, utilizando-se de um dicionário.
# Keys são column names
# Values, em listas, são os valores
data = pd.DataFrame({'col_a': [0, 1, 2, 3, 4, 5, 6, 7],
                     'col_b': [7, 6, 4, 2, 1, 1, 1, 0],
                     'strings': ['a', 'b', 'c', 9, 8, 7, np.nan, np.nan]})

# Exame dos dados
data.head()
data.columns
data.tail()
data.info()
data.describe()
data.mean(numeric_only=True)
data['col_a'].quantile(q=.9)
data.sum(numeric_only=True)
data.min(numeric_only=True)
data.max(numeric_only=True)


# Muito fácil de operar intercâmbio de dados.
# Para salvar para EXCEL, sempre inclua ponto e vírgula como separador
data.to_csv('data/nome_do_arquivo.csv', sep=';', index=False)

# Para ler o arquivo
data = pd.read_csv('data/nome_do_arquivo.csv', sep=';')

# Para deletar uma coluna
data.to_csv('data/nome_do_arquivo_com_index.csv', sep=';')
data = pd.read_csv('data/nome_do_arquivo_com_index.csv', sep=';')
data = data.drop('Unnamed: 0', axis=1)

# Identificar nomes colunas
data.columns

# Acessando colunas especificas
data.col_a.max()
data.col_b.sum()

# Alternativamente
data['col_a'].max()

# Seleciona linhas com valor maior que 3
maior_3_col_a = data.loc[data.col_a > 3, 'col_a']
maior_3_col_a_inclui_todas_cols = data.loc[data.col_a > 3, :]
menor_4_col_a_inclui_todas_cols = data.loc[data.col_a < 4, :]

is_na_string = data.loc[data.strings.isna(), :]
not_is_na_string = data.loc[~data.strings.isna(), :]

men_5_maior_3 = data.loc[(data.col_a < 4) & (data.col_a > 5), :]

maior_3_col_b = data.loc[data.col_a > 3, 'col_b']
oito_b = data.loc[data.strings == 8, 'col_b']
oito_b = data.loc[data.strings == '8', 'col_b']

# Renaming columns
data.rename(columns={'col_a': 'col_a1'}, inplace=True)

data = data.sort_values(by='col_a1', ascending=True)
data.groupby(by='col_b').col_b.agg(['sum', 'count'])

# Dropping NANs
data
data.dropna()

# Dropping a column. Axis 1 = column, Axis 0 = row
data.drop('col_a1', axis=1, inplace=False)  # Testem com inplace=True

# Selecting more than one column
double_colchetes = data[['col_a1', 'col_b']]
double_colchetes2 = data.drop('strings', axis=1)  #

# Para plotar direto do DataFrame
data.col_a1.plot(kind='hist')
plt.show()

data2 = pd.DataFrame({'outra_a': [20, 1, 92, 53, 4, 5, 6, 700],
                     'outra_b': [7, 26, 4, 45, 71, 71, 1, 870]})

data = pd.concat([data, data2], axis=1)

data3 = pd.DataFrame({'col_a': [20, 1, 92, 53, 4, 5, 6, 700],
                      'col_b': [7, 26, 4, 45, 71, 71, 1, 870],
                      'strings': ['a', np.nan, None, 9, 8, 7, 10, 11]})

data_nova2 = pd.concat([data, data3])

pd.merge(data, data3, how='inner')
pd.merge(data, data3, how='outer')
pd.merge(data, data3, how='left')
