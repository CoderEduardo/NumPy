#Aprendendo a mudar a forma dos arrays e trabalhar com manipulações avançadas de eixos, mantendo a eficiência do NumPy.
import numpy as np

#mudar a forma de um array sem alterar dados
arr = np.arange(12)
mat = arr.reshape(3,4)
print(arr)
print(mat)

#transforma os arrays em 1d
mat2 = np.array([[1,2,3],[4,5,6]])
print(mat2)
print(mat2.ravel())             #view, altera o original se você modificar
print(mat2.flatten())           #cópia, original não é alterado
print(mat2)

#invertendo eixos de um array
mat3 = np.arange(6).reshape(2,3)
print(mat3)
print(mat3.T)     #inverte para 3x2  

#adiciona um novo eixo
arr2 = np.array([1,2,3])
print(np.expand_dims(arr2,axis = 0)) #1x3
print(np.expand_dims(arr2,axis=1))   #3x1   

#remove eixos de dimensão 1
mat3 = np.array([[[1,2,3]]])
print(mat3)          # (1,1,3)
print(np.squeeze(mat3))  # (3,)

#stack e concatanete
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.stack([a,b]))          #junta os dois [[1,2,3],[4,5,6]]
print(np.concatenate([a,b]))    #concatena os dois [1,2,3,4,5,6]