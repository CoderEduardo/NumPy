import numpy as np

#Crie um array de 10 elementos e pegue os elementos do índice 3 ao 7.
arr1 = np.arange(10)
print(arr1[3:8])

#Crie um array de 10 elementos e selecione os elementos de 2 em 2.
arr2 = np.arange(10)
print(arr2[::2])

#Crie uma matriz 3x3 e selecione a segunda linha e depois a terceira coluna.
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)
print(arr3[1,:])
print(arr3[:,2])

#Crie uma matriz 4x4 e pegue as linhas 1 e 2 e colunas 2 e 3.
arr4 = np.array([[1,2,3,5],[6,7,8,9],[10,11,12,13],[14,15,16,17]])
print(arr4)
print(arr4[1:3, 2:4])

#Mostre que alterar uma fatia altera o array original.
arr5 = np.array([1,2,3,4,5])
print(arr5)
alterar = arr5[1:4]
alterar[1] = 200
print(arr5)

arr6 = np.arange(10)
fatia = arr6[3:7].copy()
fatia[2] = 999
print(arr6)