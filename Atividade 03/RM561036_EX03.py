print("RENEGOCIAÇÃO\n")

divida = float(input("Informe o valor da dívida: "))

parc=12
vista=1

if vista == 1:
    total = divida * 0
    juros = 0
    valor_parcela = divida
    print(
        "Total: R${:.2f} | Juros: R${:.2f} | Número de parcelas: {} | Valor da parcela: R${:.2f}".format(divida, juros,
                                                                                                         vista,
                                                                                                         valor_parcela))

for parcelas in range(3,parc + 1, 3):
    if parcelas == 3:
        acrescimo = divida * 0.1
        total = divida + acrescimo
        juros = total - divida
        valor_parcela = total / parcelas
        print ("Total: R${:.2f} | Juros: R${:.2f} | Número de parcelas: {} | Valor da parcela: R${:.2f}".format(total, juros, parcelas, valor_parcela))
    elif parcelas == 6:
        acrescimo = divida * 0.15
        total = divida + acrescimo
        juros = total - divida
        valor_parcela = total / parcelas
        print ("Total: R${:.2f} | Juros: R${:.2f} | Número de parcelas: {} | Valor da parcela: R${:.2f}".format(total, juros, parcelas, valor_parcela))

    elif parcelas == 9:
        acrescimo = divida * 0.2
        total = divida + acrescimo
        juros = total - divida
        valor_parcela = total / parcelas
        print ("Total: R${:.2f} | Juros: R${:.2f} | Número de parcelas: {} | Valor da parcela: R${:.2f}".format(total, juros, parcelas, valor_parcela))

    elif parcelas == 12:
        acrescimo = divida * 0.25
        total = divida + acrescimo
        juros = total - divida
        valor_parcela = total / parcelas
        print ("Total: R${:.2f} | Juros: R${:.2f} | Número de parcelas: {} | Valor da parcela: R${:.2f}".format(total, juros, parcelas, valor_parcela))