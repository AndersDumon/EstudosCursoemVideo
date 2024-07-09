s = 0
s1 =0
nomes1 ='' #faltou isso
s2 =0
for pes in range(1,5):
    nome = str(input('Nome: ')).strip()
    ida = int(input('Idade: '))
    sex = str(input('Sexo:[M/F]:')).upper()
    s +=ida
    if pes == 1 and sex in 'M': #correção
        s1 = ida
        nomes1 = nome
    if sex in 'M' and ida > s1:
        s1 = ida
        nomes1 = nome
    if sex in 'F' and ida < 20:
        s2 +=1
    '''if pes == 1:                        # faltou and  sex in 'M'
        s1 = nome,ida,sex           # Não havia nesecidade de colocar : ida e sex
        if ida > ida and sex =='M':     #faltou a variavel = nomes1 
            s1 = nome,ida,sex            # deveria ser invertido
    if ida < 20 and sex =='F':
             s2 +=1'''
m = s/4
print('A média da idade é {}'.format(m))
print('o homem mais velho é {} de {}anos de idade'.format(nomes1,s1))
print('Existem {} mulheres menores de 20 anos'.format(s2))