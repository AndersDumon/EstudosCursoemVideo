l = []
lp = []
li = []
r =''
while r != 'N':
    l.append(int(input('Digite um  valor: ')))
    r = str(input('Quer continuar?[S/N]: ')).upper().strip()
    while r not in 'NnsS':
        print('Valor invalido')
        r = str(input('Quer continuar?[S/N]: ')).upper().strip()
for num in l:
    if (num % 2 ) == 0:
        lp.append(num)
    elif (num % 2 ) == 1:
        li.append(num)
print(f'VALORES DIGITADOS : {l}')
print(f'VALORES PARES DIGITADOS: {lp}')
print(f'VALORES IMPARES DIGITADOS: {li}')