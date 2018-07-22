from math import hypot, sqrt
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
#hip = cato**2 + cata**2
#hip2 = sqrt(hip)
hip = hypot(cato, cata)
print('A hipotenusa deste triângulo retângulo vale: {}'.format(hip))