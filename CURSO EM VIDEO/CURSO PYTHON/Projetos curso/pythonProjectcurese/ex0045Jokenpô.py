import random
from time import sleep
print('\033[35m#\033[m'*60)
print('\033[36mVamos jogar JOKENPÔ?!')
print('(0)PEDRA\n(1)PAPEL\n(2)TESOURA\n ')
print('\033[35m#\033[m'*60)
item = ('pedra','papel','tesoura')
aps = int(input('QUAL VOCÊ ESCOLHE?: '))
print('\033[35m#\033[m'*60)
pc = random.randint(0,2)
print('\033[36mJO..')
sleep(1)
print('..KEN..')
sleep(1)
print('   ...PÔ!')
print('\033[33mVocê ({})\033[m X\033[32m ({}) Maquina \033[m'. format(aps,pc))
print('\033[35m#\033[m'*60)
if aps == 0 and pc == 2:
    print('\033[33mGanhou,Pedra ganha de Tesoura')
    if aps == 1 and pc == 0:
        print('\033[33mGanhou,Papel ganha de Pedra ')
    elif aps == 2 and pc == 1:
        print('\033[33mGanhou, Tesoura ganha de Papel')
    elif aps == 2 and pc == 0:
        print('\033[32mPerdeu,Tesoura perde de Pedra')
    elif aps == 0 and pc == 1:
        print('\033[32mPerdeu,Pedra perde de Papel')
    elif aps == 1 and pc == 2:
        print('\033[32mPerdeu,Papel perde de Tesoura ')
    elif aps == pc:
        print('Empate!')
else:
    print('\033[31m NÃO TENTE TRAPACEAR!')
print('\033[35m#\033[m'*60)
