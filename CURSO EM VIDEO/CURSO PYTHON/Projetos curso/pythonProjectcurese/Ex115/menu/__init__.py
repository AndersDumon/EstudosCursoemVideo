from time import sleep
from Ex115.cev.arquivo import *
ar ='Pessoa.txt'
#sequenciadecriaraquivo(ar)
def menu():
    while True:
        print('='*40)
        print(f'{"Menu principal":>25}')
        print('='*40)
        print('\033[33m1\033[m - \033[34mVER PESSOA CADASTRADA\033[m')
        print('\033[33m2\033[m - \033[34mCADASTRAR NOVA PESSOA\033[m')
        print('\033[33m3\033[m - \033[34mSAIR DO SISTEMA\033[m')
        print('='*40)
        try:
            resp = int(input('SUA OPÇÃO: '))
            if resp == 3:
                break
            if resp == 1:
                lerAquivo(ar)
            elif resp == 2:
                print('=' * 40)
                print(f'{"CADASTRAR NOVA PESSOA":>30}')
                print('=' * 40)
                nome = input('Nome: ').strip()
                if not nome.isalpha():
                    while True:
                        nome = input('Nome: ').strip()
                        if nome.isalpha():
                            break
                idade = input('Idade: ').strip()
                if not idade.isnumeric():
                    while True:
                        idade = input('Idade:').strip()
                        if idade.isnumeric():
                            break
                cadastrar(ar,nome,idade)
            else:
                print('\033[31mOpção Invalida\033[m',end=' ')
                print('\033[34mDigite Novamente!\033[m')
        except:
            print('\033[31mValor invalido\033[m',end=' ')
            print('\033[34mDigite Novamente!\033[m')
        sleep(2)
    print(f'\033[33mOBRIGADO POR USAR O NOSSO SOFTWARE!\n{"VOLTE SEMPRE!":>23}\033[m')
