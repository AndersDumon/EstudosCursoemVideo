import random
nu1 = int(random.randint(0,9))
nu2 = int(random.randint(0,9))
nu3 = int(random.randint(0,9))
nu4 = int(random.randint(0,9))
nu5 = int(random.randint(0,9))
lista = (nu1,nu2,nu3,nu4,nu5)
maior = 0
menor = 10
print(lista)
for numero in lista:
 if numero > maior:
     maior = numero
for numero in lista:
    if numero < menor:
        menor = numero
print(f'O maior numero sorteado é : {maior}')
print(f'O menor numero sorteado é : {menor}')

# MAIS DE UMA FROMA DE FAZER
nu6 = (random.randint(1,10)),(random.randint(1,10)), (random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10))
print(nu6)
print(max(nu6))
print(min(nu6))