# pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"} # Dicionarios são criados usando chaves {}, e levam valores ja designados a chaves especificas

# pessoa = dict(nome="João", idade=30, cidade="São Paulo") # Outra forma de criar dicionarios é usando a funcao dict()

dados = {"nome": "Maria", "idade": 25, "cidade": "Rio de Janeiro"}

dados["nome"] # Acessando valores no dicionario usando a chave correspondente
dados["idade"] = 26 # Modificando o valor associado a uma chave existente
dados["profissao"] = "Engenheira" # Adicionando um novo par chave: valor ao dicionario
del dados["cidade"] # Removendo um par chave: valor do dicionario usando a chave

print(dados)