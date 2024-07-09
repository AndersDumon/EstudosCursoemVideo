media = {'Nome':'aluno','Média':00,'Situação':'nulo'}
media['Nome'] = str(input('NOME DO ALUNO: '))
media['Média'] = float(input(f'Média de {media["Nome"]}:'))
if media['Média'] >= 7:
    media['Situação'] = '\033[34mAprovado\033[m'
elif media['Média'] >= 5 and media['Média']<= 6.9 :
    media['Situação'] = '\033[33mRecuperação\033[m'
else:
    media['Situação'] ='\033[31mReprovado\033[m'
print('='*40)
print(f'Nome do Aluno: {media["Nome"]}')
print(f'Média do Aluno: {media["Média"]}')
print(f'Situação: {media["Situação"]}')
print('='*40)
print('FIM DO PROGRAMA...')