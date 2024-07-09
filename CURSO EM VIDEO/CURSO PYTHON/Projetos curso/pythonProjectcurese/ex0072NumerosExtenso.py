numeros = (
'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
r = ''
while r != 'N':
    valor = int(input('Digite um valor de 0 a 20: '))
    if valor > 20 or valor < 0:
        while True:
            print('\033[31mValor Invalido\033[m')
            valor = int(input('Digite um valor de 0 a 20: '))
            if valor >= 0 and valor <= 20:
                break
    print('O valor escolhido foi: ',end='')
    print(numeros[valor])
    r = str(input('Você gostaria de continuar?[S/N]')).upper()



