print('analisador de triângulo 02')
r1 = float(input(' digite o numero da linha'))
r2 = float(input('digite o numero da segunda linha'))
r3 = float(input('digite o numero da terceira linha'))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Pode formar um triangulo ')
    if r1 == r2 == r3:
        print('Esse triangulo é Equilatero pois todos os lados são iguais')
    elif r1 != r2 != r3 != r1 :# [!=] diferente
        print('Esse triangulo é Escaleno pois todos os lados são diferentes')
    else:
        print('Esse triangulo é Isóseles pois existe dois lados iguais')
else:
    print('não pode formar um triangulo')