print("Tabuada do MeLu!")
print("Este programa foi criada para ajudar a Clarinha nas tarefas da escola. \n")

numero = int(input("Informe o valor do qual deseja obter a tabuada: "))
contadora = 1

print("\nA tabuada do número {} é: ".format(numero))

while (contadora <= 10):
    resultado = numero * contadora
    print("{} X {} = {}".format(numero, contadora, resultado))
    contadora = contadora + 1
