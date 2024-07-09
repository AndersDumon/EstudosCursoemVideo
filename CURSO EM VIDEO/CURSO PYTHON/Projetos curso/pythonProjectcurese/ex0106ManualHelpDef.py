import time
def l(txt):
    print('='*(4+len(txt)))
    print(f'{txt}')
    print('='*(4+len(txt)))
def IH():
    while True:
     print('\033[42:30m',end='')
     l(f'    SISTEMA DE AJUDA pyHELP ')
     time.sleep(1)
     a = str(input(f'\033[mfunção ou biblioteca > ')).lower().strip()
     if a == 'fim':
         break
     print('\033[44:30m')
     l(f'    Acessando o manual do comando {a}')
     time.sleep(1)
     print('\033[47:30m')
     help(a)
    print('\033[41:30m')
    l('  ATÉ LOGO VOLTE SEMPRE!')

IH()
