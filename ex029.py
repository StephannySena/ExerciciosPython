velocidade = float(input('Insira a velocidade do veículo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Você foi multado por passar {}Km/h acima do limite. A multa a pagar é R$ {:.2f}'.format(velocidade-80, multa))