l =[]
maior=0
menor=0
for c in range (0,5):
    l.append(int(input('Digite um valor')))
    if c == 0:
        maior = menor = l[c]
    else:
        if l[c] > maior:
            maior = l[c]
        if l[c] < menor:
            menor = l[c]
print(f'Você digitou {l} ')
print(f'O MAOR VALOR DIGITADO FOI {maior} nas posições',end=' ')
for i,v in enumerate(l):
    if v == maior:
        print(i,end='...')
print()
print(f'O MENOR VALOR DIGITADO FOI {menor} na posições',end=' ')
for me,pe in enumerate(l):
    if pe == menor:
        print(me,end='...')