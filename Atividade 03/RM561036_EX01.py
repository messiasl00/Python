print("VOTAÇÃO LIVE - MENTORIA FINANCEIRA\n")

colaboradores = int(input("Informe a quantidade de colaboradores que irão participar da votação: "))

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

for dias in range(1, colaboradores + 1, 1):
    votacao = input("Informe o dia da semana útil da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira): ")
    votacao.lower()

    if votacao == "segunda-feira":
        segunda = segunda + 1
    elif votacao == "terça-feira":
        terca = terca + 1
    elif votacao == "quarta-feira":
        quarta = quarta + 1
    elif votacao == "quinta-feira":
        quinta = quinta + 1
    elif votacao == "sexta-feira":
        sexta = sexta + 1
    else:
        print("Opção inválida! Por favor, insira da maneira que está entre parêntese.")

print("\n")

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia escolhido pelos colaboradores é segunda-feira!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia escolhido pelos colaboradores é terça-feira!")
elif quarta > terca and quarta > segunda and quarta > quinta and quarta > sexta:
    print("O dia escolhido pelos colaboradores é quarta-feira!")
elif quinta > terca and quinta > quarta and quinta > segunda and quinta > sexta:
    print("O dia escolhido pelos colaboradores é quinta-feira!")
elif sexta > terca and sexta > quarta and sexta > segunda and sexta > quinta:
    print("O dia escolhido pelos colaboradores é sexta-feira!")
else:
    print("Houve empate!")