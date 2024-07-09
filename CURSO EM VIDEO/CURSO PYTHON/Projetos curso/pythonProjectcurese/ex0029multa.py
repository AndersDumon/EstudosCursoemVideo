print('-'*80)
print('Acima de 80 km, paga multa de 7 Reais, por km ultrapassado!')
print('-'*80)
print('Vamos ver se você levou uma muta?')
km = float(input( 'digite a velocidade do seu carro: ' ))
print('-'*80)
mu = (km - 80) *7
if km > 80:
    print('Você ultrapassou o limite de velocidade!\nE vai pagar uma mutlta de {} reais'.format(mu))
else:
    print('Desculpe!\nVocê não levou multa, pode continuar em frente! ' )
