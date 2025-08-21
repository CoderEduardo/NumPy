import numpy as np

#para multiplicar uma matriz, o número de COLUNAS de A deve ser o mesmo número de LINHAS de B
A = np.arange(6).reshape(2,3)
B = np.arange(9).reshape(3,3)
print((A @ B).shape)            #(2,3), ela vai passar a ter o mesmo número de linhas de colunas da Matriz A

a = np.array([1,2,3])
b = np.array([10,20,30])    

print(a * b)    #elemento por elemento
print(a @ b)    #produto interno, (10 * 1 + 20 * 2 + 30 * 3) = 140

#o numpy reescreve a forma da matriz para ser possivel a multiplicação de matrizes
C = np.ones((2,3))
D = np.array([1,2,3])
print(C @ D)  #matriz-vetor (2,)

#O einsum é uma função poderosa que permite expressar operações tensoriais usando a notação de Einstein.

E = np.array([[1, 2], [3, 4]])
F = np.array([[5, 6], [7, 8]])

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

e = np.array([1,2,3])
f = np.array([10,20,30])

#produto interno
print(f"Produto interno: \n {np.einsum('i,i->',v1,v2)}")

#multiplicação matricial
print(f"Multiplicação matricial: \n {np.einsum('ij,jk->ik',E,F)}")

#traço de uma matriz
print(f"Traço de uma matriz: \n{np.einsum('ii',E)}")

#produto externo
produto_externo =np.einsum('i,j->ij',v1,v2)
print(f"Produto externo: \n {produto_externo}")

#linalg - Álgebra linear
v = np.array([3,4])

#normal L2 (Euclidiana), mede o tamanho do vetor no espaço euclediano 
normal_l2 = np.linalg.norm(v)
print(normal_l2)

#normal L1, faz a soma dos valores absolutos dos componentes do vetor
normal_l1 = np.linalg.norm(v, ord=1)
print(normal_l1)

#normal infinita, pega o maior valor absoluto
norma_inf = np.linalg.norm(v, ord=np.inf)
print(norma_inf)

"""Para etender desse código, é preciso enteder sobre Álgebra linear, no caso desse exemplo, temos o seguinte sistema, o G composto por x e y, nos 
seus índices de linhas e colunas, e os seus resultados compostos por H:

Sistema: 

        2x + y = 5
        x + 3y = 6

"""

#solução de sistemas lineares

G = np.array([[2,1],[1,3]]) #variáveis
H = np.array([5,6])         #resultados
x = np.linalg.solve(G,H)    #resolução
print(x)

