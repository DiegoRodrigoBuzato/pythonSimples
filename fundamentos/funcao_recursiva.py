# 1 -> 1*1   1
# 2 -> 2 * 1    2*factorial(1) = 2 
# 3 -> 3 * 2 * 1   3*factorial(2) = 6

# Fatorial de um número

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return (num * factorial(num - 1))
number = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {number} é {factorial(number)}")

# Soma total de um número 
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))
number = int(input("Digite um número para calcular a soma total: "))
print(f"A soma total de {number} é {total_sum(number)}")    