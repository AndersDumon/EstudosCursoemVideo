ini = int(input('Qual é o primeiro termo?: '))
ra = int (input('Qual é a Razão da P.A.: '))
de = ini + (10-1) * ra
for c in range(ini,de+1,ra):
    print(c,end=' ')
print('\nFim da P.A.')