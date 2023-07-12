import pandas as pd
import matplotlib.pyplot as plt
url="dados_imoveis.csv"

dados = pd.read_csv(url)
# print(dados.head())
# print(dados.sample(10))
# print(type(dados))
# print("\n\n")
# print("pegar todos os bairros")
# print(dados["Bairro"])
#
# print("\n\n")
# print("pegar bairro especifico")
# print(dados["Bairro"][6522])
# print("\n\n")
# print("Pegar as infos do Dados")
# print(dados.info()) #object é string nao  e int64 numero
# print("\n\n")
# #fazer media da metragem de todos os endereços
# print(dados.Metragem)
# print(dados.Metragem.mean())
# # print(dados["Metragem"]mean())  mesma coisa acima
# print("\n\n")
#
# # Verificar se há um endereço na Vila Mariana. Soma-se os valores
#
# print(sum((dados["Bairro"] == "Vila Mariana")))
# print("\n\n")
#
# #Armazenar o número de imoveis que tem na Vila mariana
# tem_imoveis_vila = (dados["Bairro"] == "Vila Mariana")
# imoveis_vila = dados[tem_imoveis_vila] # guarda todos os imoveis
#
# #tirar a media da metragem da vila mariana
# print(imoveis_vila["Metragem"].mean())
# print("\n\n")
# #Pegar quantidade de imoveis que possui em cada bairro
# print(dados["Bairro"].value_counts())
#
# #Criar um gráfico
# n_imoveis_bairro = dados["Bairro"].value_counts()
# n_imoveis_bairro.head(10).plot.bar()
# plt.show()
# # n_imoveis_bairro.plot.hist()
# # plt.show()

#Desafio

#1) Realizar a média da metragem para cada um dos bairros.

# media_metragem_bairro = dados.groupby('Bairro')['Metragem'].mean()
# print(media_metragem_bairro)

# Segundo Método
# bairros = dados['Bairro'].unique()
#
# for bairro in bairros:
#     media = dados[dados['Bairro'] == bairro]['Metragem'].mean()
#     print(f'Média da metragem para o bairro {bairro}: {media}')

# 2) Duas formas de selecionar os dados por bairro

# dados_bairro = dados.loc[dados['Bairro'] == 'Vila Mariana']
# print(dados_bairro)
#
# dados_bairro = dados.query("Bairro == 'Morumbi'")
# print(dados_bairro)
#
# bairros_selecionados = ['Vila Mariana', 'Morumbi', 'Jardins']
# dados_bairro = dados[dados['Bairro'].isin(bairros_selecionados)]
# print(dados_bairro)

#3) Explorar alguns gráficos na documentação e aplicar nas demais colunas do DF, assim como tentar colocar alguma conclusão.

# Gráfico de Barras:
# grafico = dados['Vagas'].value_counts().plot(kind='bar')
# grafico.set_title('Contagem de Vagas')
# plt.show()

# Gráfico de Pizza:

# dados['Bairro'].value_counts().plot(kind='pie')
# plt.show()


# 4) Pegar outras estatísticas dos dados (como média, mediana, mim, max)

# print(dados['Metragem'].mean())  # Calcula a média dos valores de uma coluna numérica
# print(dados['Metragem'].sum())  # Calcula a soma dos valores de uma coluna numérica
# print(dados['Metragem'].max())  # Retorna o valor máximo de uma coluna numérica
# print(dados['Metragem'].min())  # Retorna o valor mínimo de uma coluna numérica
# print(dados['Metragem'].median()) # Retorna a mediana de uma coluna numérica

#5  Descobrir quais são os bairros que não tem nome de rua

# print(dados.head())
# bairros_sem_rua = dados[dados['Rua'].isnull()]['Bairro'].unique()
# print(bairros_sem_rua)
# bairros_sem_rua = dados[dados['Rua'].isna()]['Bairro'].unique()
# print(bairros_sem_rua)