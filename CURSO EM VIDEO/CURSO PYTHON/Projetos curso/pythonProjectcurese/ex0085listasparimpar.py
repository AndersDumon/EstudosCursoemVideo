numeros = list()
nu1=list()
nu2=list()
for nu in range(1,8):
    num = int(input(f'DIGITE O {nu}° NUMERO: '))
    if (num % 2) == 0:
        nu2.append(num)
    elif (num % 2) == 1:
        nu1.append(num)
numeros.append(nu2[:])
numeros.append(nu1[:])
print(f'Valores pares: {sorted(numeros[0])}')
print(f'Valores impares: {sorted(numeros[1])}')
print(numeros)