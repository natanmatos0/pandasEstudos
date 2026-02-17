# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df
# %%
df.shape
# %%
df.info()
# %%
df.dtypes
# %%
renamed_columns = {
    "IdTransacao": "id",
    "DescSistemaOrigem": "SistemaOrigem"}
df = df.rename(columns=renamed_columns)
"""
passa um dicionario como parametro; 
chave=nome atual, valor=nome novo; 
a função devolve um df novo, não faz alterações no que ja existe
para que as alterações seja efetivas ele precisa ser instanciado novamente
"""
# %%
df = df.rename(columns=renamed_columns, inplace=True)
"""
diferente do metodo anterior, com o parametro "inplace" a alteração acontece de
forma direta, sem precisar de uma nova instancia
"""

# %%
df["id"]
"""
df["x"]: retorna uma serie com as informações daquela coluna
"""
# %%
colunas_mostradas = ["id", "QtdePontos"]
df[colunas_mostradas]
"""
ao passar uma lista como parametro de busca 
o retorno é um df com a(s) coluna(s) selecionada(s)
a ordem das colunas importa, pq é um df "novo"
"""

# %%
colunas_mostradas = ["QtdePontos","id"]
print(df[colunas_mostradas].head(5))


# %%
colunas = df.columns.tolist()
colunas.sort()
colunas
"""
isso poe as colunas em ordem alfabetica
"""


df = df[colunas]
df

# %%

