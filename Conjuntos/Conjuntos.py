# Um set é uma colletion que nao possui objetos repetidos, usamos sets para representar conjuntos matematicos ou elinar duplicatas de uma lista.

# Set nao se pode confiar na ordem dos elementos, ou seja, a ordem pode mudar a qualquer momento.

# numeros = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9])
# print(numeros)  

# letras = set("banana")
# print(letras)

# carros = set(("Gol", "Palio", "Celta", "Onix", "Palio"))
# print(carros)

# linguagens = {"Python", "Java", "C++", "JavaScript", "Python"}
# print(linguagens)


# Fatos importantes sobre set: 
# Conjunto em python nao suportam indexacao, slicing ou outras operações comuns de sequencias.

# numeros = {1, 2, 3, 4, 5}

# numero = list(numeros)

# print(numero[0:6])  # Acessando o primeiro elemento convertendo para lista


# # percorrendo o ser com loop

# for numero in numeros:
#     print(numero)

# Unindo conjuntos com .union()

set = {1, 2, 3}
set2 = {4, 5, 6}

set3 = set.union(set2)
print(set3)