'''
Faça um programa que leia o peso de cinco pessoas e mostre qual foi o maior e o menor peso.
'''
maior = 0
menor = 0
maior = menor = 0
maior = menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso é: {}Kg'.format(maior))
print('O menor peso é: {}Kg'.format(menor))

