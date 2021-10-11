from datetime import date
nasc = int(input('Insira o ano de nascimento do atleta: '))
idade = date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))
if idade < 9:
    print('Categoria: \033[35mMIRIM\033[m')
elif idade >= 9 and idade < 14:
    print('Categoria: \033[33mINFANTIL\033[m')
elif idade >=14 and idade <19:
    print('Categoria: \033[36mJUNIOR\033[m')
elif idade >=19 and idade < 20:
    print('Categoria: \033[32mSENIOR\033[m')
else:
    print('Categoria: \033[34mMASTER\033[m')