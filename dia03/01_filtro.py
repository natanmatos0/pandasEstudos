# %%
import pandas as pd

# %%
"""
codigo nescesssario para fazer um filtro 
para valores maior do que 500 com python puro
"""

pontos = [20, 434, 4034, 3120, 3234, 3, 32, 112]
filtro = []

for i in pontos:
    filtro.append(i>500)

resultado = []

for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
resultado

# %%
"""
codigo nescesssario para fazer um filtro 
para valores maior do que 500 usando pandas
"""

df2 = pd.DataFrame(
    {
        "pontos":[20, 434, 4034, 3120, 3234, 3, 32, 112]
    }
)
filtro = df2["pontos"] >= 500
df2[filtro]

# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     }
)

# %%
"""
codigo nescessario para mostrar quem tem a idade maior 
que 18 anos
"""

filtro = brinquedo["idade"] >= 18 

"""
retorna uma serie de valores booleanos 
com a mesma quantidade de linhas do df
"""

brinquedo[filtro] # mostra somente os valores que sao True no filtro

# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%
#valores maiores que 50
filtro = df["QtdePontos"] >= 50
df_filtrado = df[filtro]

# %%
#valores menores que 100
filtro = df_filtrado["QtdePontos"] <= 100
df_filtrado[filtro]

# %%
"""
*, &: and

tabela verdade do (and)

True * False = False
False * True = False
False * False = False
True * True = True

"""
#valores entre 50 e 99
filtro = (df["QtdePontos"] >= 50) * (df["QtdePontos"] < 100)
df[filtro]
# %%
"""
+, |: or

tabela verdade do (or)

True + True = True
False + True = True
True + False = True
False + False = False

"""
#valores que sao 1 ou 100
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %%
#pontos entre 0 e 50 ou do ano de 2025 pra frente
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"]<=50) | (df["DtCriacao"]>="2025-01-01")
df[filtro]
# %%
