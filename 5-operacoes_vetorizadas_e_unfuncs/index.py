import numpy as np

#Operações Aritméticas Elemento a Elemento
arr1 = np.array([1,2,3,4])

#isso se chama vetorização
print(f"Array: {arr1}")
print(arr1 + 2)             #soma em cada item
print(arr1 - 2)             #subtrai em cada item
print(arr1 * 2)             #multiplica em cada item
print(arr1 / 2)             #dividi cada item
print(arr1 ** 2)            #potencia em cada item

#UFuncs (Funções Universais)

arr2 = np.array([1,4,9,16])

print(np.sqrt(arr2))     #raiz quadrada
print(np.exp(arr2))      #exponencial
print(np.log(arr2))      #logaritmo natural
print(np.sin(arr2))      #seno
print(np.cos(arr2))      #cosseno
print(np.abs([-1,-2,3])) #valor absoluto

#Broadcasting é quando o NumPy “estica” automaticamente arrays de formas diferentes para que possam ser usados em operações.

#soma com escalar
arr3 = np.array([1,2,3])
print(arr3+10)

#matriz + vetor (linhas), soma de matrizes
mat = np.array([[1,2,3],[4,5,6]])
print(mat + np.array([10,20,30]))

#matriz + vetor (coluna)
col = np.array([[1,2]]).reshape(2,1)  # vetor coluna (2x1)
print(col)
lin = np.array([10,20,30])            # vetor linha
print(lin)
print(col + lin)

