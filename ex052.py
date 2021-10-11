soma = 0

n = int(input('Digite um número inteiro: '))
for i in range(1, n+1):
    if n % i == 0:
        print('\033[31m{}\033[m'.format(i), end=' ')
        soma += 1
    else:
        print(i, end=' ')
if soma > 2:
    print('\nO número {} foi dividido {} vezes, então não é primo.'.format(n,soma))
else:
    print('\nO número {} foi dividido apenas 2 vezes, então ele é primo.'.format(n))