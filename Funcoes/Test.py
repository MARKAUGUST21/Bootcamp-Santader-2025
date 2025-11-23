# def somar(a, b):
#    resultado = a + b
#    print(f"A soma de {a} + {b} é igual a {resultado}")
   
   
# somar(2, 3,)


def somar(a, b):
   return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")
    
    
exibir_resultado(4, 5, somar)