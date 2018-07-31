'''
Crie um programa que leia vários números inteiros pelo teclado até que o número digitado seja 999. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''
n = t = s = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    t += 1
    s += n
print(f'A soma dos {t} valores foi {s}')
