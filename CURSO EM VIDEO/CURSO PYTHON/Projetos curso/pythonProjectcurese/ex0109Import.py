from ex109 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {(moeda.dobro(p,True))}')
print(f'Aumentando 10%, temos {(moeda.aument10(p,True))}')
print(f'Reduzindo 13%, temos {(moeda.dimi13(p,True))} ')