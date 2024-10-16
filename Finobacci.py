print("Bem-vindo ao jogo Sequência de Finobacci!\n")

a = 1
b = 1


while True:
    resposta = int(input("Qual é o número: "))
    if resposta == a:
        print("Correto! Vamos continuar ...")
        atual = a + b
        a = b
        b = atual
    else:
        print("Errado :( o número correto era {}".format(a))
        break
