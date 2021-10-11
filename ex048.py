soma = 0
for c in range(1, 500+1):
    if c % 2 != 0:
        if c % 3 ==0:
            soma += c

print('A soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500 é: {}'.format(soma))