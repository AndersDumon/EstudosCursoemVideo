fra = str(input('Escreva uma frase')).strip().upper()
se = fra.split()
ju = ''.join(se)
inv = ''
for letra in range(len(ju)-1,-1,-1):
#    print(ju[c],end='') #[O join junta a frase]
    inv += ju[letra]
print(ju,inv,end='')
if ju == inv:
    print('\né um palindromo')
else:
    print('\nNão é um palindromo')
