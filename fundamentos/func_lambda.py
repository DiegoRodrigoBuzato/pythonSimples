# Função de potência de um número 
power = lambda num : num **2
print(power(5))

# Função que verifica se o número é par 
is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(43))

# Função que divide um número por outro
div_num = lambda x,y: x / y
print(div_num(10,2))

# Função que inverte uma string 
reverse_string = lambda s: s[::-1]
print(reverse_string("Hello World"))

# Funcionalidades relacionadas aos filmes 
movies_list = ["Inception", "The Shawshank Redemption",
              "The Dark Knight", "Pulp Fiction", "Interstellar "]
ratings = {
    "Inception": [8.8, 9.0, 6.8],
    "The Shawshank Redemption": [9.3, 8.5, 6.9],
    "The Dark Knight": [9.0, 8.5, 7.0],
    "Pulp Fiction": [8.9, 8.0, 7.5],
    "Interstellar": [8.6, 7.5, 6.5],
}

# Função para calcular a média das avaliações de um filme 
averege_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f'Média de avaliações de Inception: {averege_rating("Inception")}')

#Função que verifica se um filme está na lista 
check_movie = lambda movie_name: movie_name in movies_list

print(f'Inception está na lista? {check_movie("Inception")}')

# recomendar um filme com base na avaliação média 
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {averege_rating(movie_name):.2f}"
print(f'{recommend_movie("The Dark Knight")}')