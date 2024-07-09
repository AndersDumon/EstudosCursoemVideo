s = 0
n =0
cont = 0
print('Digite [999] se quiser  parar')
while n != 999:
    n = int(input('Digite um numero inteiro:'))
    if n != 999:
       cont += 1
       s +=n
print('A soma dos valores digitado foi {},\nforam digitados {} vezes'.format(s,cont))

