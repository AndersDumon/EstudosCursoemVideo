print(' emprestimo do seu imóvel')
casa = float(input('Qual é o valor do imóvel?R$'))
salario = float(input('Qual é o valor do seu salário?R$'))
anos = int(input('Em quanto anos você gostaria de pagar?'))
mes = anos * 12
cal = casa/mes
res = (salario*30)/100
if cal < res:
    print('\033[33mo valor ficara {:.2f} ao mês\nEMPRÉSTIMO CONCEDIDO\033[m'.format(cal))
else:
    print('\033[31mDesculpe, EMPRÉSTIMO NEGADO\nNão será possivel fazer o emprestimo,\nPois o valor ultrapassa 30% do seu salário \no seu emprestimo ficaria R${:.2f}\033[m'.format(cal))