from random import choice
from time import sleep
jokenpo = ['pedra', 'papel','tesoura']
print('\033[34m=*\033[m' *28,'Vamos jogar JOKENPO??? Escolha Pedra, Papel ou Tesoura','\033[34m=*\033[m'*28, sep = '\n')
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')
jogador = str(input('Digite sua escolha: '))
computador = choice(jokenpo)

print('VOCÊ:',jogador,'\n       x       ','\n EU: ',computador)

if jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
    print('\033[34mVocê ganhou! Topa uma revanche?\033[m')
elif computador =='pedra' and jogador == 'tesoura' or computador == 'papel' and jogador == 'pedra' or computador == 'tesoura' and jogador == 'papel':
    print('\033[31mVocê perdeu! Tente novamente\033[m')
else:
    print('\033[33mTemos um empate, mas aposto que eu ganho na próxima!\033[m')
