n = int(input('Digite um numero inteiro'))
esc = int (input('''Você gostaria de converter para\nBinario    [1]\nOctadecimal[2]\nHexadecimal[3]
\nEcolha a sua opção:'''))
if esc == 1:
    print('{} convertido para Binário é {}'.format(n,bin(n)[2:]))
elif esc == 2:
    print('{} convertido para Octadecimal é {}'.format(n,oct(n)[2:]))
elif esc == 3:
    print('{} convertido para Hexadecimal é {}'.format(n,hex(n)[2:]))
elif esc > 3:
    print('Não existe essa opção!')