print('Qual Tabuada você gostaria de saber?')
v = cont = 0
while v != '-':
    print('*=*'*20)
    v = int(input('Quer ver a tabuada de qual Valor?: '))
    print('*=*' * 20)
    cont = 0
    if v < 0:
        break
    while cont != 10:
        cont += 1
        print(f'{v}x{cont}={v*cont}')
print('Fim do programa!')


