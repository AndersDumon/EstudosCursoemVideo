ini =int(input('Digite o primeiro termo '))
ra = int(input('Digite a razão'))
cont = 1
termos = ini
res = 10
total = 0
while res != 0:
    total = total + res
    while cont <= total:
        cont += 1
        termos += ra
        print(termos,end=' ')
    res = int(input('\nMais quantos termos: '))
print('O total de termos foi {}'.format(total))
print('Fim do programa!')
