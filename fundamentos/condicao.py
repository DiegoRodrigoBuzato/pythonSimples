# # Informações sobre o filme 
# name = input("Digite o nome do filme:\n")
# year_release = int(input("Digite o ano do filme:\n"))
# rating = float(input("Digite a avaliação do filme (0.0 a 10.0):\n"))

# # Verifica se o filme é recomendado
# if rating > 8.0 and year_release >= 2015:
#     print(f"O filme '{name}' é recomendado.")
# else:
#     print(f"O filme '{name}' não é recomendado.")

num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
operation = input("Digite a operação (+, -, *, /):\n")

if operation == "+":
    result = num1 + num2
    print(f"O resultado da soma é: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"O resultado da subtração é: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"O resultado da multiplicação é: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"O resultado da divisão é: {result}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
     print("Operação inválida")
     result = 0

print(f"O resultado final é: {result:.2f}")