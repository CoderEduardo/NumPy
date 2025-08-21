import numpy as np
from numpy.random import default_rng

#criando o gerador de sementes
rng = default_rng(42)  # 42 é só um exemplo de semente (int)

# Dois generators com a mesma semente → mesma sequência
rng1 = default_rng(123)
rng2 = default_rng(123)
print(rng1.random(3), rng2.random(3))  # arrays idênticos

u = rng.random(5)
u2d = rng.random((3,2))
print(u.dtype)              #float por padrão

#inteiros aleatórios
ints = rng.integers(0,10,size=5)        #gera um array com cinco elementos, com números de 0 até 9
print(ints)
print(ints.dtype)                       #por padrão é int64

ints32 = rng.integers(0,10,size=5,dtype=np.int32)   #mudando o padrão para int32
print(ints32.dtype)

matriz_int = rng.integers(1,7,size=(2,3))
print(matriz_int)

#amostragem de elementos
itens = np.array(['A','B','C','D'])

#com reposição (elementos se repetem)
amostra = rng.choice(itens, size = 3)
print(amostra)

#sem reposição  (elementos não se repetem)
amostra_sr = rng.choice(itens, size=3, replace=False)
print(amostra_sr)

#com pesos (probabilidades)
pesos = np.array([0.7, 0.2, 0.1])
amostra_p = rng.choice(['A','B','C  '], size=10_000, p=pesos)
print(amostra_p)

#permutação vs embaralhamento
perm_indices = rng.permutation(10)
perm_array = rng.permutation(np.arange(6))
print(perm_indices)
print(perm_array)

arr = np.arange(10)
rng.shuffle(arr)        #embaralha o array
print(arr)

mat = np.arange(12).reshape(4,3)
rng.shuffle(mat, axis=0)            #embaralha as linha
print(mat)

#para embaralhar colunas

cols = rng.permutation(mat.shape[1])
mat_cols = mat[:,cols]                  #cria uma cópia com colunas 

#Distribuições mais usadas e parâmetros

#Uniforme contínua [low, high]
uni = rng.uniform(low=0.0, high=1.0, size=1000)

#Normal (Gaussiana): loc = média, scale = desvio-padrão
norm = rng.normal(loc=0.0, scale=1.0, size=1000)

# Binomial: nº de sucessos em n tentativas, prob p
binom = rng.binomial(n=10, p=0.3, size=1000)

# Poisson: contagens por intervalo com taxa λ
pois = rng.poisson(lam=2.0, size=1000)

# Exponencial: tempo entre eventos (scale = 1/λ)
expo = rng.exponential(scale=1.0, size=1000)

# Beta: contínua em [0,1], modela proporções (a, b > 0)
beta = rng.beta(a=2.0, b=5.0, size=1000)

# Lognormal: exp(N(loc, sigma)) — dados positivos com cauda longa
logn = rng.lognormal(mean=0.0, sigma=1.0, size=1000)

#Depois de gerar amostras grandes, confira estatísticas:
arr.mean(), arr.std(), arr.min(), arr.max()
