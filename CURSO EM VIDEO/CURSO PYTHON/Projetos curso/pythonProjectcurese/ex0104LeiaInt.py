def leiaint(txt):
    print('-'*30)
    n = input(('Digite um numero: ')).strip()
    if n.isalpha() or len(n) == 0 :
        while True:
            print('\033[31mErro! Digite um valor valido.\033[m')
            n = input(('Digite um numero Inteiro: '))
            if n.isnumeric():
                break
    else:
        return n
    return n

n = leiaint('Digite um valor:')
print(f'Você acabou de digitar o numero {n}')
