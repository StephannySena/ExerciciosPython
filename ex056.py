velho = 0
nomevelho = 'x'
idades = 0
mulheres = 0
for i in range(1,5):
    nome = str(input('Digite o nome da pessoa {}: '.format(i)))
    idade = int(input('Digite a idade da pessoa {}: '.format(i)))
    sexo = str(input('Digite o sexo da pessoa {}: '.format(i)))
    idades += idade
    if sexo == 'masculino':
        if idade > velho:
            velho = idade
            nomevelho = nome
    if sexo == 'feminino':
        if idade < 20:
            mulheres +=1
print('A idade média do grupo é: {}\nO homem mais velho é o: {}\nTotal de mulheres com menos de 20 anos: {}'.format(idades/4,nomevelho,mulheres))

