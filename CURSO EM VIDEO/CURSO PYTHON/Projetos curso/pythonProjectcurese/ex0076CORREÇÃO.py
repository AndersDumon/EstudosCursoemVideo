mercado = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,
           'Traferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',
           22.30,'Livro',34.90)
print('='*40)
print(f'\033[32m{"LISTA DE PREÇOS":^40}\033[m')
print('='*40)
for pos in range(0,len(mercado)):
    if pos % 2 == 0:
        print(f'{mercado[pos]:.<30}',end='')
    else:
        print(f'R${mercado[pos]:>7}')
print('='*40)