from datetime import date
nasc = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - nasc
print('Sua idade é: {} anos'.format(idade))
if idade < 18:
    print('Você deverá se alistar ao \033[42mserviço militar\033[m daqui a {} anos.'.format(18-idade))
elif idade > 18:
    print('Você já deveria ter se alistado ao \033[42mserviço militar\033[m há {} anos atrás.'.format(idade-18))
else:
    print('Que horas são? Hora de se alistar ao \033[42mserviço militar\033[m!')
