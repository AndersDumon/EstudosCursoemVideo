numeros=list()
nu1 = list()
nu2 = list()
nu3 = list()
par = 0
impar = 0
maior = 0
for nu in range(0,3):
    nu1.append(int(input(f'valor de [0, {nu}]: ')))
    numeros.append(nu1[:])
    nu1.clear()
for nuu in range(0,3):
    nu2.append(int(input(f'valor de [1, {nuu}]: ')))
    numeros.append(nu2[:])
    nu2.clear()
for n in range(0,3):
    nu3.append(int(input(f'valor de [2, {n}]: ')))
    numeros.append(nu3[:])
    nu3.clear()
print('\033[34m#\033[m'*40)
print(f'\033[33m[  {numeros[0][0]}  ][  {numeros[1][0]}  ][  {numeros[2][0]}  ]')
print(f'[  {numeros[3][0]}  ][  {numeros[4][0]}  ][  {numeros[5][0]}  ]')
print(f'[  {numeros[6][0]}  ][  {numeros[7][0]}  ][  {numeros[8][0]}  ]\033[m')
print('\033[34m#\033[m'*40)
for p in numeros:
 if  (p[0] % 2) == 0:
     par += p[0]
 else:
     impar = p
print(f'A SOMA DOS VALORES PARES: {par}')
print(f'A SOMA DOS VALORES DA 3° COLUNA: {numeros[2][0]+numeros[5][0]+numeros[8][0]}')
mai = numeros[3][0], numeros[4][0], numeros[5][0]
for m in mai:
    if m > maior:
        maior = m
print(f'O MAIOR NUMERO DA 2° LINHA: {maior}')
print('\033[34m#\033[m'*40)