# def exibir_mensagem():
#     print("Esta é uma função de exemplo.")
    


# def exibir_mensagem2(nome):
#     print(f"Olá, {nome}!")
    
    
# def exibir_mensagem3(nome = "Usuário"):
#     print(f"Olá, {nome}!")
    


# exibir_mensagem()
# exibir_mensagem2("Guilherme")
# exibir_mensagem3()

# Argumento com parametros 

def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no banco de dados
    print(f"Carro salvo: {marca} {modelo} {ano} {placa}")
    
salvar_carro("Toyota", "Corolla", 2020, "ABC-1234") # Desse jeito os argumentos sao passados na ordem dos parametros
salvar_carro(placa="XYZ-5678", modelo="Civic", ano=2019, marca="Honda") # Desse jeito os argumentos sao passados usando o nome dos parametros, entao a ordem nao importa
salvar_carro("Ford", modelo="Focus", ano=2018, placa="DEF-5678")# Ou seja aqui é o famoso argumento nomeado
salvar_carro(**{"marca": "Chevrolet", "modelo": "Onix", "ano": 2021, "placa": "GHI-9012"}) # Aqui ele mostro pro py que é um dicionario com os nomes dos parametros e valores correspondentes


# *args vai vir como uma tupla de valores
# **kwargs vai vir como um dicionario de valores
