import numpy as np

#Crie um array de 10 elementos e selecione todos maiores que 5.
arr1 = np.arange(10)
maior_cinco = arr1 > 5
print(arr1[maior_cinco])

#Crie um array de 0 a 9 e selecione todos pares usando máscara booleana.
arr2 = np.arange(10)
pares = arr2 % 2 == 0
print(arr2[pares])

#Crie um array de 5 elementos e use lista de índices [0,2,4] para selecionar elementos específicos.
arr3 = np.arange(5)
indices = [0,2,4]
print(arr3[indices])

#Crie uma matriz 3x3 e use fancy indexing para pegar os elementos (0,0), (1,1) e (2,2).
identidade = np.eye(3)
print(identidade)
print(identidade[[0,1,2],[0,1,2]])