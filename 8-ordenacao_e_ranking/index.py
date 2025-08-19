import numpy as np

#odenar o array de forma crescente
arr = np.array([3,1,4,2])
print(arr)
print(np.sort(arr))

#retornar os índices que ordenaria um array
print(np.argsort(arr))

#ordenação multicritério, útil para ordenar por várias chaves:
#primeiro ele ordena por ordem alfabética, depois por ordem crescente, começando por ana com o menor score, para depois com o maior score
names = np.array(['Ana', 'Bob', 'Ana', 'Bob'])
scores = np.array([90, 80, 85, 70])
idx = np.lexsort((scores,names))    #a primeira ordenação vai começar por names, que é o segundo array passado
print(idx)

#valores únicos e contagem
arr2 = np.array([1,2,2,3,3,3,4])
print(np.unique(arr2))              #mostra apenas um dos repetidos 
print(np.bincount(arr2))            #conta as ocorrências de cada número

#ordenar da forma decrescente
print(np.sort(arr)[::-1])