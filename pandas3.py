import pandas as pd

vendas_df = pd.read_csv(r'Contoso - Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep =';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep =';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep =';')



clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Categoria']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]



vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')


vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
#print(frequencia_clientes[:10])

frequencia_clientes[:5].plot(figsize=(15, 5))


vendas_lojas = vendas_df.groupby("Nome da Loja").sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
vendas_lojas

vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending=False)
display(vendas_lojas)
vendas_lojas[:5].plot(figsize=(15, 5), kind='bar')



maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()

menor_valor = vendas_lojas['Quantidade Vendida'].min()
pior_loja = vendas_lojas['Quantidade Vendida'].idxmin()

print(f'A loja que MAIS vendeu foi: " {melhor_loja}" Ela vendeu o total de: {maior_valor}')

print(f'A loja que MENOS vendeu foi: " {pior_loja}" Ela vendeu o total de: {menor_valor}')



#Iniciar Aula 14