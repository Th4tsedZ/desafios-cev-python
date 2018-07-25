'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora, usando for.
'''
num = int(input('Digite um número inteiro qualquer: '))
for c in range(0, 11):
    tabu = num * c
    print('{} X {} = {}'.format(num, c, tabu))