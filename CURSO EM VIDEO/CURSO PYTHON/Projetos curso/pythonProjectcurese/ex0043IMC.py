print('IMC')
alt = float(input('Diga a sua altura:'))
pes = float(input(' diga seu peso:'))
imc = pes/ (alt*alt)
if imc <= 18.5:
    print('Voce esta abaixo do peso, peso = {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Voce esta no peso ideal, peso = {:.1f}'.format(imc))
elif imc >=25 and imc < 30:
    print('sobrepeso, peso = {:.1f}'. format(imc))
elif imc >= 30 and imc < 35:
    print('Obesidade grau I, peso ={:.1f}'. format(imc))
elif imc >=35 and imc < 40:
    print('Obesidade grau II, peso = {:.1f}'. format(imc))
elif imc >= 40:
    print ('Obesidade grau III, peso = {:.1f}'. format(imc))