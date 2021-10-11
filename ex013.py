salario = float(input('Digite o salário: R$'))
novosalario = salario + (salario * 15 / 100)
print('O novo salário com reajuste de 15% é: R$ {:.2f}'.format(novosalario))