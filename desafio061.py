'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while.
'''
pa = 0
c = 1
pTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os dez primeiros termos desta PA são: ')
while c <= 10:
    pa = pTermo + (c - 1) * razao
    print('O {} termo desta PA é: {}'.format(c, pa))
    c += 1