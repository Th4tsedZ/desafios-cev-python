'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela se o primeiro valor é maior, se o segundo valor é maior ou se os dois são iguais.
'''
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo valor {}!'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro valor {}!'.format(n2, n1))
else:
    print('Não existe valor maior! Os dois valores são iguais.'.format(n1, n2))