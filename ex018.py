import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('Angulo digitado: {:.2f}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(angulo,seno,cos,tang))
