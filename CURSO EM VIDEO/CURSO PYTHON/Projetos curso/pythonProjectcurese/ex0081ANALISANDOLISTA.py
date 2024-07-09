v = []
r = ''
while r != 'N' :
    v.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar ? [S/N]: ')).upper().strip()
    while r not in 'NnsS':
        print('Invalido')
        r = str(input('Quer continuar? [S/N]:')).upper().strip()
print(f'Valores digitados : {v}')
print(f'Existem {len(v)} numeros na lista')
v.sort(reverse=True)
print(f'Ordem decrecente : {v} ')
if 5 in v:
    print(f'Na lista existem o valor 5 ')
else:
    print('Não foi encontrado o numero 5')