import numpy as np

arr = np.array([10,20,30,40,50])
mascara = arr > 25                  #criando o array booleano
print(mascara)
print(arr[mascara])                 #aplicando a máscara

print(arr[(arr > 15) & (arr < 45)]) #você pode combinar condições

#Fancy indexing (índices específicos)
indices = [0,2,4]
print(arr[indices]) #retorna apenas o índices que você pediu

#funciona também em matrizes 2d
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat)
#o primeiro índice especifica índices de linhas, e o segundo de colunas
print(mat[[0,2], [1,2]])  # pega elementos (0,1) e (2,2) → [2 9]

