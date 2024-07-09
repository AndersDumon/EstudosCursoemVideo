import numbers
import time
def contagem(a,b,c,):
    print('='*30)
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f'CONTAGEM DE {a} ATÉ {b} DE {c} EM {c}')
    if a > b :
        for c in range (a,b-1,-c):
            #time.sleep(0.5)
            print(c,end=' ')
    else:
        for c in range(a,b+1,c):
            #time.sleep(0.5)
            print(c,end=' ')
    print('FIM')

contagem(1,10,1)
contagem(10,0,2)
print('AGORA É SUA VEZ  DE PERSONALIZAR A CONTAGEM:')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a,b,c)