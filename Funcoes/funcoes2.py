# def criar_carro(modelo, ano, placa, / , marca, motor, combustivel):
#     print(f"Carro criado: {marca} {modelo} {ano} {placa} {motor} {combustivel}")


# criar_carro("Civic", 2020, "ABC-1234", marca="Honda", motor="2.0", combustivel="Gasolina") # Dessa forma funciona, pois os tres primeiros parametros sao posicionais obrigatorios

# # criar_carro(modelo="Corolla", ano=2019, placa="XYZ-5678", marca="Toyota", motor="1.8", combustivel="Flex") # Dessa forma vai dar erro, pois os tres primeiros parametros sao posicionais obrigatorios


def criar_carro(*, marca, modelo, ano, placa, motor, combustivel): # AQUI ELE OBRIGA TODOS OS PARAMETROS A SEREM NOMEADOS
   print(f"Carro criado: {marca} {modelo} {ano} {placa} {motor} {combustivel}")
   
criar_carro(marca="Honda", modelo="Civic", ano=2020, placa="ABC-1234", motor="2.0", combustivel="Gasolina") # Dessa forma funciona, pois todos os parametros sao nomeados obrigatorios