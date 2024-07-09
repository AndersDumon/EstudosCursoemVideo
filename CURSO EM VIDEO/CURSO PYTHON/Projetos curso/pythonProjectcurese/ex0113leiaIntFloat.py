def leiaint(n):
    try:
        n  = int(input('Digite um valor Inteiro: '))
    except (ValueError,TypeError,TabError):
        while True:
            print('\033[31mInfelismente houve uma falha no valor!\033[m')
            n = input('digite um numero Inteiro: ').strip()
            if n.isnumeric():
                break
    except KeyboardInterrupt:
        print('\nO usuario preferiu não digitar!')
        return 0
    else:
        return n
    return n



def leiafloat(n):
    while True:
        try:
            n = float(input('Digite um numero Real: '))
        except(ValueError,TypeError,TabError):
                print('\033[31mInfelismente houve uma falha no valor\033[m')
                continue
        except KeyboardInterrupt:
            print('\nO usuario preferiu não digitar!')
            return 0
        else:
            return n



n = leiaint('Digite um valor: ')
n1 = leiafloat('Digite um valor: ')
print(f'Os valores digitados foram {n} Inteiro e {n1} Real')
