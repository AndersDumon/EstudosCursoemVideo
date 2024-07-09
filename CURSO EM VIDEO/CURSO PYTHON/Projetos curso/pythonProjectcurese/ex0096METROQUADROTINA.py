def area():
   ar = a * b
   print(f'{ar:.1f}m². ')
def l ():
   print('='*40)

#programa principal
print('CONTROLE DE TERRENOS')
l()
a = float(input('Largura(m): '))
b = float(input('Comprimento(m): '))
print(f'Á AREA DE UM TERRENO DE {a}x{b} É DE ',end='')
area()
l()