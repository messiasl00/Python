print("Seja bem-vindo a calculdora do MeLu!")
print("Está calculadora foi criada para ajudar a Clarinha nas tarefas da escola. \n")

op = 0
while op !=6 :
    num1 = float(input("Qual o valor do primeiro número: "))
    num2 = float(input("Qual o valor do segundo número: "))

    print ("\n1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Resto da divisão")
    print ("6 - Sair\n")
    op = int(input("Qual das opções acima deseja realizar: "))

    if (op == 1):
        resultado = num1 + num2
        print("A soma dos dois valores é {}\n".format(resultado))
    elif (op == 2):
        resultado = num1 - num2
        print("A subtração dos dois valores é {}\n".format(resultado))
    elif (op == 3):
        resultado = num1 * num2
        print("A multiplicação dos dois valores é {}\n".format(resultado))
    elif (op == 4):
        resultado = num1 / num2
        print("A divisão dos dois valores é {}\n".format(resultado))
    elif (op == 5):
        resultado = num1 % num2
        print("O resto da divisão dos dois valores é {}\n".format(resultado))
    elif (op >= 7 ):
        print("Opção incorreta!\n")

print("\nPrograma encerrado, muito obrigado!")