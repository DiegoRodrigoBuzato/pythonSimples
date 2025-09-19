import pprint

film_dict = {
    "inception": {
        "year_release": 2010,
        "imdb_rating": 8.8,
        "genre": ["Action", "Sci-Fi", "Thriller"],
    },  
    "interstellar": {
        "year_release": 2014,
        "imdb_rating": 8.6,
        "genre": ["Adventure", "Drama", "Sci-Fi"],
    }, 
    "the_dark_knight": {
        "year_release": 2008,
        "imdb_rating": 9.0,
        "genre": ["Action", "Crime", "Drama"],
    }
}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(film_dict)

# Buscar uma informação dentro de um dicionário aninhado
print(film_dict["inception"]["imdb_rating"])

# Adicionar um novo item 
film_dict["the_dark_knight"]["director"] = "Christopher Nolan"
pp.pprint(film_dict)

# Excluir um dicionário
del film_dict["interstellar"]
pp.pprint(film_dict)    