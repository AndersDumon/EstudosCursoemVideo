s = float(input(' digite o seu salario'))
if s > 1250:
    print('o aumento do salario é {}\ndando um total de {}'.format((s*10)/100,s+(s*10)/100))
else:
    print('o aumento do salario é {}\ndando um total de {}'.format((s*15)/100,s+(s*15)/100))