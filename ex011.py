larg = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
area = larg * alt
tinta = area / 2
print('A quantidade de tinta necesária para pintar {} m² é {} litros.'.format(area,tinta))
