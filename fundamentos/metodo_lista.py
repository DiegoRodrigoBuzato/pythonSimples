films_list = ["Inception", "The Shawshank Redemption",
              "The Dark Knight", "Pulp Fiction", "Interstellar "]

# Tamanho da lista
print(len(films_list))

# Recuperar item da lisat pelo ìndice
print(films_list.index("Pulp Fiction"))

# Adicionar um item ao final da lista 
films_list.append("The Lor of Rings")
print(films_list)

# Ordenar lista
films_list.sort()
print(films_list)

# Copiaos itens de uma lista para outra
films_copy = films_list.copy()
films_copy.remove("Pulp Fiction")
print(films_copy)

# Remove todos os itens da lista
films_list.clear()
print(films_list)  