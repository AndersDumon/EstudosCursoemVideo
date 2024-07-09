print('='*70)
print('Sequencia de fibonacci')
print('='*70)
nu =int(input('numeros elemento da sequencia: '))
print('='*70)
s = 0
s1 = 1
print(s,s1,end=' ')
cont = 3
while cont != nu+1:
    s2 = s1+s
    print(s2,end=' ')
    s = s1
    s1 = s2
    cont +=1
print('>Fim')
print('='*70)