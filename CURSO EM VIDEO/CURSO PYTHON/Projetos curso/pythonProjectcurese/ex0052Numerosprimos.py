print('\033[34mNUMEROS PRIMOS\033[m')
n = int(input('digite um numero:'))
tot = 0
for c in range(1,n+1):
     if n % c == 0 :
          print('\033[33m',end='')
          tot+=1
     else:
         print('\033[31m',end='')
     print(c,end=' ')
print('\n\033[36mO número {}, foi divisivel {} vezes'.format(n,tot))
if tot == 2:
     print('Ele é um numero primo')
else:
     print('\033[31mEle não é um numero primo')