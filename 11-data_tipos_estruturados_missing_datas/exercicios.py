import numpy as np

# Crie um array com as datas de todos os dias de janeiro de 2023

janeiro = np.arange('2023-01-01','2023-02-01',dtype='datetime64[D]') #para criar uma data de um começo ao outro usamos o arange
print(janeiro)

# Calcule:
# 1. Quantos dias de semana (segunda a sexta) existem no mes

dias_semana = np.is_busday(janeiro)  #np.busday_count conta os dias da semana de segunda a sexta
dias_uteis = np.sum(dias_semana)
print(f"Dias da semana: {dias_uteis}")

# 2. Quais são os dias que caem no fim de semana
finais_semana = janeiro[~dias_semana]
print(f"Finais de semana{finais_semana}")

# 3. Adicione 2 semanas a cada 
duas_semanas = np.timedelta64(2, 'W')
datas_futuras = dias_semana + duas_semanas
print("3. Datas + 2 semanas:", datas_futuras)

#Array estruturados

# Crie um array estruturado para armazenar informações de produtos:
# - nome (string de 30 caracteres)
# - preço (float)
# - quantidade_estoque (inteiro)
# - disponivel (booleano)

produtos = np.dtype([
    ('nome','U20'),
    ('preco','f'),
    ('quantidade_estoque','i'),
    ('disponivel','?')
])

# Adicione 5 produtos diferentes
produto = np.array([
    ('Calculadora',20.5,90,True),
    ('Óculos',100,17,True),
    ('Chocolate',8,0,False),
    ('Celular',1000.50,5,True),
    ('Tênis',250,25,True),
], dtype=produtos)
# Calcule:
# 1. O preço médio dos produtos disponíveis
media = np.nanmean(produto['preco']) 
print(media)

# 2. O valor total do estoque (preço × quantidade)
valor_total_estoque = np.sum(produto['preco']* produto['quantidade_estoque'])
print(valor_total_estoque)

# 3. Liste os nomes dos produtos com menos de 10 unidades em estoque
pouco_estoque = produtos['nome'][produtos['quantidade_estoque'] < 10]
print("3. Produtos com menos de 10 unidades:", pouco_estoque)