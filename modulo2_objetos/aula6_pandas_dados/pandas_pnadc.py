import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_basics(path):
    # Load only needed columns
    cols = [
        'domicilioid', 'renda_trabalho_habitual', 'peso',
        'uf', 'trimestre', 'sexo'
    ]
    return pd.read_csv(path, sep=';', usecols=cols)


def weighted_mean(df, by, value, weight):
    # Compute weighted mean per group
    wm = df.groupby(by).apply(
        lambda x: np.average(x[value], weights=x[weight]),
        include_groups=False
    )
    wm.name = f'{value}_weighted_mean'
    return wm


if __name__ == '__main__':
    p = 'data/pnadc2020.csv'
    d = read_basics(p)

    # Weighted mean by household
    renda_med = weighted_mean(
        d, 'domicilioid', 'renda_trabalho_habitual', 'peso'
    )

    # Merge weighted household mean back to df
    d = d.merge(renda_med, on='domicilioid')

    var = 'renda_trabalho_habitual_weighted_mean'

    # Weighted income per UF
    print("\nMédia ponderada por UF:")
    print(d.groupby('uf')[var].mean())

    # Weighted income by quarter and UF
    print("\nMédia ponderada por trimestre e UF:")
    print(d.groupby(['trimestre', 'uf'])[var].mean())

    # Plot quarterly evolution
    d.groupby('trimestre')[var].mean().plot(marker='o')
    plt.title('Renda média ponderada por trimestre')
    plt.ylabel('Renda média (R$)')
    plt.xlabel('Trimestre')
    plt.show()

    # Plot by sex over time
    by_sex = d.groupby(['trimestre', 'sexo'])[var].mean().reset_index()

    plt.figure()
    for sex in by_sex['sexo'].unique():
        df_sex = by_sex[by_sex['sexo'] == sex]
        plt.plot(df_sex['trimestre'], df_sex[var], marker='o', label=f'Sexo {sex}')

    plt.title('Renda média ponderada por trimestre e sexo')
    plt.ylabel('Renda média (R$)')
    plt.xlabel('Trimestre')
    plt.legend()
    plt.show()
