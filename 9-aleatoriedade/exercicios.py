import numpy as np
from numpy.random import default_rng

#Exercício 1 — Básico de Generator
#Crie rng = np.random.default_rng(42).
rng = np.random.default_rng(42)

# 5 inteiros entre 0 e 9.
inteiros = rng.integers(0,10,size=5)
print(inteiros)

#Gere uma matriz 3×2 de uniformes em [0,1).
matriz = rng.random(size=(3,2))
print(matriz)

#Imprima shape e dtype de ambos os resultados.
print(inteiros.shape)
print(inteiros.dtype)
print(matriz.shape)
print(matriz.dtype)

#Exercício 2 — Amostragem com e sem reposição (e pesos)

#Com itens = np.array(['A','B','C','D']), gere:
itens  = np.array(['A','B','C','D'])

#a) 3 amostras com reposição
amostra1_r = rng.choice(itens, size=4)
amostra2_r = rng.choice(itens, size=4)
amostra3_r = rng.choice(itens, size=4)

#b) 3 amostras sem reposição
amostra1_sr = rng.choice(itens, size=4, replace=False)
amostra2_sr = rng.choice(itens, size=4, replace=False)
amostra3_sr = rng.choice(itens, size=4, replace=False)

#Use p = [0.6, 0.2, 0.1, 0.1] e gere 10.000 amostras com reposição.
pesos = np.array([0.6, 0.2, 0.1, 0.1])
amostra_p = rng.choice(itens, size=10_000, p=pesos)
print(amostra_p)

#Mostre as frequências relativas usando np.unique(..., return_counts=True).
relativo = np.unique(amostra_p, return_counts=True)
frequencia_relativa = (relativo[1] / len(amostra_p)) * 100
print(relativo)
print(f"Frequência relativa em porcentagem: {frequencia_relativa}")

#Exercício 3 — Permutação vs Embaralhamento

#Crie arr = np.arange(10) e:
arr = np.arange(10)

#a) gere uma cópia permutada com rng.permutation(arr)
copia_permutada = rng.permutation(arr)
print(copia_permutada)

#b) embaralhe no lugar com rng.shuffle(arr)
rng.shuffle(arr)

#Crie mat = np.arange(12).reshape(4,3) e:
mat = np.arange(12).reshape(4,3)
print(mat)

#a) embaralhe as linhas com shuffle(axis=0)
rng.shuffle(mat, axis=0)

#b) reordene as colunas usando cols = rng.permutation(mat.shape[1]) e mat[:, cols].
cols = rng.permutation(mat.shape[1]) 
print(cols)

mat_cols_permutadas = (mat[:, cols])
print(mat_cols_permutadas)

#Exercício 4 — Distribuições + sanity check

#Gere x = rng.normal(loc=5, scale=2, size=100_000) e calcule x.mean() e x.std().
x = rng.normal(loc=5, scale=2, size=100_000)
print(x)
print(x.mean()) #média
print(x.std())  #desvio padrão

#Gere y = rng.poisson(lam=3, size=50_000) e calcule y.mean() e y.var().
y = rng.poisson(lam=3, size=50_000)
print(y)
print(y.mean())
print(y.var())  #variância

#Comente se os resultados estão próximos dos parâmetros.
#Sim, a média e variânca e de poisson são praticamente iguais

