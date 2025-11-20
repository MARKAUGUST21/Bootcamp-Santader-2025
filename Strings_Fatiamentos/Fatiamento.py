nome = "gUIlherme"

print(nome.upper()) # Transforma todos os caracteres em maiusculo
print(nome.lower()) # Transforma todos os caracteres em minusculo
print(nome.title()) # Transforma o primeiro caractere de cada palavra em maiusculo

texto = "    Ola mundo!"

print(texto.strip() + ".")  # Elimina os espaços em branco no inicio e no fim da string
print(texto.lstrip() + ".") # Elimina os espaços em branco no inicio da string
print(texto.rstrip() + ".") # Elimina os espaços em branco no fim da string


menu = "Python"

print("###" + menu + "###")# Centraliza a string de acordo com o numero de caracteres informado
print(menu.center (12, "#")) # Centraliza a string de acordo com o numero de caracteres informado