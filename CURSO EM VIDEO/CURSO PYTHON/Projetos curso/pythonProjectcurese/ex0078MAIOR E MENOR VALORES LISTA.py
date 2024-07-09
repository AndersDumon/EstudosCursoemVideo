v = []
c = maior = 0
for contagem, val in enumerate(range(0,5)):
    v.append(int(input(f'Digite um valor para posição:\033[33m{contagem}\033[m: ')))
print(f'Os valores que você digitou foi \033[32m{v}\033[m')
print(f'O maior valor digitado foi \033[32m{max(v)}\033[m na posição \033[33m{v.index(max(v)), v.index(max(v), 1)}\033[m')
print(f'O menor valor digitado foi \033[32m{min(v)}\033[m na posição \033[33m{v.index(min(v),v.index(min(v),1))}\033[m')
