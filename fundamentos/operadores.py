num1 = int(input("Digite o primeiro número:\n "))
num2 = int(input("Digite o segundo número:\n ")) 

#aritméticos
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2

print(f"A soma é: {sum}")
print(f"A subtração é: {sub}")
print(f"A multiplicação é: {mult}")
print(f"A divisão é: {div}")
print(f"O módulo é: {mod}")
print(f"O expoente é: {exp}")

#comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"O primeiro número é maior que o segundo? {bigger}")
print(f"O primeiro número é menor que o segundo? {smaller}")
print(f"O primeiro número é igual ao segundo? {equal}")
print(f"O primeiro número é diferente do segundo? {different}")
print(f"O primeiro número é maior ou igual ao segundo? {bigger_equal}")
print(f"O primeiro número é menor ou igual ao segundo? {smaller_equal}")

#atribuição
num1 += 5  # num1 = num1 + 5
num1 -= 3  # num1 = num1 - 3
num1 *= 2  # num1 = num1 * 2
num1 /= 4  # num1 = num1 / 4
num1 %= 3  # num1 = num1 % 3
num1 **= 2 # num1 = num1 ** 2
num1 //= 2 # num1 = num1 // 2
print(f"O valor final de num1 após as operações de atribuição é: {num1}")