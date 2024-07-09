pessoas =list()
ppes = list()
plev = list()
cont = 0
mai = 0
men = 999
while True:
    pessoas.append(str(input('NOME: ')))
    pessoas.append(int(input('PESO: ')))
    cont +=1
    if cont == 0:
        men = mai = pessoas[1]
    elif pessoas[1] > mai:
        mai = pessoas[1]
    elif pessoas[1] < men:
        men = pessoas[1]
    if pessoas[1]>= mai :
        ppes.append(pessoas[:])
    elif pessoas[1]<= men :
        plev.append(pessoas[:])
    pessoas.clear()
    r = str(input('QUER CONTINUAR [S/N]:'))
    if r in 'Nn':
        break
print(f'Ao todo foram registrados : {cont} pessoas')

print(f'O Menor peso foi de {men}KG. PESO DE ',end=' ')
for p in plev:
    if p[1] == men:
        print(f'{p[0]}')
print(f'O Maior peso foi de de {mai}KG. PESO DE ',end=' ')
for p2 in ppes:
    if p2[1] == mai:
        print(f'{p2[0]}')
