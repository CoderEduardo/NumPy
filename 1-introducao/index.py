import numpy as np 

#array 1
arr1 = np.array([1,2,3,4,5])
print(f"Array 1: {arr1}")

#array 2 (matriz)
arr2 = np.array([[1,2,3],[4,5,6]])
print(f"Array 2 (Matriz): {arr2}")

#array com valores de 0 a 9
arr3 = np.arange(10)
print(f"Array com np.arange: {arr3}")

#array com números igualmente espaçados, esse array pega o primeiro número passado e vai até o segundo número, com o número de divisões indicadas
#pelo terceiro parâmetro
arr4 = np.linspace(0,1,5)
print(f"Array com np.linspace: {arr4}")

#array especiais 

zeros = np.zeros((2,3)) #matriz com duas linhas e três colunas compostas de 0
print(zeros)

ones = np.ones((3,2))
print(ones) #matriz com três linhas e duas colunas compostas de 1

"""
O que é uma matriz identidade?
É uma matriz onde todos os elementos da diagonal principal são igual a 1, e todos os outros elementos são iguais a 0
No caso desse exemplo de baixo, ela seria assim:
[1 0 0
 0 1 0
 0 0 1]

"""

eye = np.eye(3)
print(eye) #matriz identidade de 3x3