import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

tabela = pd.read_csv('clientes.csv')
codificador = LabelEncoder()
tabela['profissao'] = codificador.fit_transform(tabela['profissao'])
tabela['mix_credito'] = codificador.fit_transform(tabela['mix_credito'])
tabela['comportamento_pagamento'] = codificador.fit_transform(tabela['comportamento_pagamento'])

y = tabela['score_credito']
x = tabela.drop(['score_credito', 'id_cliente'], axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste.to_numpy())

print(accuracy_score(y_teste, previsao_arvoredecisao))
print(accuracy_score(y_teste, previsao_knn))

novos_clientes = pd.read_csv('novos_clientes.csv')
novos_clientes['profissao'] = codificador.fit_transform(novos_clientes['profissao'])
novos_clientes['mix_credito'] = codificador.fit_transform(novos_clientes['mix_credito'])
novos_clientes['comportamento_pagamento'] = codificador.fit_transform(novos_clientes['comportamento_pagamento'])

previsao = modelo_arvoredecisao.predict(novos_clientes)
print(previsao)
