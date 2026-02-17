#%%
import pandas as pd
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


series_idades = pd.Series(idades)
series_nomes = pd.Series(indexs)


#%%
# O conjunto de series é um dataframe
df = pd.DataFrame()
df["nomes"] = series_nomes


df
# %%
df["idades"] = series_idades
df.iloc[0]               
# %%
