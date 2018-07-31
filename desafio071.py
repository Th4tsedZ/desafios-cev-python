'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: considere que o caixa possuí cédulas de R$50, R$20, R$10 e R$1.
'''
print('='*40)
print('BANCO CEV')
print('='*40)
valor = int(input('Qual valor você quer sacar? R$'))
vCinquenta = valor // 50
rCinquenta = valor % 50
vVinte = rCinquenta // 20
rVinte = rCinquenta % 20
vDez = rVinte // 10
rDez = rVinte % 10
vUm = rDez // 1
print(f'Total de {vCinquenta} cédulas de R$50')
print(f'Total de {vVinte} cédulas de R$20')
print(f'Total de {vDez} cédulas de R$10')
print(f'Total de {vUm} cédulas de R$1')
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

