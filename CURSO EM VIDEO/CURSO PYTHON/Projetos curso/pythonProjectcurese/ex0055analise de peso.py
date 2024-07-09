pesado = 0
leve = 0
for p in range(1,6):
    peso = float(input('digite o seu peso da {}° pessoa'.format(p)))
    if p == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print('o maior peso é {}\nO menor peso é {}'.format(pesado,leve))