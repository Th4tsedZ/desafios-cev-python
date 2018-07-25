'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia de Fibonacci.
'''
a = c = 1

i = b = 0
n = int(input('Quantidade de termos: '))
while i < n:
    c = a + b
    a = b
    b = c
    i += 1
    print('O {}º termo da sequência de Fibonacci é: {}'.format(i, a))