'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = input('Digite o seu nome completo: ')
dividido = nome.split()
print('Primeiro nome: {}'.format(dividido[0]))
print('Último nome: {}'.format(dividido[-1]))