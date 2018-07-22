num = int(input('Digite um número inteiro qualquer: '))
for c in range(0, 11):
    tabu = num * c
    print('{} X {} = {}'.format(num, c, tabu))