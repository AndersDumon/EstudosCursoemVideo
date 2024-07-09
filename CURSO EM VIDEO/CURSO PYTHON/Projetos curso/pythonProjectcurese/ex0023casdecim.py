print('=' * 70)
n = int(input('Digite um numero de 0 a 9999 : '))
#'''nu = n.split(),n.strip()
#print('milhas',n[0])
#print('centenas',n[1])
#print('dezenas',n[2])
#print('unidade',n[3])'''
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print('milhas  {} '.format(m))
print('centenas {} '.format(c))
print('dezenas {} '.format(d))
print('unidades {} '.format(u))
