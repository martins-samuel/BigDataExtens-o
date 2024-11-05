from faker import Faker
import pandas as pd
import random

#aqui se inicia o Faker para dados fictícios em português do Brasil
fake = Faker('pt_BR')
num_registros = 500

#lista de produtos que a MCG Papelaria vende
produtos = ["Caneta", "Lápis", "Caderno", "Papel A4", "Marcador", "Clips", "Borrachas", "Pastas", "Post-its", "Grampeador"]

#aqui se criação os dados fictícios
dados_vendas = []
for _ in range(num_registros):
    data_venda = fake.date_this_year()  # Data de venda no ano atual
    produto = random.choice(produtos)  # Produto vendido
    quantidade = random.randint(1, 20)  # Quantidade vendida
    preco_unitario = round(random.uniform(2, 50), 2)  # Preço unitário do produto
    cliente = fake.name()  # Nome brasileiro do cliente
    endereco = f"{fake.street_name()}, {random.randint(1, 100)}, Brasília - DF, {fake.postcode()}"  # Endereço simulado no DF
    
    #aqui calcula o valor total da venda
    valor_total = round(quantidade * preco_unitario, 2)
    
    #aqui adiciona o registro à lista de dados de vendas
    dados_vendas.append([data_venda, produto, quantidade, preco_unitario, valor_total, cliente, endereco])

#aqui se cria o DataFrame com os dados
df_vendas = pd.DataFrame(dados_vendas, columns=["Data", "Produto", "Quantidade", "Preço Unitário", "Valor Total", "Cliente", "Endereço"])

#aqui é salvo os dados em um arquivo CSV
df_vendas.to_csv("vendas_MCG_Papelaria.csv", index=False)

print("Dados fictícios de vendas para MCG Papelaria gerados e salvos em 'vendas_MCG_Papelaria.csv'.")
