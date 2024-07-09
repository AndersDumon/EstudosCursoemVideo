from datetime import date
dados = dict()
dados['NOME'] = str(input('Nome: '))
nacs = int(input('Data de Nascimento: '))
anoatual = date.today().year
idade1 = anoatual - nacs
dados['IDADE'] = idade1
dados['CTPS'] = int(input('Carteira de Trabalho ([0] não tem): '))
if dados['CTPS'] <= 0:
    dados['CTPS'] = 'NÃO TEM CTPS'
else:
    ancon = int(input('ANO DE CONTRATAÇÃO:'))
    aposentadoria = (ancon - nacs) + 35
    dados['Contratação'] = ancon
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = aposentadoria
print('='*50)
for k,v in dados.items():
    print(f'{k:<5}:  {v}')
print('='*50)