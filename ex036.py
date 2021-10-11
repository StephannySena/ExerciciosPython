valor = float(input('Digite o valor total do imóvel: '))
salario = float(input('Digite seu salário total: '))
anos = int(input('Digite em quantos anos você pretende pagar: '))
valor_mensal = valor / (anos * 12)

if valor_mensal <= (salario * 30/100):
    print('\033[1;97;42mEmpréstimo Aprovado!\033[m \n Valor total do imóvel: {:.2f} \nValor da parcela: {:.2f} \nTotal de parcelas: {}'.format(valor,valor_mensal,(anos*12)))
else:
    print('\033[1;97;41mEmpréstimo Negado.\033[m \nSugerimos que tente novamente em 6 meses.')