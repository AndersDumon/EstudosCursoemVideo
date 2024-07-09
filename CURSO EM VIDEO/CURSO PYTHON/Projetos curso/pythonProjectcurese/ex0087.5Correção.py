martriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0,3):
        martriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
for l in range (0,3):
    for c in range(0,3):
        print(f'[{martriz[l][c]:^5}]',end='')
        if martriz[l][c] %2 == 0:
            spar += martriz[l][c]
    print()
print(f'A SOMA DOS VALORES PARES É {spar}')
for l in range (0,3):
    scol += martriz[l][2]
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA {scol}')
for c in range(0, 3):
    if c == 0:
        mai = martriz[1][c]
    elif martriz[1][c] > mai:
        mai = martriz[1][c]
print(f'O MAIOR VALOR DA SEGUNDA LINHA É {mai}')