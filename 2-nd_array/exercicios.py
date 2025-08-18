import numpy as np

#Crie um array 1D de 12 elementos e descubra quantas dimensões ele tem.
arr1 = np.arange(12)
print(arr1.ndim)

#Crie uma matriz 3x4 e mostre shape, size e ndim.
arr2 = np.full((3,4),1)
print(arr2)
print(arr2.shape)
print(arr2.size)
print(arr2.ndim)

#Crie um array de 5 elementos float e mostre dtype e itemsize.
arr3 = np.arange(5,dtype=float)
print(arr3)
print(arr3.dtype)
print(arr3.itemsize)

#Crie uma matriz 2x3 de inteiros e calcule nbytes.
arr4 = np.full((2,3),1)
print(arr4)
print(arr4.nbytes) 
