n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Ok, digite mais um número: '))
maior_n = n1
if maior_n < n2:
    maior_n = n2
if maior_n < n3:
    maior_n = n3

menor_n = n1
if menor_n > n2:
    menor_n = n2
if menor_n > n3:
    menor_n = n3

print('O maior número é {} e o menor número é {}. ' .format(maior_n, menor_n))
