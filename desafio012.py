l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = h * l
quantidade = a / 2
print('A área da parede eh de {:.2f}m². Serão necessárias {:.0f} latas de tinta para pinta-la'.format(a, quantidade))
