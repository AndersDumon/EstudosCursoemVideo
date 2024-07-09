
def ficha(j,n):
    if len(n) == 0:
        n = 0
    elif not n.isnumeric():
        n = 0
    if len(j) == 0:
       j =('<desconhecido>')
    print(f'O jogador {j}, fez {n} gol(s)'
          f' no campeonato.')

j = str(input('DIGITE O NOME DO JOGADOR: ')).upper().strip()
n = str(input('Digite quantos gols: '))
ficha(j,n)