import random
lista = [0, 1, 2, 3, 4, 5]
num = random.choice(lista)
palpite = int(input('Acabei de pensar em um número, você consegue adivinhar? \nDigite seu palpite: '))
if num == palpite:
    print('PARABÉNS, VOCÊ VENCEU!\nComo você sabia?')
else:
    print('HAHA, PERDEU!\nEu pensei no número {} e não {}.'.format(num, palpite))