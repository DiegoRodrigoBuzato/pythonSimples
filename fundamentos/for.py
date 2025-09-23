# Lista de filmes 
movies_list = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Interando valores de uma lista 
for movie in movies_list:
    print(movie)

# Quando a condição for atendida, o loop é interrompido
for movie in movies_list:
    if movie == "Interstellar":
        break
    print(movie)

# Qunadoi a condição for atendida, o loop vaio para proxima iteração
for movie in movies_list:
    if movie == "Interstellar":
        continue
    print(movie)

# Avaliação do filme 
movie_name = input("Digite o nome do filme:\n")
movie_rating = int(input("Digite quantas avaliações deseja fazer:(0 a 10):\n"))

total=0
for i in range(movie_rating):
    note = float(input(f"Digite a nota:\n"))
    total += note

if movie_rating > 0:
    average = total / movie_rating
else :
    average = 0 
print(f"A média das notas do filme '{movie_name}' é: {average:.2f}")