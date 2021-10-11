km = float(input('Digite quantos Km você andou: '))
dias = int(input('Digite por quantos dias você alugou o carro: '))
pg = (60*dias) + (0.15 * km)
print('O valor a pagar por {} dias de aluguel do veículo e {} km rodados é R${:.2f}'.format(dias,km,pg))
