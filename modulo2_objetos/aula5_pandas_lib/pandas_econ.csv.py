import pandas as pd

econ = pd.read_csv("data/economia_br_firms.csv")
print(econ.head)


# Exercícios práticos com a base economia_br_firms.csv
# 1. Firmas com >100 empregados
print("Firmas com mais de 100 empregados:")
print(econ[econ['employees'] > 100].head())


# 2. Setor de tecnologia fora de SP
print("Empresas do setor de tecnologia fora de SP:")
print(econ[(econ['sector'] == 'Tecnologia') & (econ['state'] != 'SP')].head())


# 3. Cidades com desemprego > 12%
print("Cidades com desemprego maior que 12%:")
print(econ[econ['unemployment_rate'] > 12][['city','state','unemployment_rate']].drop_duplicates().head())


# 4. Produtividade: revenue / employees
print("Criando coluna de produtividade:")
econ['productivity'] = econ['revenue'] / econ['employees']
print(econ[['city','sector','employees','revenue','productivity']].head())


# 5. Média de empregados por setor
print("Média de empregados por setor:")
print(econ.groupby('sector')['employees'].mean())


# 6. Faturamento médio por estado
print("Faturamento médio por estado:")
print(econ.groupby('state')['revenue'].mean())


# 7. Massa salarial total por região
print("Massa salarial total por região:")

print(econ.groupby('state')['wage_bill'].sum())


# 8. Top 5 maiores faturamentos
print("Top 5 empresas por faturamento:")
print(econ.sort_values('revenue', ascending=False).head())
print(econ.info())
print(econ.describe())


# seleção e filtros
print("\nEmpresas com mais de 100 empregados:")
print(econ[econ['employees'] > 100].head())


print("\nSomatório de empregados por setor:")
print(econ.groupby('sector')['employees'].sum())


# nova coluna — produtividade
print("\nCriando coluna produtividade (faturamento/empregados)")
econ['productivity'] = econ['revenue'] / econ['employees']
print(econ[['sector','employees','revenue','productivity']].head())


# ordenação
print("\nTop 5 empresas por produtividade:")
print(econ.sort_values('productivity', ascending=False).head())


# value counts
print("\nFrequência por setor:")
print(econ['sector'].value_counts())