#%%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

series_idades = pd.Series(idades)  


#%%

idades[0]
series_idades[0]

# %%

series_idades[len(series_idades)-1]
# %%
series_idades = series_idades.sort_values()
series_idades

#%%
series_idades.iloc[0]
# %%
series_idades.iloc[[0,1,2,3]] # ignora o indice e so busca as linhas


#%%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]



indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades, index=indexs) 
series_idades