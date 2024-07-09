from ex107 import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {Moeda.metade(p)}')
print(f'O dobro de {p} é {Moeda.dobro(p)}')
print(f'Aumentando 10%, temos {Moeda.aument10(p)}')
print(f'Reduzindo 13%, temos {Moeda.dimi13(p)} ')
