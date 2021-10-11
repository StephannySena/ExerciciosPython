frase = str(input('Insira uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for l in range(len(junto)-1,-1,-1):
    inverso += junto[l]
print(inverso)
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')
