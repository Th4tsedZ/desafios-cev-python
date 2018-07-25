'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
pa = 0
c = 1
novoC = 1
novoTermo = 1
pTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
while c <= 10:
    pa = pTermo + (c - 1) * razao
    print('O {}º termo desta PA é: {}'.format(c, pa))
    c += 1
while novoTermo != 0:
    novoTermo = int(input('Quantidade de novos termos: '))
    while novoC <= novoTermo:
        pa = pTermo + (c - 1) * razao
        print('O {}º termo desta PA é: {}'.format(c, pa))
        novoC += 1
        c += 1
    novoC = 1