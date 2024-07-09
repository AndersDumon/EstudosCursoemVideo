from datetime import date
print(('Alistamento'))
ano = int(input('Digite o ano que você nasceu: '))
anat = date.today().year
idade = anat - ano
if idade == 17:
    print('\033[34mVocê tem {} anos, Está no ano de você se alistar'.format(idade))
elif idade > 17:
    print('\033[31mVocê tem {} anos, já passou {} anos de se alistar , Vá buscar a sua Reservista!'.format(idade,idade-17))
    anot =anat-(idade-17)
    print(' o seu alistamento foi em {}'.format(anot))
elif idade < 17:
    print('\033[33mVocê tem {} anos, ainda não é tempo de se alistar faltam {} anos '.format(idade,17-idade))
    anoet=anat+(17-idade)
    print('o seu alistamento será em {} '. format(anoet))

