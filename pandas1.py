import pandas as pd


vendas_df = pd.read_csv(r'Contoso - Vendas  - 2017.csv', sep=';')

id_cliente = vendas_df['ID Cliente']

produtos_quantidade = vendas_df[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]


print(produtos_quantidade)




