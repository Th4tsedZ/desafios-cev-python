n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('O maior número eh: \033[7;33m{}\033[m'.format(maior))
print('O menor número eh: \033[7;32m{}\033[m'.format(menor))