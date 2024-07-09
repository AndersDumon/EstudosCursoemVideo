proba = r = prod =''
item = bara = mac = tot = preco = 0
print('='*30)
print('Lojas Monte:')
print('='*30)
while r != 'N':
    prod = str(input('Nome do produto: ')).upper().strip()
    preco = float(input('Preço: '))
    r = str(input('Quer continuar[S/N]:')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    tot += preco
    item +=1
    if preco > 1000:
        mac += 1
    if item == 1:
        bara = preco
        proba = prod
    else:
        if preco < bara:
            bara = preco
            proba = prod
print(f'Foram registrados {item} itens\nTotal da compra: {tot}')
print(f'Exitem {mac} maiores que R$1.000\nO porduto mais barato é {proba} que custa {bara}')