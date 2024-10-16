print("Batimentos Cardíacos MeLu\n")
print("A pesquisa foi realizada de acordo com o site Tua Saúde: https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm\n")

bpm = int(input("Informe o número de batimentos por minuto: "))
idade = int(input("Informe sua idade: "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Para sua idade de {} anos e com {} de BPM, você está DENTRO da faixa adequada!".format(idade, bpm))
    elif bpm > 140:
        print("Para sua idade de {} anos e com {} de BPM, você está ACIMA da faixa adequada!".format(idade, bpm))
    else:
        print("Para sua idade de {} anos e com {} de BPM, você está ABAIXO da faixa adequada!".format(idade, bpm))

if idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Para sua idade de {} anos e com {} de BPM, você está DENTRO da faixa adequada!".format(idade, bpm))
    elif bpm > 100:
        print("Para sua idade de {} anos e com {} de BPM, você está ACIMA da faixa adequada!".format(idade, bpm))
    else:
        print("Para sua idade de {} anos e com {} de BPM, você está ABAIXO da faixa adequada!".format(idade, bpm))

if idade >= 18 and idade <= 59:
    if bpm >= 70 and bpm <= 80:
        print("Para sua idade de {} anos e com {} de BPM, você está DENTRO da faixa adequada!".format(idade, bpm))
    elif bpm > 80:
        print("Para sua idade de {} anos e com {} de BPM, você está ACIMA da faixa adequada!".format(idade, bpm))
    else:
        print("Para sua idade de {} anos e com {} de BPM, você está ABAIXO da faixa adequada!".format(idade, bpm))

if idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Para sua idade de {} anos e com {} de BPM, você está DENTRO da faixa adequada!".format(idade, bpm))
    elif bpm > 61:
        print("Para sua idade de {} anos e com {} de BPM, você está ACIMA da faixa adequada!".format(idade, bpm))
    else:
        print("Para sua idade de {} anos e com {} de BPM, você está ABAIXO da faixa adequada!".format(idade, bpm))

else:
    print("Não existem dados para a idade indicada")