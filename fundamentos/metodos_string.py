movie_name = "Top Gun"
movie_description = """Top Gun is a 1986 American action, 
        drama film directed by Tony Scott"""

print (movie_name.upper())#tudo maiusculo
print (movie_name.lower())#tudo minusculo
print (movie_name.capitalize())#primeira letra maiouscula
print (movie_name.title())# todas primeiras letras maiusculas
print(movie_name.center(10, '-'))#retorna string centralizada com caractere preenchido
print(movie_name.find("u"))#retorna a posiçao inicial da string procurada
print(movie_name.replace("Gun", "Rain"))#substitui a string procurada
print(movie_description.split(','))#divide a string em uma lista