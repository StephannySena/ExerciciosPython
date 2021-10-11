maior = 0
menor = 1000
for i in range(1,6):
    peso = float(input('Digite o peso da pessoa {}:'.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso digitado foi: {}Kg\nO menor peso digitado foi: {}Kg '.format(maior,menor))