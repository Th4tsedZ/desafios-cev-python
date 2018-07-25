'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = h * l
quantidade = a / 2
print('A área da parede eh de {:.2f}m². Serão necessárias {:.0f} latas de tinta para pinta-la'.format(a, quantidade))
