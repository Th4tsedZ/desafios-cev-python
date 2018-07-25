'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas;
– Quantas letras ao todo;
– Quantas letras tem o primeiro nome
'''
nome = input('Digite o seu nome completo: ')
print('Seu nome com todas as letras maiúsculas eh: {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas eh: {}.'.format(nome.lower()))
print('Seu nome possuí {} letras.'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
print('Seu primeiro nome eh: {}'.format(dividido[0]))
