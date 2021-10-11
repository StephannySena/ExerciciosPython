r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
retas = [r1, r2, r3]
retas.sort()
if (retas[0]+retas[1]) > retas[2]:
    print('É possível formar um triangulo')
    if r1 == r2 == r3:
        print('O triângulo será \033[1;34mequilátero\033[m.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é \033[1;31misósceles\033[m.')
    else:
        print('O triângulo é \033[1;33mescaleno\033[m.')
else:
    print('Não é possível formar um triângulo')

