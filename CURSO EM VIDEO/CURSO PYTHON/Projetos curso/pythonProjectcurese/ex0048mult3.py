s=0
cont = 0
print('multiplo de três de 1 a 500')
for c in range(1,500+1,2):
    if c % 3 == 0 :
        cont +=1
        s = s + c
print('Os numeros contados foi {}'.format(cont))
print('A soma dos multiplos é {}'.format(s))

