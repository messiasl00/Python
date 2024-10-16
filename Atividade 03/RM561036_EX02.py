print("TABELA DE COMPRA DE UM VEÍCULO\n")

valor = float(input("Informe o preço do carro: "))

desconto = valor * 0.2
valor_com_desconto = valor - desconto

desconto = 0
parc=60

print("\nO preço final á vista com desconto 20% é R${:.2f}".format(valor_com_desconto))
for parcelas in range (6,parc + 1, 6):
    if parcelas == 6:
        acrescimo = valor * 0.03
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas,valor_final, valor_parcela))
    elif parcelas == 12:
        acrescimo = valor * 0.06
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 18:
        acrescimo = valor * 0.09
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 24:
        acrescimo = valor * 0.12
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 30:
        acrescimo = valor * 0.15
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 36:
        acrescimo = valor * 0.18
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 42:
        acrescimo = valor * 0.21
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 48:
        acrescimo = valor * 0.24
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 54:
        acrescimo = valor * 0.27
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))
    elif parcelas == 60:
        acrescimo = valor * 0.3
        valor_final = valor + acrescimo
        valor_parcela = valor_final / parcelas
        print("O preço final parcelado em {}x é de R${:.2f} com parcelas de R${:.2f}".format(parcelas, valor_final,
                                                                                             valor_parcela))