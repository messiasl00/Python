print("Controle de Gastos - MeLu!")
print("Programa criado especialmente para MeLu, esposa do MeLu.\n")

transacao = int(input("Informe a quantidade de transação realizada no dia: "))
incremental = 1
total_gasto = 0
media = 0

while incremental <= transacao :
    gastos = float(input("Informe o valor gasto para a transação {}: ".format(incremental)))
    total_gasto += gastos
    incremental += 1

media = total_gasto / transacao

print("\nO total gasto foi de R${:.2f} , com média de R${:.2f} por transação !".format(total_gasto, media))