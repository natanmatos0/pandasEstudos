#%%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")


# %%
df_clientes.head(n=1) #pega os n primeiros

#%%
df_clientes.tail(n=5) #pega os n ultimos

#%%
df_clientes.sample(10) #pega n valores de forma aleatoria

#%%
df_clientes.shape #mostra a quantidade de linhas e colunas em forma de tupla

#%%
df_clientes.columns #mostra o nome das colunas em formatod de lista


#%%
df_clientes.index #mostra o indice das linhas do dataframe(igual as listas)

#%%
df_clientes.info(verbose=True) #mostra a quantidade de linhas, o nome das colunas, a quantidade de valores não nulos por culuna, os tipos de cada coluna


# %%
df_clientes.dtypes #mostra o tipo de cada coluna do dataframe em forma de serie


#