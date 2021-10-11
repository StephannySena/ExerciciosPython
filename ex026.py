frase = str(input('Digite uma frase: ')).strip()
print('Quantidades de "A": ', frase.lower().count('a'))
print('A primeira letra "A" aparece na posição: ', frase.find('a'))
print('A última letra "A" aparece na posição: ', frase.rfind('a'))


