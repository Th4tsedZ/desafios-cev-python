'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
cidade = input('Digite o nome de uma cidade: ')
dividido = cidade.split()
print('O nome da sua cidade começa com "Santo"?')
print('Santo' in dividido[0])