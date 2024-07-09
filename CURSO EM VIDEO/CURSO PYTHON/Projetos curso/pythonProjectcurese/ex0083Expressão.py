l = []
ex = str(input('Digite a expressão:\n '))
for simb in ex:
    if simb == '(':
        l.append('(')
    elif simb == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0 :
    print('Expressão valida!')
else:
    print('Expressão invalida!')
