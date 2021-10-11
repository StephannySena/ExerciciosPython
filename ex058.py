from random import choice

números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = choice(números)
print(computador)
chances = 1
print('~'*10,'Acabei de pensar em um número, você consegue adivinhar?','~'*10)
jogador = int(input('Digite seu palpite: '))
while jogador != computador:
    jogador = int(input('Não foi dessa vez, vou te dar mais uma chance: '))
    chances += 1

print('Foram necessárias {} chances para você acertar.'.format(chances))
if chances > 1:
    print('Finalmente! Já estava cansado de te dar chances.')
else:
    print('Parabéns! Você acertou de primeira!')