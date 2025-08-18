import  numpy as np

#Crie um array de 1 a 10 e calcule soma, média, desvio padrão, mínimo e máximo.
arr = np.arange(10)
print(arr)
print(arr.sum())
print(arr.mean())
print(arr.std())
print(arr.min())
print(arr.max())

#Crie uma matriz 3x3 e calcule a soma por linha e por coluna.
mat = np.arange(9).reshape(3,3)
print(mat)
print(mat.sum(axis=0)) #coluna
print(mat.sum(axis=1)) #linha 

#Crie um array [2,5,1,3] e calcule cumsum e cumprod.
arr2 = np.array([2,5,1,3])
print(arr2)
print(arr2.cumsum())
print(arr2.cumprod())

#Para a matriz [[1,5,2],[7,3,9]], encontre os índices do maior e menor valor por linha e por coluna.
mat2 = np.array([[1,5,2],[7,3,9]])
print(mat2)
print(mat2.argmax(axis=0))  #coluna
print(mat2.argmin(axis=0))  #coluna
print(mat2.argmax(axis=1))  #linha
print(mat2.argmin(axis=1))  #linha