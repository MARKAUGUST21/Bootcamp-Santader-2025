# Entrada de dados
peso = float(input("Digite o peso em kg: "))
preco_por_tonelada = float(input("Digite o preco por tonelada: R$ "))

# Menu de tipos de cliente
print("\nEscolha o tipo de cliente:")
print("1 - Cliente Novo")
print("2 - Cliente Fidelizado")
print("3 - Cliente Premium")

opcao = input("Digite o número correspondente ao tipo de cliente: ")

# Calculo do preço total
preco_total = (peso / 1000) * preco_por_tonelada

# Determina o desconto conforme opção
if opcao == "1":
    tipo_cliente = "Cliente Novo"
    desconto = 0.00

elif opcao == "2":
    tipo_cliente = "Cliente Fidelizado"
    desconto = 0.05

elif opcao == "3":
    tipo_cliente = "Cliente Premium"
    desconto = 0.10

else:
    tipo_cliente = "Inválido"
    desconto = 0.00
    print("\n⚠ Opção inválida. Nenhum desconto será aplicado.")

# Calcula o valor final
valor_final = preco_total * (1 - desconto)

# Saída
print("\n===== RESULTADO =====")
print(f"Tipo de cliente: {tipo_cliente}")
print(f"Preço total antes do desconto: R$ {preco_total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Preço final: R$ {valor_final:.2f}")
