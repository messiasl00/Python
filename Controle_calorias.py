print("Controle de Calorias - MeLu!")
print("Programa criado especialmente para MeLu, esposa do MeLu.\n")

alimentos = int(input("Informe a quantidade de alimentos ingeridos no dia: "))
incremental = 1
total_calorias = 0

while incremental <= alimentos :
    calorias = float(input("Informe a quantidade de calorias do alimento {}: ".format(incremental)))
    total_calorias += calorias
    incremental += 1

print("O total de calorias consumida no dia foi de {} kcal .".format(total_calorias))
