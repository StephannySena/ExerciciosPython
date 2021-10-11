maior = 0
menor = 0
from datetime import date
for i in range(1,8):
    nasc = int(input('Digite o ano de nascimento da pessoa {}: '.format(i)))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Total de pessoas maiores de idade: {}\nTotal de pessoas menores de idade: {}'.format(maior,menor))

