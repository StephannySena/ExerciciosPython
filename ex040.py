nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('\033[41mREPROVADO\033[m')
elif media >= 5 and media < 7:
    print('\033[43mRECUPERAÇÃO\033[m')
else:
    print('\033[42mAPROVADO\033[m')