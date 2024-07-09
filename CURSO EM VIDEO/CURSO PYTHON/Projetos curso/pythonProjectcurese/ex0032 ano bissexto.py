from datetime import date
ano = int(input('digite o ano , para saber o ano atual digite 0: '))
'''#div = ano % 4'''
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bisexto'.format(ano))
else:
    print('o ano {} não é bisexto'.format(ano))