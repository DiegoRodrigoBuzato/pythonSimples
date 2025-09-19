films_set = {"Inception", "The Shawshank Redemption",
             "The Dark Knight", "Pulp Fiction", "Interstellar "}
print(type(films_set))

# Buscar o tamanho do set 
print(len(films_set))

# True e 1 são considerados o mesmo valor 
example_set = {"Inception", True, 1, 8.7}
print(example_set)

# Adicionar um item de outro set
films_set.update(example_set)
print(films_set)

# remover um item do set
films_set.remove(True)
films_set.remove(8.7)
print(films_set)