pessoas = list()
ppes = list()
plev = list()
cont = 0
while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(int(input('Digite o peso: ')))
    if pessoas[1] >= 100:
        ppes.append(pessoas[:])
    elif pessoas[1] <= 70:
        plev.append(pessoas[:])
    cont += 1
    pessoas.clear()
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break

print(pessoas)
print(f'Total de pessoas cadastradas: {cont}')
print(f'Pesadas: {ppes}')
print(f'leves; {plev}')