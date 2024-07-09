v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite mais um valor: '))
v4 = int(input('Digite novamente um valor: '))
lista = (v1,v2,v3,v4)
print(f'Você digitou esses números: {lista}')
print(f'O numero 9 apareceu: {lista.count(9)} vezes')
if v1 and v2 and v3 and v4 != 3:
    print('O numero 3 não foi digitado nenhuma vez!')
else:
    print(f'O numero 3 apareceu na posição: {(lista.index(3))+1}')
print('Valores pares = ',end=' ')
for par in lista:
    if (par % 2) == 0:
       print(par,end=' ')

print('\n')
# outra forma de fazer a tupla
n = (int(input('Digite uma valor')),int(input('Digite uma valor')),
int(input('Digite uma valor')),int(input('Digite uma valor')))
print(n)