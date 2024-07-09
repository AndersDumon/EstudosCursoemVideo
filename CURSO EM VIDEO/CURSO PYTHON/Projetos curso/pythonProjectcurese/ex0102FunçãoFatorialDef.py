def fatorial(n,show=False):
    """
    -> CALCULA O FATORIAL  DE UM NÚMERO.
    :param n: O NÚMERO A SER CALCULADO.
    :param show: (OPCIONAL) MOSTRAR OU NÃO A CONTA.
    :return:O VALOR DO FATORIAL DE UM NÚMERO N.
    """
    print('-'*40)
    f = 1
    if show ==True:
        for c in range(n,0,-1):
            f *=c
            print(c,end='')
            print(f' x ' if c > 1 else' = ',end='')
        print(f)
    else:
        for c in range(n,0,-1):
            f *=c
        print(f)

fatorial(10,True)
fatorial(10,False)
help(fatorial)