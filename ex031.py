distancia = float(input('Insira a distância da viagem em Km: '))
if distancia <= 200:
    passagem = 0.50 * distancia
else:
    passagem = 0.45 * distancia
print('O valor da passagem para uma viagem de {}Km é R$ {:.2f}'.format(distancia,passagem))