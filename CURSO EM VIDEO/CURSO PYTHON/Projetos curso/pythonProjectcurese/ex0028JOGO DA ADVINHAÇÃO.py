import random
from time import sleep
print(('_'*70))
print('Vamos ver se vc adivinha, qual numero estou pensando?')
n = int(input('Escolha um numero de 0 a 5: '))
computador = random.randint(0, 5)
print('huummmmm...')
sleep(3)
if n == computador:
    print('Acertou é {}, Mizeravi!'.format(n))
else:
    print('ERROU não é {}!, TENTE NOVAMENTE!'.format(n))
