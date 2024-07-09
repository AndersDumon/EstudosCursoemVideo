from datetime import date
print('*=*'*70)
print('\033[34mConfederação de natação\033[m')
ano =int(input('digite o ano que você nasceu: '))
print('*=*'*70)
anat= date.today().year
idade = anat - ano
if idade <= 9:
    print('você tem {} CATEGORIA:\033[33mMirim'.format(idade))
elif idade <= 14:
    print('você tem {} CATEGORIA:\033[33mInfantil'.format(idade))
elif idade <= 19:
    print('você tem {} CATEGORIA:\033[33mJunior'. format(idade))
elif idade <= 20:
    print('você tem {} CATEGORIA:\033[33mSênior'. format(idade))
elif idade > 20:
    print('você tem {} CATEGORIA:\033[33mMaster'. format(idade))

