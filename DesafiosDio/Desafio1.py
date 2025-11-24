print("=============== Desafio 1 ===============")

def calcular_imposto(salario):
    aliquota = 0.00
    
    if salario <= 1100:
        aliquota = 0.05
    elif salario <= 2500:
        aliquota = 0.10
    else:
        aliquota = 0.15

    imposto = salario * aliquota
    print(f'Salario: R$ {salario:.2f} - Aliquota: {aliquota*100:.0f}% - Imposto: R$ {imposto:.2f}')
    return imposto  # <-- AGORA RETORNA

valor_salario = float(input("Digite o valor do salario: R$ "))
valor_beneficio = float(input("Digite o valor do beneficio: R$ "))

valor_imposto = calcular_imposto(valor_salario)
saida = valor_salario - valor_imposto + valor_beneficio

print(f'Salario final com beneficio: R$ {saida:.2f}')
110