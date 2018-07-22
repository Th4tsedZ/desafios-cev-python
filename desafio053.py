frase = str(input('Digite uma frase: ')).lower().replace(' ', '')
for c in frase:
    for d in frase[::-1]:
        print(end=='')
if c == d:
    print('Esta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo!')