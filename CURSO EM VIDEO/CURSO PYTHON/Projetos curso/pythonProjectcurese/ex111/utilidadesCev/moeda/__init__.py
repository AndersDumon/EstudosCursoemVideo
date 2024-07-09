def metade(n,f=False):
    r = n/2
    if f == True:
        r = f'R${n:.2f}'.replace('.', ',')
    return r
def moeda(n):
    r = f'R${n:.2f}'.replace('.', ',')
    return r

def dobro(n,f=False):
    r = n*2
    if f == True:
        r = f'R${n:.2f}'.replace('.',',')
    return r
def aument(n,m,f=False):
    r = n+((n*m)/100)
    if f == True:
        r = f'R${n:.2f}'.replace('.', ',')
    return r
def dimi(n, o, f=False):
    r = n-((n*o)/100)
    if f == True:
        r = f'R${n:.2f}'.replace('.', ',')
    return r
def resumo(n=0, m=0, o=0,):
    print('='*30)
    print(f'{"RESUMO DO VALOR":^25}')
    print('='*30)
    li = ('Preço Analisado', moeda(n), 'Dobro do Preço', moeda(dobro(n)),
          'Metade do preço', moeda(metade(n)),f'{m}% de aumento',
          moeda(aument(n, m)), f'{o}% de redução', moeda(dimi(n, o)))
    for c in range(0, len(li)):
        if c % 2 == 0:
            print(f'{li[c]:<20}', end=' ')
        else:
            print(f'{li[c]:>2}')
    print('=' * 30)
