

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/usuario/Downloads/mcg_papelaria_big_data/vendas_MCG_Papelaria.csv")

#Produtos mais vendidos (em quantidade e valor total)
produtos_mais_vendidos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
produtos_maior_receita = df.groupby('Produto')['Valor Total'].sum().sort_values(ascending=False)

#Média de valor de compra por cliente
valor_medio_cliente = df.groupby('Cliente')['Valor Total'].mean()

#Desempenho por região (com base no endereço)
vendas_por_regiao = df.groupby('Endereço')['Valor Total'].sum()

#Frequência de compras por cliente
frequencia_cliente = df['Cliente'].value_counts()

#Ticket médio geral
ticket_medio = df['Valor Total'].mean()

#Produtos mais comprados por cliente
produtos_por_cliente = df.groupby(['Cliente', 'Produto']).size().unstack().fillna(0)

 #Distribuição de preços dos produtos vendidos
Distribuição_de_preços = df['Preço Unitário'].plot(kind='hist', bins=10)

#Relação entre preço unitário e quantidade vendida
Relação_PU_Q = df.plot.scatter(x='Preço Unitário', y='Quantidade')

#Prints

print("Produtos mais vendidos:\n", produtos_mais_vendidos)
print("\nProdutos de maior receita:\n", produtos_maior_receita)
print("\nMédia de valor de compra por cliente:\n", valor_medio_cliente)
print("\nDesempenho por região (com base no endereço):\n", vendas_por_regiao)
print("\nFrequência de compras por cliente:\n", frequencia_cliente)
print("\nTicket médio geral:\n", ticket_medio)
print("\nProdutos mais comprados por cliente:\n", produtos_por_cliente)
print("\nDistribuição de preços dos produtos vendidos:\n", Distribuição_de_preços)
print("\nRelação entre preço unitário e quantidade vendida:\n", Relação_PU_Q)






