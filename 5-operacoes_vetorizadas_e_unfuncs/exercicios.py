import numpy as np

#Crie arr = np.array([1, 4, 9, 16]) e calcule sqrt, exp e log.
arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))

#Some 10 a todos os elementos de um array np.arange(5).
arr2 = np.arange(5)
print(arr2 + 10)

#Crie uma matriz 2x3 e some com [10,20,30] (broadcasting).
mat = np.full((2,3),1)
print(mat + [10,20,30])

#Use broadcasting para somar [[1],[2],[3]] com [10,20,30].
linha = np.array([[1],[2],[3]])
coluna = np.array([10,20,30])
print(linha)
print(coluna)
print(linha + coluna)


#Calcule seno, cosseno e valor absoluto de um array com números negativos.
arr3 = np.array([-1,-27,-451,-9])
print(np.sin(arr3))
print(np.cos(arr3))
print(np.abs(arr3))