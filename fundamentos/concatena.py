name = input("Digite o nome do filme:\n")
year_launch = int(input("Digite o ano do filme:\n"))
note_movie = float(input("Digite a nota do filme:\n"))

print("Dados do filme")
print("===================")
#alternativa 1
print("Nome do filme:",name)
print("Ano do lançamento:",year_launch)
print("Nota do filme:",note_movie)

#alternativa 2
print("Nome do Filme:", name, "\nAno do lançamento:", year_launch, "\nNota do filme:", note_movie)

#alternativa 3 
print(f"Nome do filme: {name}\n"
      f"Ano do lançamento: {year_launch}\n"
      f"Nota do filme: {note_movie}\n"
    )