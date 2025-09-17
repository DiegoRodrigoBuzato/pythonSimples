muvie_name = "Top Gun"
#string[inicio:fim] - índice começa na posição 0 | índice final - 1 

#1 - buscar toda string a partir da primeira poição 
print(muvie_name[0:])

# - Buscar toda string até a ultima posição 
print(muvie_name[:7])

# 3 - Buscar toda string da terceira até a última posição
print(muvie_name[2:])

"""
#string[inicio:fim:passo] - índice começa na posição 0 | índice final - 1 
passo determina o incremento. Por padrão esse número é o 1.
"""
# 4 - Buscar toda string de 2 em 2 caracteres 
print(muvie_name[::2])

# 5 - Buscar toda string nos indices impares 
print(muvie_name[1::2])

# 6 - Inverter uma string de trás pra frente 
print(muvie_name[::-1]) 