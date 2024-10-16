print("INVESTIMENTOS\n")

print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")
print("4. Sair")
escolha = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

resgate = float(input("Digite o valor a ser resgatado: "))
dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

aliquota = 0

if escolha == 1:
    if dias <= 180:
        aliquota = resgate * 0.22
        print("O valor do imposto de renda a ser pago é: R${.:2f}.".format(aliquota))
    elif dias >= 181 and dias <= 360:
        aliquota = resgate * 0.20
        print("O valor do imposto de renda a ser pago é: R${:.2f}.".format(aliquota))
    elif dias >= 361 and dias <= 720:
        aliquota = resgate * 0.17
        print("O valor do imposto de renda a ser pago é: R${.:2f}.".format(aliquota))
    else:
        aliquota = resgate * 0.15
        print("O valor do imposto de renda a ser pago é: R${.:2f}.".format(aliquota))
elif escolha == 2:
    print ("Seja bem-vindo ao LCI")
elif escolha == 3:
    print ("Seja bem-vindo ao LCA")
elif escolha == 4:
    print("Muito obrigado, até logo!")
else:
    print("Opção inválida! Por favor, reinicie o programa ...")