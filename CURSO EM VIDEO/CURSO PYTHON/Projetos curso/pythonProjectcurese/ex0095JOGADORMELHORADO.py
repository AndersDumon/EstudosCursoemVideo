jogador = dict()
cont = 0
jogadores = list()
gol =resp = 0
print('\033[34m*\033[m'*60)
while True:
    gol1 = list()
    numero = 0
    jogador['Nome'] = str(input('Nome do do jogador: ')).upper()
    jogos = int(input(f'Quantos jogos o {jogador["Nome"]} jogou?: '))
    for g in range(1, jogos+1):
        gol= int(input(f'Quantos gols foram feitos na partida {g}: '))
        numero += gol
        gol1.append(gol)
    jogador['Total'] = numero
    jogador['Gols'] = gol1
    jogadores.append(jogador.copy())
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if r in 'Nn':
        break
print('\033[34m*\033[m'*60)
print(f'{"COD.":<3}|{"   NOME  ":<9}|{"   GOLS ":>7}     |{"TOTAL DE GOLS":>8}')
for j in jogadores:
    print(f'{cont:<3}{jogadores[cont]["Nome"]:<9}       {jogadores[cont]["Gols"]}{jogadores[cont]["Total"]:>8}')
    cont += 1
print('\033[34m*\033[m'*60)
print('\033[35mDIGITE: (999) PARA INTERROMPER\033[m ')
while True:
    print('-'*60)
    resp = int(input('MOSTRAR DADOS DE QUAL JOGADOR?[DIGITE O COD.]:'))
    if resp == 999:
        break
    elif resp <= len(jogadores)-1:
        print(f'--*LEVANTAMENTO DO JOGADOR:*--*\033[33m{jogadores[resp]['Nome']}\033[m*--')
        for pat,v in enumerate(jogadores[resp]['Gols']):
            print(f'Na Partida {pat+1} = fez {v} GOL')
    else:
        print('\033[31mCod.Invalido\033[m\nNÃO EXISTE JOGADOR COM ESSE COD.')
print('\033[34m*\033[m'*60)
print('Obrigado por usar o nosso software!')
print('>>>>>>>>>>*Volte Sempre*<<<<<<<<<<<')



