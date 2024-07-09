def leiadinheiro(n):
    n = input(('Digite um valor: R$')).strip().replace(',','.')
    if n.isalpha() or len(n) == 0:
        while True:
            print('\033[31mErro! Digite um valor valido.\033[m')
            n = input(('Digite um valor: R$'))
            if n.isnumeric():
                break
    else:
        n = float(n)
        return n
    n = float(n)
    return n
