nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Primeiro Nome: {}\nÚltimo Nome: {}'.format(nome[0], nome[-1]))
