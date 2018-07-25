'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
pTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = 0
print('Os dez primeiros termos desta PA são: ')
for c in range(1, 11):
    pa = pTermo + (c - 1) * razao
    print(pa)