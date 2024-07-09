print(' Média do aluno')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
if m >= 7.0:
    print('\033[34mParabéns, você foi Aprovado com a média de {:.1f}'.format(m))
elif m > 5.1 < 6.9:
    print('\033[33mVocê está de Recuperação com a média de {:.1f}'.format(m))
elif m <= 5.0:
    print('\033[31mQue pena! você foi Reprovado com a média de {}'. format(m))