# O count serve para contar o número de ocorrências de um elemento em uma lista.
# Exemplo:

# .count(elemento)
lista = [1, 2, 3, 2, 4, 2, 5, 5, 5, 5,5 ]
contador = lista.count(5)
print(f"O número 5 aparece {contador} vezes na lista.")

# Ja o extend serve para adicionar elementos de uma lista a outra.
# Exemplo:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print("Lista após o extend:", lista1)