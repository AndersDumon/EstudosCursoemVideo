import random
print('Vamos jogar par ou impar?')
I = str('Impar')
P = str('Par')
v = 0
while True:
    pc = random.randint(0,10)
    jogador= int(input('Diga o valor: '))
    soma = jogador + pc
    pip =' '
    while pip not in 'PI':
        pip = str(input('Par ou Impar?[P/I]: ')).strip().upper()[0]
    print(f'Jogador {jogador} X {pc} Computador, Total = {soma}')
    if pip == 'P' :
        if (soma % 2) == 0:
            print('Você Venceu!')
            print (f'Deu {P}')
            v += 1
        else:
            print('Você Perdeu!')
            print(f'Deu {P}')
            break
    elif pip == 'I':
        if (soma% 2) == 1:
            print('Você venceu!')
            print(f'Deu {I}')
            v += 1
        else:
            print('Você Perdeu!')
            print(f'Deu {I}')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes')

