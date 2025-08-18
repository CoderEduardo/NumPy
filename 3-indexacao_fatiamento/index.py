import numpy as np

#indexação básica
arr = np.array([10,20,30,40,50])
print(arr[0])      #primeiro elemeto
print(arr[-1])     #último elemento
print(arr[1:4])    #entre o primeiro e terceiro elemento

#fatiameto avançado
arr2 = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr2[::2])    #pega elemetos de 2 em 2
print(arr2[1:7:2])  #do índice 1 até o 6, passo 2. O primeiro parâmetro é onde começa, o segundo é até onde vai, e o terceiro é o passo

#indexação com array 2d 
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
print(matriz[0,0])     #linha 0, coluna 0
print(matriz[1,:])     #toda linha 1
print(matriz[:,2])     #toda coluna 2 
print(matriz[0:2,1:3]) #fatia linha 0 - 1, colunas 1 - 2

#cópia e view 
#uma view faz alterações no array original
arr3 = np.arange(5)
print(arr3)
sub = arr3[1:4]
sub[0] = 99
print(arr3)

#para criar uma cópia independente usamos: 
sub_copy = arr[1:4].copy()
