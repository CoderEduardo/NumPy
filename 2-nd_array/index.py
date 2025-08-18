import numpy as np

#diferença entre lista e array

lista = [1,2,3,4,5]
array = np.array([1,2,3,4,5])

#operação de multiplicação
print(lista * 2)    #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5] repete a lista
print(array * 2)    #[ 2  4  6  8 10] multiplica cada elemento
#arrays permitem operações vetorizadas, se fossemos fazer uma lista multiplicar cada elemento, teriamos que criar um for.

#Tipos de dados

arr = np.array([1,2,3])
print(arr.dtype)    #mostra o tipo de dados do array, no caso int64 por padrão de números

arr_float = np.array([1,2,3], dtype=float) #dtype muda o tipo do dado
print(arr_float.dtype)

##Principais propriedades do ndarray

array_teste = np.array([[1,2,3],[4,5,6]])

print(array_teste.shape)    #retorna o número de linhas e colunas: (2, 3)
print(array_teste.size)     #retorna o número total de elementos: 6
print(array_teste.ndim)     #retorna o número de dimensões: 2
print(array_teste.itemsize) #retorna o tamanho em bytes de cada elemento
print(array_teste.nbytes)   #retorna o total de memória usada (size * itemsize)