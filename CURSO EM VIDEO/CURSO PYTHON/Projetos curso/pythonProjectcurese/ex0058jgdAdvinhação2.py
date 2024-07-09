import random
print('\033[35m#'*70)
print('\033[32mVamos tentar adivinhar de novo!\033[m')
t= 15
pc = random.randint(0,10)
con = 0
print('\033[35m#'*70)
while t != pc:
    n = int(input('\033[32mQue numero, estou pensando de 1 a 10? : '))
    pc = random.randint(0, 10)
    t = n
    if t != pc:
        con +=1
    print('\033[31mErrou!\033[mEstava pensando no numero \033[31m{}\033[m \nHahaha!\nTenta de novo'.format(pc))
else:
    print('\033[33mUffa! \nAcertou dessa vez!')
print('#'*70)
print('\033[35mVocê tentou {} vezes!'.format(con))
print('#'*70)