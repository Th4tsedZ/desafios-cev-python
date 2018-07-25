'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
ano = int(input('Digite um ano qualquer: '))
if ano%4 == 0:
    print('\033[7;30m{}\033[m é um ano \033[7;30mbissexto!\033[m'.format(ano))
else:
    print('\033[7;30m{}\033[m não é um ano \033[7;30mbissexto!\033[m'.format(ano))