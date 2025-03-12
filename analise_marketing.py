import pandas as pd
marketing = pd.read_csv('./marketing.csv', delimiter=';')

# a) Imprima as primeiras 5 linhas do DataFrame marketing
print(marketing.head())

# b) Imprima um resumo estatístico de todas as colunas do DataFrame marketing
print(marketing.describe(include='all'))

# c) Imprima tipos de dados das colunas e a quantidade de valores não-nulos por coluna
print(marketing.info())
