film_inception = {
    "title": "Inception",
    "year_release": 2010,
    "imdb_rating": 8.8,
    "genre": ["Action", "Sci-Fi", "Thriller"],
    }
print(film_inception)
print(len(film_inception))
print(type(film_inception))

# Recuperar um elemento do dicionário 
print(film_inception["genre"])
print(film_inception.get("imdb_rating"))

# Buscar apenas as chaves do dicionário 
print(film_inception.keys())

# Buscar apenas os valores do dicionário
print(film_inception.values())

# Buscar itens do dicionário com chave e valor
print(film_inception.items())

# Adicionar itens no dicionário 
film_inception["director"] = "Christopher Nolan"
print(film_inception)

# atualizar itens do dicionário
film_inception.update({"imdb_rating": 9.0})
print(film_inception)

# Remover itens do dicionário
film_inception.pop("year_release")
print(film_inception)