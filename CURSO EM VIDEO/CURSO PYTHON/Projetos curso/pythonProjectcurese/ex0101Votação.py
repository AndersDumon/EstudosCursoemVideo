def voto(ano=2024):
    from datetime import date
    anat = date.today().year
    ida = anat - ano
    if ida >= 65 :
        op = (f'Com {ida} anos = Voto é opcional')
        return op
    elif ida < 16:
        op = (f'Com {ida} anos = Não pode votar')
        return op
    elif ida >16 and ida < 18:
        op = (f'Com {ida} anos = Voto é opcional')
        return op
    else:
        op = (f'Com {ida} anos = Voto é obrigatório')
        return op


ano = int(input('digite o ano do seu nascimento: '))
print(voto(ano))
