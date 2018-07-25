'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
frase = input('Digite uma frase: ')
print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}'.format(frase.find('a')))
print('A letra "a" aparece pela última vez na posição {}'.format(frase.rfind('a')))