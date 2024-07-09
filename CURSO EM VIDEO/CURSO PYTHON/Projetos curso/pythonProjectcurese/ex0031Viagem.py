print('qual a distancia da sua viagem?')
print(' se for até 200km você paga 0.50 por km')
print(' se for maior que 200km você paga 0.45 por km')
k = float(input(' digite o km para calcular o valor da sua passagem: '))
me = k * 0.50
ma = k * 0.45
if k <= 200:
    print('Você irá pagar {} reais'.format(me))
else:
    print('Voce irá pagar {} reais'.format(ma))
#ou
'''preço = k * 0.50 if k <= 200 else k *0.45
print(' o valor a pagar é {}'.format(preço))'''
