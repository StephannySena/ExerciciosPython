import math
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimeito do cateto adjacente: '))
hipotenusa = math.hypot(catop,catad)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
