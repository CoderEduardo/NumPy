import numpy as np

#Crie arr = [4,1,3,2] e ordene com np.sort
arr = np.array([4,1,3,2])
print(np.sort(arr))

#Encontre os índices ordenados do array acima com np.argsort.
print(np.argsort(arr))

#Crie arr = [1,2,2,3,3,3] e encontre os valores únicos e a contagem de cada valor com np.unique e np.bincount.

#Crie dois arrays names = ['Ana','Bob','Ana','Bob'] e scores = [90,80,85,70] e use np.lexsort para ordenar por nome e depois por score.