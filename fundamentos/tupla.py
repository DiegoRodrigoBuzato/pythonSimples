films_tuple = ("Inception", "The Shawshank Redemption",
              "The Dark Knight", "Pulp Fiction", "Interstellar ")
print(type(films_tuple))

# Buscar os dois primeiros itens da tupla
print(films_tuple[:2])

# Buscar último item da tupla 
print(films_tuple[-1])

# Buscar filmes até uma determinada posição
print(films_tuple[:3])

# Buscar filmes de uma posição em diante 
print(films_tuple[2:])

# Recuperar um item da tupla pelo nome 
print(films_tuple.index("Pulp Fiction"))