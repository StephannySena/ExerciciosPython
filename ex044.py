preco = float(input('Insira o preço do produto: '))
pgto = str(input('Insira qual será a forma de pagamento (à vista, à vista cartão, 2x, 3x ou mais.): '))
if pgto == 'à vista':
    print('Pagamento à vista: {:.2f}'.format(preco - (preco * 10/100)))
elif pgto == 'à vista cartão':
    print('Pagamento á vista no cartão: {:.2f}'.format(preco - (preco * 5/100)))
elif pgto == '2x':
    print('Pagamento em 2x no cartão: {:.2f}'.format(preco))
else:
    print('Pagamento em 3x ou mais: {:.2f}'.format(preco + (preco * 20/100)))
