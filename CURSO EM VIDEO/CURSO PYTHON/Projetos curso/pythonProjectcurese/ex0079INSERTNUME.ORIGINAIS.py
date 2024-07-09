numeros = list()
r = ''
while r != 'N':
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('ADICIONADO COM SUSSESO!')
    else:
        print('VALOR DUPLICADO , NÃO SERÁ ADICIONADO!')
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if r != 'N' or r != 'S':
        while r != 'N' and r != 'S':
            print('\033[31mValor Invalido\033[m')
            r = str(input('Quer continuar? [S/N]: ')).upper()
numeros.sort()
print(numeros)
