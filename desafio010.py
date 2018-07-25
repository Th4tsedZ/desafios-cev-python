'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''
real = float(input('Quantos reais vocês pode gastar? '))
dol = real / 3.27
print('Você pode comprar ${:.2f} DOL'.format(dol))
