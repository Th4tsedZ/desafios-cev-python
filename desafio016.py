'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
import math
num = float(input('Digite um número real: '))
numint = math.trunc(num)
print('A porção inteira de {} eh: {}'.format(num, numint))
