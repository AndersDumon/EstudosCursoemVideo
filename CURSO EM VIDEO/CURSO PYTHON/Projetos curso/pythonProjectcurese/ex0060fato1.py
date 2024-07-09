from math import factorial
n = int(input('digite um valor para saber o seu fatorial: '))
f = n
s = n
f2 = n
print('{}! ='.format(n),end='')
while f != 0:
    print(' {}'.format(f),end='')
    print(' x'if f > 1 else ' =',end=' ')
    f -=1
while f2 != 1:
    f2 -=1
    s = s*f2
print(s)

'''# correção importe o math from factorial
n = int(input( 'digite o valor'))
f = factorial(n)
print(' o fatorial é {}'.format(f))'''