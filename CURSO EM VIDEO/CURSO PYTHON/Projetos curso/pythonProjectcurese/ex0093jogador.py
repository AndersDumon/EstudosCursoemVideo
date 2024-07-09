jogador = dict()
gol1 = list()
numero = 0
print('*'*70)
jogador['Nome'] = str(input('Nome do jogador: ')).upper()
jogos = int(input(f'Quantos jogos o {jogador["Nome"]} jogou?'))
for g in range(1,jogos+1):
    gol = int(input(f'quantos gols na partida {g}: '))
    numero +=gol
    gol1.append(gol)
jogador['Gols'] = gol1
jogador['Total'] = numero
print('*'*70)
print(jogador)
print('*'*70)
for k,v in jogador.items():
    print(f'O CAMPO DO {k} TEM {v}')
print('*'*70)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas:')
for v,i in enumerate(gol1):
    print(f'Na partida {v+1}, fez {i} gols')
print(f'Foi um total de {numero} Gols')
print('*'*70)