from random import randint
import time
from operator import itemgetter
ranking = dict()
jogadores = {'\033[31mJogador 1°\033[m':randint(1,6),'\033[32mjogador 2°\033[m':randint(1,6),
             '\033[36mjogador 3°\033[m':randint(1,6),'\033[34mJogador 4°\033[m':randint(1,6)}
print('CADA JOGADOR IRÁ JOGAR UM DADO...\n...VAMOS VER QUEM SERA O VENCEDOR?')
time.sleep(3)
print(' \033[33mQUE COMECEM OS JOGOS!\033[m')
print('='*40)
for v,d in jogadores.items():
    time.sleep(1)
    print(f'{v} tirou {d} no dado.')
print('='*40)
print('=======>\033[35mRANKING DOS JOGADORES\033[m<=======')
ranking = sorted(jogadores.items(), key=itemgetter(1),reverse=True)
cont = 1
for k , v in ranking:
    time.sleep(1)
    print(f'{cont}°LUGAR O {k} tirou: {v} ')
    cont +=1



