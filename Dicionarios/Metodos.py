# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#     "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
# }

# contatos.clear()# Remove todos os itens do dicionario

# # Mas tome cuidado, pois isso apagará todos os dados armazenados no dicionário!
# print(contatos)  # {}





# contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# copia = contatos.copy()
# copia["guilherme@gmail.com"] = {"nome": "Gui"}

# print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

# print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}




# resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None} # Cria um dicionario com as chaves especificadas e valores padrao None
# print(resultado)

# resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"} # Cria um dicionario com as chaves especificadas e valores padrao "vazio"
# print(resultado)