num = int(input('Digite um número inteiro: '))
#usando conhecimentos iniciais
print('',num,'* 0 =',(num*0),'\n',num,'* 1 =',(num*1),'\n',num, '* 2 =',(num*2),'\n',num,'* 3 =',(num*3),'\n',num,'* 4 =',(num*4),'\n',num,'* 5 =',(num*5),'\n',num,'* 6 =',(num*6),'\n',num,'* 7 =',(num*7),'\n',num,'* 8 =',(num*8),'\n',num,'* 9 =',(num*9),'\n',num,'* 10 =',(num*10), end='\n\n')


#usando o for:
for i in range(11):
    print(num,'* {} = {}'.format(i,num*i))
