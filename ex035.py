
r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
retas = [r1, r2, r3]
retas.sort()
if (retas[0]+retas[1]) > retas[2]:
    print('É possível formar um triangulo')
else:
    print('Não é possível formar um triângulo')