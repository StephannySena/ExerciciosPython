peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura*altura)

if IMC < 18.5:
    print('Você está \033[31mabaixo do peso.\033[m')
elif IMC >= 18.5 and IMC < 25:
    print('Você está no \033[32mpeso ideal\033[m!')
elif IMC >= 25 and IMC < 30:
    print('Você está com \033[31msobrepeso\033[m.')
elif IMC >= 30 and IMC < 40:
    print('Você está com \033[31mobesidade\033[m.')
else:
    print('Você está com \033[31;40mobesidade mórbida\033[m')
