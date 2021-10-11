termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
for i in range(0,10):
    print(termo, end='; ')
    termo += razao
