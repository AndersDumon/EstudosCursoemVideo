def notas(*num,sit=False):
    """
    -->FUNÇÃO PARA ANALISAR  NOTAS E SITUAÇÕES DE VARIOS ALUNOS.
    :param num: UMA OU MAIS NOTAS DE ALUNOS (ACEITA VÁRIAS)
    :param sit: VALOR OPCIONAL,INDICANDO SE DEVE OU NÃO ADICIONAR A SITUAÇÃO
    :return:DICIONÁRIO COM VÁRIAS INFORMAÇÕES SOBRE A SITUAÇÃO DA TURMA.
    """
    resp = {'Total': 0, 'Maior': 0, 'Menor': 0, 'Média': 0,'Situação':''}
    tot =sum(num)
    resp['Maior']=ma =max(num)
    resp['Menor']=me =min(num)
    resp['Total']=tota = len(num)
    resp['Média']=med = tot/tota
    if sit == True:
        if med > 7:
            resp['Situação'] = 'Aprovado'
        elif 5 < med < 7:
            resp['Situação'] = 'Recuperação'
        else:
            resp['Situação'] = 'Reprovado'
    else:
        del resp['Situação']
    return resp

resp = notas(5.5,9.5,10,6.5,sit=True)
resp1 = notas(5,4,1,7,sit=True)
resp2 = notas(5,5,6,6,sit=True)
resp3 = notas (10,10,10,5)
print(resp)
print(resp1)
print(resp2)
print(resp3)
help(notas)
