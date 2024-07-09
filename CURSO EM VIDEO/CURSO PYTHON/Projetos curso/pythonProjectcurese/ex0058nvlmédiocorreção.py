import random
print('\033[35m#'*70)
print('\033[32mVamos tentar adivinhar de novo!\033[m')
acertou = False
pc = random.randint(0,10)
con = 0
print('\033[35m#'*70)
while not acertou:
    n = int(input('\033[32mQue numero, estou pensando de 1 a 10? : '))
    con +=1
    if n == pc:
        acertou = True
        print('\033[33mUffa! \nAcertou dessa vez!')
    else:
        if n < pc:
            print('\033[31mErrou!\033[mEstava pensando no numero \033[31mMaior\033[m \nHahaha!\nTenta de novo')
        elif n > pc:
            print('\033[31mErrou!\033[mEstava pensando no numero \033[31mMenor\033[m \nHahaha!\nTenta de novo')
print('#'*70)
print('\033[35mVocê acertou com {} tentativas!'.format(con))
print('#'*70)