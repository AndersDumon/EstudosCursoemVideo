a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
c = int(input('digite o terceiro numero'))
# verificando qual é menor
menor = a
if b<a and b<c:
    menor= b
if c<a and c<b:
    menor = c
 # verificando qual é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(' o maior valor é {}'.format (maior))
print(' o menor valor é {}'.format(menor))