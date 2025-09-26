# Listar valores de 0 a 10 que sejam menores que 4 
list_numbers = [i for  i in range(11) if i < 4]
print(list_numbers)

movies_list = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Filmes que possuem a letras 'e' no título
movies_withE = [movie for movie in movies_list if 'n' in movie.lower()]
print(movies_withE)

# Filmes que eu assisti
movie_watched = [movie for movie in movies_list if movie != "The Matrix"]
print(movie_watched)

# Encontrando um filome pelo nome 
while True:
    search_name = input("Digite o nome do filme que deseja encontrar (ou sair para encerrar): ")
    if search_name.lower() == "sair":
        print("Encerrando a busca.")
        break
    found_movies = [movie for movie in movies_list if search_name.lower() in movie.lower()]
    if found_movies:
        print(f"Filmes encontrados: {search_name}")
        for found_movie in found_movies:
            print(f"- {found_movie}")
    else:
        print(f'Nenhum filme encontrado com o nome: {search_name}')