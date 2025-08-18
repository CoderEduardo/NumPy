import numpy as np

#Crie um array de 0 a 11 e transforme em matriz 3x4.
arr = np.arange(12)
novo = arr.reshape(3,4)
print(novo)

#Transforme essa matriz em 1D usando ravel e depois flatten.
print(novo.ravel())
print(novo.flatten())

#Crie uma matriz 2x3 e obtenha sua transposta.
arr2 = np.arange(6).reshape(2,3)
print(arr2)
print(arr2.T)

#Use expand_dims para transformar [1,2,3] em 3x1.
arr3 = np.array([1,2,3])
print(np.expand_dims(arr3,axis=1))

#Concatene [1,2,3] e [4,5,6] em um único array.
arr4 = np.array([1,2,3])
arr5 = np.array([4,5,6])
print(np.concatenate([arr4,arr5]))