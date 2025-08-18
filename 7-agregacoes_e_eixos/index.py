import numpy as np

#numpy oferece funções que operam em todos elementos do array

arr = np.arange(1,6)

print(arr.sum())    #soma todos elementos do array
print(arr.mean())   #faz a média de todos elementos do array
print(arr.std())    #desvio padrão
print(arr.min())    #retorna o menor valor
print(arr.max())    #retorna o maior valor

#Para arrays multidimensionais, podemos especificar eixo:
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat)
print(mat.sum(axis=0))  #somamos todas as colunas
print(mat.sum(axis=1))  #somaos todas as linhas

#funções cumulativas
arr2 = np.array([1,2,3,4])
print(np.cumsum(arr2))      #soma de forma cumulativa, 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10
print(np.cumprod(arr2))     #multiplica de forma cumulativa, 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24 

#indice de valores externos
arr3 = np.array([5,1,9,3])
print(arr3.argmax())          #índice do maior valor
print(arr3.argmin())          #índice do menor valor

#consiguimos fazer também com matrizes
mat2 = np.array([[1,5,2], [7,3,9]])
print(mat2)
print(mat2.argmax(axis=0))   #maior por coluna
print(mat2.argmax(axis=1))   #maior por linha
