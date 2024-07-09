print('Valor do produto\nComo você gostaria de fazer o seu pagamento?')
valor = float(input('Digite o valor R$ : '))
print('Agora digite a forma de pagamento ')
print('A vista no dinheiro digite (1)\na vista no cartão digite   (2)\nem até 2x no cartão digite (3)\n3x ou mais no cartão digite(4)')
fp = float(input('A vista no dinheiro digite: '))
if fp == 1:
    print('O valor fica R${:.2f}, com desconto de 10%'.format(valor-(valor*10/100)))
elif fp == 2:
    print('O valor fica R${:.2f}, com desconto de 5%'.format(valor-(valor*5/100)))
elif fp == 3:
    print('O valor de R${:.2f}, em 2x de R${:.2f} '.format(valor,valor/2))
elif fp == 4:
    par = int(input('Em quantas vezes você gostaria de parcelar?'))
    print('''O valor de R${:.2f}, com acrécimo de 20% de juros ficará R${:.2f},
    parcelado em {} vezes, ficará R${:.2f} ao mês'''.format(valor,valor+(valor*20/100),par,(valor+(valor*20/100))/par))
elif fp > 4:
    print('Nem tente fazer gracinha!R$ ')
