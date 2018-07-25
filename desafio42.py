'''
Refaça o desafio 035 dos triangulos acrescentando o recurso de mostrar se formará um triangulo equilátero, isósceles ou escaleno.
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

if a == b and a == c:
    print('É um triângulo equilátero!')
elif a == b or a ==c or b == c:
    print('É um triângulo isósceles!')
else:
    print('É um triângulo escaleno!')