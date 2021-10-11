num = int(input('Insira um número para ver o seu fatorial: '))
i = num - 1
fatorial = num
print('{}! = {}'.format(num,num), end='')
while i > 0:
    fatorial = i * fatorial
    print(' x {}'.format(i), end='')
    i -= 1
print(' = {}'.format(fatorial))