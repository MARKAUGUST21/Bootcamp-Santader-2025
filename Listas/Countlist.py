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


# .index serve para encontrar o índice de um elemento na lista.
# Detalhe: se o elemento aparecer mais de uma vez, ele retorna o índice da primeira ocorrência.
# Exemplo:

lista = ['a', 'b', 'c', 'd', 'e'] # lembrando que o índice começa em 0 ;)
indice = lista.index('c')
print(f"O índice do elemento 'c' é: {indice}")

#.insert serve para inserir um elemento em uma posição específica da lista.
# Exemplo:
lista = [1, 2, 4, 5]
lista.insert(2, 3) # insere o número 3 na posição de índice 2
print("Lista após o insert:", lista)

#.pop serve para remover e retornar um elemento de uma lista, baseado no índice fornecido.
# Se nenhum índice for fornecido, ele remove e retorna o último elemento da lista.
# Exemplo:
lista = [10, 20, 30, 40, 50]
elemento_removido = lista.pop(2) # remove o elemento no índice 2
print(f"Elemento removido: {elemento_removido}")
print("Lista após o pop:", lista)

#.remove serve para remover a primeira ocorrência de um elemento específico em uma lista.
# Exemplo:
lista = [1, 2, 3, 2, 4, 2]
lista.remove(2) # remove a primeira ocorrência do número 2
print("Lista após o remove:", lista)

#.reverse serve para inverter a ordem dos elementos em uma lista.
# Exemplo:
lista = [1, 2, 3, 4, 5]
lista.reverse()
print("Lista após o reverse:", lista)

#.sort serve para ordenar os elementos de uma lista.
# Exemplo:
lista = [5, 2, 9, 1, 5, 6]
lista.sort()
print("Lista após o sort:", lista)

# len() serve para obter o número de elementos em uma lista.
# Exemplo:
lista = [1, 2, 3, 4, 5]
tamanho = len(lista)
print(f"O tamanho da lista é: {tamanho}")

#.copy serve para criar uma cópia rasa (shallow copy) de uma lista.
# Exemplo:
listas = [1, "Python", [40, 30, 20]]
l2 = listas.copy()
print(listas)
print(l2)