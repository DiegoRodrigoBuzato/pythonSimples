# Lista de filmes 
movies_list = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Interando valores de uma lista de filmes usando while 
index = 0
while index < len(movies_list):
    print(movies_list[index])
    index += 1

# Quando a condição for atendida, o loop será encerrado
index = 0
while index < len(movies_list):
    if movies_list[index] == "Interstellar":
        break
    print(movies_list[index])
    index += 1

# Quando a condição for atendida, o loop vai para próxima interação
index = 0
while index < len(movies_list):
    if movies_list[index] == "Interstellar":
        index += 1
        continue
    print(movies_list[index])
    index += 1

# Avaliação do filme com while
movie_name = input("Digite o nome do filme:\n")
movie_rating = int(input("Digite quantas avaliações deseja fazer:\n"))
total=0
count=0

while count < movie_rating:
    note = float(input(f"Digite a nota:\n"))
    total += note
    count += 1

if movie_rating > 0:
    average = total / movie_rating
else :
    average = 0 
print(f"A média das notas do filme '{movie_name}' é: {average:.2f}")