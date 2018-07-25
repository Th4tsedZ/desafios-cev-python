'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
a = int(input('Digite quanto vale o lado A do triângulo: '))
b = int(input('Digite quanto vale o lado B do triângulo: '))
c = int(input('Digite quanto vale o lado C do triângulo: '))
if (b - c) < a < (b + c):
    if (a - c) < b < (a + c):
        if (a - b) < c < (a + b):
            print('\033[7;30;41mAs medidas informadas podem formar um triâgulo! ')
else:
    print('\033[7;32;40mAs medidas informadas não podem formar um triângulo!')
