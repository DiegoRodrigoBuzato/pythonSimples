# Função para imprimir uma mensagem
def welcome():
    print("Bem-vindo ao sistema de filmes!")

# for i in range (10):
#     welcome()

#Função para calcular a média de notas 
def calculate_average():
    num_ratings = int(input("Quantas notas você quer inserir?\n "))
    total = 0
    for i in range(num_ratings):
        note = float(input(f"Insira a nota:\n "))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
        print(f"A média das notas é: {average}")
    else:
        average = 0
        print("Nenhuma nota foi inserida.")
    
    return average

print(f"a média de avaliações é: {calculate_average():.2f}")    

# Função para cadastrar um filme 
def create_movie():
    name = input("Insira o nome do filme:\n ")
    year_launch = int(input("Insira o ano de lançamento:\n "))
    movie_price = float(input("Insira o preço do filme:\n "))
    rating = float(input("Insira a nota do filme:\n "))
    print(f"{name} ({year_launch}) - R$ {movie_price:.2f}")

create_movie()
create_movie()