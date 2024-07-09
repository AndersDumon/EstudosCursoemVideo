r = ''
soma = con = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um valor: '))
    con += 1
    soma += n
    if con == 1:
     maior = menor = n
    else:
        if n > maior:
         maior = n
         if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r != 'S' and r != 'N':
        print('\033[31mValor inexitente!\033[m')
media = soma / con
print('Numeros digitados: {}\nA soma entre os valores: {}'.format(con, soma))
print('a média é : {}'.format(media))
print('O maior é : {}, e o menor é : {}'.format(maior,menor))
