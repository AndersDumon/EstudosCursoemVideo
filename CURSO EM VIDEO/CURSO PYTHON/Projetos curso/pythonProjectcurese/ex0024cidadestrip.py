print('='*70)
print('Digite o nome da sua cidade para saber se começa com Santo')
print('='*70)
no = str(input('Digite o nome :')).strip()
nom = no.upper()
nem = (nom[0:5])
print('='*70)
print('se é [true]= começa \nou\nse for [false]= não começa ')
print('='*70)
print('SANTO'in nem)
''' cid = str(input('digite um nome')).strip()
print([:5].upper() == 'santos')'''