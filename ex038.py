n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O \033[1mprimeiro valor\033[m ({}) é maior que o segundo.'.format(n1))
elif n2 > n1:
    print('O \033[1msegundo valor\033[m ({}) é maior que o primeiro.'.format(n2))
else:
    print('Não existe valor maior, \033[1mos dois valores inseridos são iguais.')