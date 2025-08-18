import numpy as np

#Crie um array de 10 elementos com valores de 5 a 14.
arr1 = np.arange(5,15)
print(arr1)

#Crie uma matriz 4x4 cheia de 7.
arr2 = np.full((4,4),7)
print(arr2)

#Crie uma matriz identidade 5x5
arr3 = np.eye(5)
print(arr3)

#Gere um array com 6 valores igualmente espaçados entre 10 e 20
arr4 = np.linspace(10,20,6)
print(arr4)