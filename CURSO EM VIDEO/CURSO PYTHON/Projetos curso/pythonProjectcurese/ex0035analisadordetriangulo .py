print('Analisador de triângulo!')
r1 = float(input('qual o valor da reta?'))
r2 = float(input('qual o valor da outra reta?'))
r3 = float(input('qual o valor da terceira reta?'))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
  print('Pode formar um triângulo!')
#'''if r2 + r3 > r1
 #   print('é um triângulo!')
#if r3 + r1 > r2:
 #   print('é um triângulo!')'''
else:
    print('Não pode formar um triângulo!')