# *args  - utilizamos ele quando não temos certeza de quantos argumentos queremos na função
# Os argumentos são passados como uma tupla para a função

#**kwargs - Além dos valores podemos passar também as respectiovas chaves para cada argumento
# Os argumentos são passados como um dicionário para a função

# Soma de números args
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f'Soma total: {sum_total}')

sum(7,9,10,11)

# Apresentação de curso kwargs
def presentation(**data):
    for key, value in data.items():
        print(f'{key}: {value}')
print("Lista de cursos:")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão computacional", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data science", level="Intermediário")

