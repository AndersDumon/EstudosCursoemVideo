'''print('Digite o seu sexo: ')
s = str(input('[M/F]')).strip().upper()[0]
if s != 'M' and s!= 'F':
    print('Valor invalido,por favor seu sexo! ')
    while s != 'M' and s != 'F':
        s = str(input('[M?F]')).upper()
        print('Valor Invalido!')
    else:
        print('Agora, sim valor valido')
print('fim')'''
#correção############
sexo = str(input('Informe o seu sexo [M/f]:')).strip().upper()[0]
while sexo not in 'FfmM':
    sexo = str(input('informe o seu sexo [M/F]:')).strip().upper()[0]
print('Sexo regitrado com sucesso!')
