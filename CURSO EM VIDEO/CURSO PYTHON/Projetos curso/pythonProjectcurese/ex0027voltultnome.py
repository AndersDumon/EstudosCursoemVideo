nc = str(input('digite o seu nome completo')).strip()
nom = nc.split()
print('seu primeiro nome é :',nom[0])
print('seu ultimo nome é : {}'.format(nom[len(nom)-1]))