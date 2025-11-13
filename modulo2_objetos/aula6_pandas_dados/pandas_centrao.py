import pandas as pd
import numpy as np


if __name__ == '__main__':
    p = 'data/centrao.xlsx'
    c = pd.read_excel(p)
    labels = c.columns
    c.columns = ['nome_mun', 'uf', 'cod_mun', 'votos_federal', 'perc_centrao', 'ranking']
    source = c.loc[5298]['nome_mun']
    len(c)
    c = c.dropna()
    len(c)
    c.loc[:, 'nome_mun'] = c.nome_mun.str.title()

    # Groupby
    # df.groupby(["coluna"]).coluna.funcao()
    c.groupby(['uf']).perc_centrao.mean()
    c.groupby(['uf']).perc_centrao.mean().sort_values(ascending=False)

    c.groupby(['uf']).votos_federal.max().sort_values(ascending=False).apply(lambda row: f'{row:,.2f}')

    c.groupby('uf').votos_federal.agg(['min', 'mean', 'max', 'count'])
    c.groupby('uf').votos_federal.agg(['min', 'mean', 'max']).map(lambda x: f'{x:,.0f}')

