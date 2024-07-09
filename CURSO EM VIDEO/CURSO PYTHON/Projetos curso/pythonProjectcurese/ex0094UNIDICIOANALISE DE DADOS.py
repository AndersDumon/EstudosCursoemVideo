dados = dict()
dados2 = list()
cont = 0
media = 0
while True:
    nome = str(input('NOME: ')).upper().upper()
    dados['Nome'] = nome
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo not in 'MmFf':
        while sexo not in 'MmfF':
            print('\033[31mERRO Sexo Invalido\033[m')
            sexo = str(input('Porfavor Digite corretamente o sexo [M/F]:')).upper()
    dados['Sexo'] = sexo
    idade = int(input('Idade: '))
    dados['Idade'] = idade
    dados2.append(dados.copy())
    cont += 1
    media += idade
    r = str(input('Quer continuar?[S/N]: ')).upper()
    if r not in 'sSnN':
        while r not in 'sSnN':
            print('\033[31mERRO DIGITE APENAS [S/N]\033[m')
            r = str(input('Quer continuar?[S/N]: ')).upper()
            if r in 'Nn':
                break
    if r in 'Nn':
        break
m = media / cont
print('_'*50)
print(f'O GRUPO TEM {cont} PESSOAS CADASTRADAS')
print(f'A MÉDIA DE IDADE DO GRUPO É: {m:.2f} anos')
print('AS MULHERES CADATRAS:',end=' ')
for v in dados2:
    if v['Sexo'] == 'F':
        print(v['Nome'],end=', ')
print()
print('_'*50)
print('LISTA DAS PESSOAS QUE ESTÃO ACIMA DA MÉDIA:')
for me in dados2:
    if me['Idade'] > m :
        for n , e in me.items():
            print(f'{n}:{e}',end='; ')
    print()
print('_'*50)
print('<<<FIM DO PROGAMA>>>')