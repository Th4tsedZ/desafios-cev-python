'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar. No final mostre:
A) Qual o total gasto na compa;
B) Quantos produtos custam mais de R$ 1000;
C) Qual o nome do produto mais barato;
'''
vTot = prodCaro = prodBarato = 0
nprodBarato = ''
print('-'*25)
print('LOJA SUPER BARATÃO')
print('-'*25)
prodBarato = 99999
while True:
    nProd = str(input('Nome do produto: '))
    vProd = float(input('Preço: R$'))
    choice = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    vTot += vProd
    if vProd > 1000:
        prodCaro += 1
    if vProd < prodBarato:
        prodBarato = vProd
        nprodBarato = nProd
    if choice == 'N':
        print('--------FIM DO PROGRAMA--------')
        break
print(f'O total da compra foi R${vTot:.2f}')
print(f'Temos {prodCaro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nprodBarato} que custa R${prodBarato}')