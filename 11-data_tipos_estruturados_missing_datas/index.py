import numpy as np

#datetime64 representa datas e timestamps com alta precisão:

#criando array de datas
datas = np.array(['2023-01-01', '2023-01-02', '2023-01-03'],dtype='datetime64[D]')
print(f"Datas: {datas}")

#operações com datas
data_inicial = np.datetime64('2023-01-01')
dias = np.arange(5)
print(dias)
#ele vai somar a quantidade de elementos aos dias
datas_futuras = data_inicial + dias
print(f"Datas futuras: {datas_futuras}")

#timedelta64 representa diferenças entre datas:
data1 = np.datetime64('2023-01-10')
data2 = np.datetime64('2023-01-05')
diferenca = data1 - data2
print(f"Diferença em dias: {diferenca}")

#criando intervalo de tempo
uma_semana = np.timedelta64(1,'W') #1 semana
duas_horas = np.timedelta64(2,'h') #duas horas

# Structured Arrays (Arrays Estruturados)
#Permitem armazenar dados heterogêneos com campos nomeados:

#definindo um tipo estruturado
tipo_pessoa = np.dtype([
    ('nome','U20'),     #string unicode com 20 caracteres
    ('idade','i4'),     #inteiro de 32 bites
    ('altura','f8'),    #float de 64 bits
    ('ativo','?')       #booleano
])

#criando array estruturado
pessoas = np.array([
    ('Ana',25,1.65,True),
    ('Carlos',30,1.80,False),
    ('Maria',22,1.70,True)
], dtype=tipo_pessoa)

#Acessando campos
print(f"Nomes: ", pessoas['nome'])
print(f"Idade média", np.mean(pessoas['idade']))

#missing datas

#array com valores missing
dados = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])
print(f"Dados com NaN: {dados}")

#detectando valores NaN
mask_nan = np.isnan(dados)
print(f'Posições com NaN: {mask_nan}')
print(f'Valores válidos: {dados[~mask_nan]}')

#cuidado com operações 
print(f"Soma com NaN: {np.sum(dados)}") #resulta em NaN
print(f"Ignorando NaN: {np.nansum(dados)}") #ignora nan

#cuidados com dtype 
#NaN força conversão para float
arry_int = np.array([1,2,3])
print(arry_int)
arry_int[0] = np.nan #isso converte todo array para float 
print(f"Array convertido: {arry_int}")
