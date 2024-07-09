from time import sleep
def maior(*num):
    print('-=-'*20)
    print('Analisando os valores passados...')
    for c in num:
        sleep(0.5)
        print(f'{c}',end=' ')
    print (f'Foram informados {len(num)} valores ao todo')
    if len(num) == 0:
        print('Não existe valor')
    else:
        print(f'o maior numero informado foi {max(num)}.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
maior(1,4,4,45,8,87,525,7,85,87,858,78,788,788,887)