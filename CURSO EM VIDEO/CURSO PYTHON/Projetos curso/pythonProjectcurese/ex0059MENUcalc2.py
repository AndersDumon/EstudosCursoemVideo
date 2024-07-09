from time import sleep
r = 0
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
print('=°'*70)
while r != 5:
    print('\033[34m[1]Somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]Trocar numeros')
    print('[5]Sair do programa\033[m')
    s = n1 + n2
    m = n1 * n2
    r = int(input('\033[32mDigite oque você gostaria de fazer?:\033[m'))
    if r == 1:
         print('A soma entre os valores \033[32m{}\033[m + \033[32m{}\033[m é: {}'. format(n1,n2,s))
    elif r == 2:
         print('A multiplicação entre os valores \033[32m{}\033[m X \033[32m{}\033[m é: {}'.format(n1,n2,m))
    elif r == 3:
        if n1 > n2:
            print('O maior é \033[32m{}\033[m e o menor é \033[32m{}\033[m '.format(n1,n2))
        else:
            print('O maior é \033[32m{}\033[m e o menor é \033[32m{}\033[m'.format(n2,n1))
    elif r == 4:
        print('Para qual valor você gotaria de trocar?')
        n1 = int(input('1° valor:'))
        n2 = int(input('2° valor:'))
    elif r == 5:
        sleep(2)
        print('Obrigado por utilizar o nosso programa!')
    elif r > 5:
        print('\033[31mValor Invalido!\033[m')
    else:
        print('\033[31mValor Invalido!\033[m')
    sleep(1)
    print('=°' * 70)
print('Fim do programa!')

