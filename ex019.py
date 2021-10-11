import random
n1 = input('Digite o nome do aluno nº1: ')
n2 = input('Digite o nome do aluno nº2: ')
n3 = input('Digite o nome do aluno nº3: ')
n4 = input('Digite o nome do aluno nº4: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido para apagar o quadro é: {}'.format(escolhido))
