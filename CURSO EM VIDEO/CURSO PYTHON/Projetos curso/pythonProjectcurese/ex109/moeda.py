
def moeda(n):
    r = f'R${n:.2f}'.replace('.',',')
    return r

def dobro(n,f=False):
    r = n*2
    if f == True:
        r = f'R${n:.2f}'.replace('.', ',')
    return r
def aument10(n,f=False):
    r = n+((n*10)/100)
    if f == True:
        r = f'R${n:.2f}'.replace('.', ',')
        r
    return r
def dimi13(n,f=False):
    r = n-((n*13)/100)
    if f == True:
        r = f'R${n:.2f}'.replace('.', ',')
    return r
def metade(n,f=False):
    r = n/2
    if f == True:
        r = f'R${n:.2f}'.replace('.', ',')
    return r