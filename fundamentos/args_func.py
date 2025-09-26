# Função para imprimir um nome completo 
def full_name(first_name, last_name):
    print(f'Nome é: {first_name} {last_name}')

full_name("Fulano", "Siclano")
full_name("João", "da Silva")

# Função para somar dois números 
def sum_numbers(a, b):
    return a + b
print(f'A soma é: {sum_numbers(10, 5)}')

# Função com parametro default
def address(country="Brasil"):
    print(f'Eu moro no(a): {country}')

address()
address("Argentina")

# Função para avaliar um filme utiolizando parametro 
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input(f"Insira a nota do filme {movie_name}:\n "))
        total += note
    
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    
    print(f'Média de avaliações do filme {movie_name} é: {average:.2f}')

rate_movie(3, "Avatar")