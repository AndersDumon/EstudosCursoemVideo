from time import sleep
from Ex115.cev.arquivo import *
from Ex115.cev import *
arq = 'cevideo.txt'

if arquivoExiste(arq):
    print('Arquivo existe!')
else:
    print('Arquivo não exisite')
    criarAquivo(arq)

while True:
    resposta = menu(['VER PESSOAS CADASTRADAS','CADASTRAR NOVA PESSOA','SAIR  DO SISTEMA'])
    if resposta == 1:
        # opção de listar conteúdo de um aquivo
        lerAquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar (arq, nome, idade)
    elif resposta == 3:
        cabecalho('SAINDO DO SISTEMA')
        break
    else:
        print('ERRO, DIGITE UMA OPÇÃO VALIDA.')
    sleep(2)

