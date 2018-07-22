import math
ang = float(input('Digite um angulo qualquer: '))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno de {}º eh {:.2f}. Seu cosseno eh {:.2f} e a tangente eh {:.2f}'.format(ang, seno, cose, tang))

