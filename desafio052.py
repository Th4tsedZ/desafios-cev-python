num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot += 1
if tot <= 2 and tot != 1:
    print('{} é um número primo! '.format(num))
else:
    print('{} não é um número primo! '.format(num))