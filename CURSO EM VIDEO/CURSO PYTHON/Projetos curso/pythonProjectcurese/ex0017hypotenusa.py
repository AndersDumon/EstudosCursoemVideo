from math import hypot
print('='*70)
print('A soma da hipotenusa de um quadrado retangulo')
n1 = float(input('digite o cateto oposto'))
n2 = float(input('digite o cateto adjacente'))
hy = hypot(n1,n2)
print('o valor da Hipotenusa é: {:.2f}'.format(hy))
'''
(Tabém poderia ser feito assim sem importmath)

co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))

hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print("\n**************************\n")

print("O valor da hipotenusa é: {}".format(hipotenusa))'''
