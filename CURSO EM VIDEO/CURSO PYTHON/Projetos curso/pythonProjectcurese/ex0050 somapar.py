s=0
c1=0
for c in range(0,6):
    n = int(input('Digite um numero:'))
    if (n%2)==0:
        s+=n
        c1 += 1
print('Você informou {} valores pares,a soma dos valores pares são {}'.format(c1,s))