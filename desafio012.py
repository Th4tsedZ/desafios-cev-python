'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
v = float(input('Digite o valor do produto: '))
v2 = v * 0.05
vdesc = v - v2
print('O valor deste produto com desconto de 5% eh de: R${:.2f}'.format(vdesc))