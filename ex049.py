n = int(input('Insira um número:'))
print('TABUADA DO {}:'.format(n))
for c in range(0,10+1):
    print('{} x {:2} = {:2}'.format(n,c,n*c))