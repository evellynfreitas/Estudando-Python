import pandas
import plotly.express as px

# importando banco de dados
tabela = pandas.read_csv("cancelamentos.csv")


# tratamento de dados

tabela = tabela.dropna()  # excluindo linhas vazias
tabela = tabela.drop("CustomerID", axis=1)  # excluindo colunas

#print(tabela.info())

# analisando dados

tabela = tabela[tabela["duracao_contrato"] != "Monthly"]

#print(tabela["cancelou"].value_counts())
#print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

#print(tabela.groupby("duracao_contrato").count())
#print(tabela.groupby("duracao_contrato").sum())
#print(tabela.groupby("duracao_contrato").mean())

#tabela = tabela.drop

#print(tabela["duracao_contrato"].value_counts())

#grafico = px.histogram(tabela, x="assinatura",color="cancelou")
#grafico.show()

tabela = tabela[tabela["ligacoes_callcenter"]<5]
tabela = tabela[tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts(normalize=True))

#codigo dia 24:
