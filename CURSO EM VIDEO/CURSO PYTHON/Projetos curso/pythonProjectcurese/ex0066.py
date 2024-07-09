print('Digite [999] para parar! ')
n = s = cont = 0
while n != 999:
    n = int(input('Digite um valor'))
    if n ==999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números\nA soma dos valores é {s}')
