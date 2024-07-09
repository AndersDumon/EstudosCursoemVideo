def leiaint(txt):
    try:
        n  = int(input(txt))
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


def linha(tam=42):
    return '='*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu Principal')
    c=1
    for item in lista:
        print(f'{c} - {item} ')
        c+=1
    print(linha())
    opc = leiaint('Sua opção:')
    return opc