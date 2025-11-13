import matplotlib.pyplot as plt
import pandas as pd

# 0. Iterating over a groupby
# 1. List comprehension. Dictionary comprehension


# Tarefas:
# 1. Quantos dias em média entre o pedido (OrderDate) e a postagem (ShipDate). Use pd.to_datetime(column).
# Faça a diferença.
# 2. Faça uma frequencia (value_counts) da coluna ShipStatus
# 3. Some o Profit por State e ordene. California lucrou mais? E o segundo?
# 4. Quais são as 4 categorias de envio (ShipMode)? Qual é o mais lucrativo?

def produz_respostas(data):
    print('Questao 1')
    data['tempo_handling'] = pd.to_datetime(data['ShipDate']) - pd.to_datetime(data['OrderDate'])
    print(f"Média entre pedido e entrega postada: {data['tempo_handling'].mean()}")
    print('')
    print('Questao 2')
    print(f"Frequência Ship Status: \n{data['ShipStatus'].value_counts().apply(lambda value: f'{value:,}')}")
    print('')
    print('Questao 3')
    res = data.groupby('State').agg('sum')['Profit'].sort_values(ascending=False).head()
    print(res.apply(lambda value: f"{value:,}"))
    print('')
    print('Questao 4')
    q4 = data.groupby('ShipMode').agg(['sum', 'count'])['Profit']
    print('Categorias de envio: ')
    print([i for i in q4.index])
    q4['ModeProfit'] = q4['sum'] / q4['count']
    print('Lucro máximo: ')
    print(q4[q4['ModeProfit'] == q4['ModeProfit'].max()])


def exemplo_iterate_over_group(data, by='ShipMode'):
    print(f'Num. linhas originais: {len(data)}')
    for name, grupo in data.groupby(by):
        print(f'\nNome do grupo: {name}, a partir da coluna: {by}\n'
              f'tipo objeto {type(grupo)}, '
              f'tamanho grupo: {len(grupo)}')
    # Alternativa para imprimir nome e grupo usando lista comprehension -->
    # gr = [g for n, g in d2.groupby('ShipMode')]


def direto_csv_net(address):
    return pd.read_csv(f'{address}?raw=True')


if __name__ == '__main__':
    p2 = 'https://raw.githubusercontent.com/metatron-app/metatron-doc-discovery/master/_static/data/sales-data-sample.csv'
    d2 = pd.read_csv(p2)
    exemplo_iterate_over_group(d2)
    produz_respostas(d2)

    # Plot rápido
    d2.plot(x='longitude', y='latitude', kind='scatter')
    plt.show()
    d3 = d2.groupby('ShipMode').agg(['sum', 'count'])['Profit']




