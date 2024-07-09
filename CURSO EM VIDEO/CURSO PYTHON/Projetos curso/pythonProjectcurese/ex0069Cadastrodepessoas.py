sex=r = ''
mume=hom=maior=ida = 0
while r != 'N':
    print('='*40)
    print('CADASTRE UMA PESSOA')
    print('='*40)
    ida = int(input('Idade:'))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    while sex not in 'FfMm':
        print('\033[31mSexo Invalido!\033[m')
        sex = str(input('Digite o Sexo novamente![M/F]: '))
    print('-' * 40)
    r = str(input('Quer continuar?[S/N]: ')).strip().upper()
    while r not in 'sSnN':
        print('Valor Invalido!')
        r = str(input('Quer continuar?[S/N]: '))
    if ida > 18:
        maior += 1
    if sex == 'M':
        hom += 1
    if sex == 'F' and ida < 20:
         mume +=1
print('='*40)
print('Terminando o Resgistro')
print('-' * 40)
print(f'''Total de pessoas maior de 18 anos: {maior}
Ao todo foram registrados:
{hom} Homens e temos {mume} mulheres com menos de 20 anos ''')
print('-' * 40)