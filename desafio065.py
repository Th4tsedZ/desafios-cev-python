'''
Crie um programa que leia vários números inteiros e no final, mostre a média entre eles; mostre também o menor e maior valor. O programa deve perguntar se o usuário quer continuar a digitar valores.
'''
media = cont = temp = 0
res = 'S'
maior = 1
menor = 999999
while res == 'S':
    cont += 1
    n = int(input('Digite um número inteiro: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    res = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    temp += n
media = temp / cont
print('A média entre os {} números digitados é: {:.2f}'.format(cont, media))
print('O maior valor foi {}, enquanto o menor foi {}'.format(maior, menor))