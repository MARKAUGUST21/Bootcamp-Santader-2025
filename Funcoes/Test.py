# def somar(a, b):
#    resultado = a + b
#    print(f"A soma de {a} + {b} é igual a {resultado}")
   
   
# somar(2, 3,)


# def somar(a, b):
#    return a + b

# def exibir_resultado(a, b, funcao):
#     resultado = funcao(a, b)
#     print(f"O resultado da operação é: {resultado}")
    
    
# exibir_resultado(4, 5, somar)


salario = 4000

def salario_bonus(bonus):
    # Colocando Global aqui para dizer que a variavel salario é a de fora da funcao
    global salario
    salario += bonus
    print(f"Salario com bonus: {salario}") # Ou mostrar o salario atualizado aqui mesmo
    return salario


salario_bonus(500)
print(salario)# temos como colocar no final da operacao o valor atualizado da variavel salario que foi modificada dentro da funcao