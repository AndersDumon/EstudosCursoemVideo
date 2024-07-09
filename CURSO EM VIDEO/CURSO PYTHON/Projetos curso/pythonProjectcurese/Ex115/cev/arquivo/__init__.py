from Ex115.cev import *

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um Erro na criação do arquivo!')
    else:
        print(f'Aquivo {nome} criado com sucesso!')


def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro em abrir o aquivo ')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<25}{dado[1]:>3} anos')
    finally:
        a.close()


def sequenciadecriaraquivo(nome):
    if arquivoExiste(nome):
        print('existe')
    else:
        print('não existe')
        criarAquivo(nome)

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de cadastrar os dados!')
        else:
            print(f'novo registro de {nome} adicionado')
            a.close()