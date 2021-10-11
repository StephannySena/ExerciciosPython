n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
result = 0
print('-'*3,'Calculadora', '-'*3)
opc = 0
while opc != 5:
    opc = int(input('MENU:\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] INSERIR NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\n'))
    if opc == 1:
        resultado = n1 + n2
    elif opc == 2:
        resultado = n1 * n2
    elif opc == 3:
        if n1 > n2:
            resultado = n1
        else:
            resultado = n2
    elif opc == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        resultado = 0
    print('\033[1mO resultado da operação é {}\033[m'.format(resultado))
print('Você saiu da calculadora.')



