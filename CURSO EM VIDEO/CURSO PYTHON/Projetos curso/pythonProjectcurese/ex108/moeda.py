
def moeda(n=0):
    r = f'R${n:.2f}'.replace('.',',')
    return r

def dobro(n=0):
    r = n*2
    return r
def aument10(n=0):
    r = n+((n*10)/100)
    return r
def dimi13(n=0):
    r = n-((n*13)/100)
    return r
def metade(n=0):
    r = n/2
    return r