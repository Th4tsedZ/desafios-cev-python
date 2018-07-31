'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
n = c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')
        break
    while c <= 10:
        prod = n * c
        print(f'{n} x {c} = {prod}')
        c += 1
    c = 0