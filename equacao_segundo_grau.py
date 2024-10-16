import math

print("Equação de 2° grau com MeLu!")
print("Este programa foi criada para ajudar a Clarinha nas tarefas da escola. \n")

#Realizando o cálculo Delta

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta = b * b - 4 * a * c

if delta > 0.0 :
    #Cálculo de dois valores para x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1  = {} e x2 = {}".format(a,b,c,x1,x2))

elif delta == 0.0 :
    #Cálculo de um valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1  = {}".format(a,b,c,x))

else:
    print=("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a,b,c))
