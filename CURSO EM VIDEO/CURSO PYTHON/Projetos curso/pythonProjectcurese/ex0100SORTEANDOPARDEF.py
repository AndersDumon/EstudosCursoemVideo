import random
import time

num = (random.randint(0, 10), random.randint(0, 10),
       random.randint(0, 10), random.randint(0, 10),
       random.randint(0, 10))
def soteia(lst):
    print(f'Sorteando {len(lst)} valores da lista',end=' ')
    for c in lst:
        time.sleep(0.5)
        print(f'{c}',end=' ',flush=True)
    print('Pronto!')
def somapar(lst):
    soma = 0
    for c in lst:
        if c %2 == 0:
            soma +=c
    print(f'Somando os valores pares de {lst} , temos {soma}')



soteia(num)
somapar(num)