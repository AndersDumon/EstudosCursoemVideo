from datetime import date
anat = date.today().year
s = 0
me = 0
for c in range(0,7):
    ano = int(input('digite o ano do seu nascimento:'))
    idade = anat - ano
    if idade > 21:
        s += 1
        print('{} você é de maior'.format(idade))
    elif idade < 21:
        me += 1
        print('{} você é de menor'.format(idade))
print('Existem {} de Maior idade e {} de Menor idade'.format(s,me))