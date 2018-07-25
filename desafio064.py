'''
Crie um programa que leia vários números inteiros pelo telcado e só pare quando o usuário digitar 999. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
'''
totalN = somaN = n =  0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        totalN += 1
        somaN += n
print('Foram digitados {} números e a soma entre eles é de {}'.format(totalN, somaN))
