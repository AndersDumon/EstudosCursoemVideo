alun = {'nome':'','nota':0, 'nota 2':0,'média': 0}
nome = str(input('qual é o seu nome ?')).lower()

if nome == 'anderson':
    print(f'Seja bem vindo {nome}.')
    print('Agora digite o nome e  as notas dos alunos')
    while True:
        alun['nome'] = str(input('Nome do aluno:'))
        n1 = float(input(f'Primeira nota {alun['nome']}: '))
        alun['nota']= n1
        n2 = float(input(f'Segunda nota {alun['nome']}: '))
        alun['nota 2'] = n2
        m = (n1 + n2) / 2
        alun['média'] = m
        print(f'O aluno {alun['nome']} teve a média de {m}')
        print(alun)
else:
    print('não te conheço')

