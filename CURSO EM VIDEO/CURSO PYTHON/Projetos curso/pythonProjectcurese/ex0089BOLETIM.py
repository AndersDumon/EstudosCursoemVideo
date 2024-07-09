media = list()
nomes = list()
nota = list()
cont1 = 0
med = list()
resp = 0
while True:
    nome = str(input('Digite o nome')).upper()
    nomes.append(nome)
    n1 = float(input('digite a nota: '))
    n2 = float(input('digite a nota: '))
    nota.append(n1)
    nota.append(n2)
    m = (n1+n2)/2
    med.append(m)
    nomes.append(nota[:])
    media.append(nomes[:])
    nota.clear()
    nomes.clear()
    r = str(input('Quer continuar?')).upper()
    if r in 'Nn':
        break
print('='*30)
print(f'{"NO.":<3}|{"   NOME  ":<9} |{" MÉDIA":>11} ')
for p in media:
    print(f'{cont1:<5}{media[cont1][0]:<10}{med[cont1]:>10}')
    cont1 +=1
print('='*30)
print('DIGITE 999 PARA INTERROMPER')
while True:
    resp = int(input('Você gostaria de ver a nota de qual aluno?'))
    if resp == 999:
        print('FINALIZANDO...')
        break
    elif resp <= len(media) - 1:
        print(f'NOTAS DE {media[resp][0]} FOI: {media[resp][1]}')
print('VOLTE SEMPRE')