salario = float(input('Digite seu salário: R$ '))
if salario > 1250.00:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)
print('Seu salário reajustado é R$ {:.2f}'.format(salario))
