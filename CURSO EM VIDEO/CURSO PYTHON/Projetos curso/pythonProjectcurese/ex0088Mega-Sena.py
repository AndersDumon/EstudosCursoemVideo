import random
import time
jogo = list()
joo = list()
cont= 0
print('='*47)
print('=============\033[33mJOGO NA MEGA SENA\033[m=================')
print('='*47)
resp = int(input('Quantos jogos você gostaria que eu sorteie?: '))
for c in range(1,resp+1):
      con = 0
      while True:
        num = random.randint(1,60)
        if num not in joo:
            joo.append(num)
            con +=1
        if con >= 6:
            break
      jogo.append(joo[:])
      joo.clear()
print(f'=============\033[33mSORTEANDO {resp} NUMEROS\033[m===============')
for jog in range(1,resp+1):
       print(f'\033[32mjogo ({jog:>2})\033[m = \033[34m{sorted(jogo[cont])}\033[m')
       cont +=1
       time.sleep(0.8)
print('='*47)
print(f'=================<\033[33mBOA SORTE\033[m>===================')