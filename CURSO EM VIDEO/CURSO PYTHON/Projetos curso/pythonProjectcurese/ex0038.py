print('digite os valore')
v1 = int(input(' digite o primeiro valor: '))
v2 = int (input('digite o segundo valor: '))
if v1 > v2:
    print('\033[35mO primeiro valor {} é maior que o segundo valor {}\033[m'.format(v1,v2))
elif v1 < v2:
    print('\033[34mO segundo valor {} é maior que primeiro  valor {}\033[m'. format(v2,v1))
else:
    print('\033[36mOs valores {} e {} são iguais\033[m'.format(v1,v2))
