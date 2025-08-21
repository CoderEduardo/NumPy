import numpy as np

#Exercício 1: Operações Básicas

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])
C = np.array([1, 2, 3])
D = np.array([4, 5, 6])

#A @ B (usando o operador @)
resultado1 = A @ B
print(resultado1)

#np.dot(A, B)
resultado2 = np.dot(A, B)
print(resultado2)

#np.matmul(A, B)
resultado3 = np.matmul(A,B)
print(resultado3)

#np.dot(C, D)
resultado4 = np.dot(C, D)
print(resultado4)

#C @ D
resultado5 = C @ D
print(resultado5)

#Exercício 2: Usando einsum

E = np.array([[1, 2], [3, 4]])
F = np.array([[5, 6], [7, 8]])
G = np.array([1, 2])
H = np.array([3, 4])

#Produto interno de G e H
produto_interno = np.einsum('i,i->',G,H)
print(produto_interno)

#Multiplicação matricial de E e F
multiplicacao_matricial = np.einsum('ij, jk->ik',E,F)
print(multiplicacao_matricial)

#Traço da matriz E
traco = np.einsum('ii',E)
print(traco)

#Produto externo de G e H
produto_externo = np.einsum('i,j->ij',G,H)
print(produto_externo)

#Exercício 3: Normas

vetor = np.array([1, -2, 3, -4, 5])
matriz = np.array([[1, 2], [3, 4]])

#Norma L2 do vetor
norma_l2 = np.linalg.norm(vetor, ord=1)
print(norma_l2)

#Norma L1 do vetor
norma_l1 = np.linalg.norm(vetor)
print(norma_l1)

#Norma infinita do vetor
norma_inf = np.linalg.norm(vetor, ord=np.inf)
print(norma_inf)

#Norma Frobenius da matriz
norma_frob = np.linalg.norm(matriz, 'fro')
print(norma_frob)

#Exercício 4: Sistemas Lineares, Resolva o sistema:

"""
2x + 3y - z = 1
x - y + 2z = 8
3x + 2y + z = 9
"""

x = np.array([
    [2,3,1],
    [1,1,2],
    [3,2,1]
    ])

y = np.array([1,8,9])

resultado = np.linalg.solve(x,y)
print(resultado)

#Desafio Extra
#Crie uma função que recebe uma matriz e retorna:

valores = []

def retornar_valores(matriz):
    #Sua determinante
    determinante = np.linalg.det(matriz)
    
    #Sua inversa (se existir)
    if np.linalg.det(matriz) != 0:
         inversa = np.linalg.inv(matriz)
    else:
        inversa = "A matriz não possui inversa"
    #Seu posto (rank)
    posto = np.linalg.matrix_rank(matriz)

    #Sua decomposição QR
    qr = np.linalg.qr(matriz)

    valores =  [determinante, inversa, posto, qr]

    return valores

matriz = np.arange(16).reshape(4,4)
matriz_valores =  retornar_valores(matriz)
print(f"Matriz: \n{matriz}\n Determinante: \n{matriz_valores[0]}, \n Inversa: \n{matriz_valores[1]}, \nSeu posto(rank):\n {matriz_valores[2]} \n Decomposição: \n {matriz_valores[3]}")