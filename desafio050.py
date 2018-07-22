soma = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num%2==0:
        soma += num
    else:
        print(end=='')
print('A soma dos valores pares eh de: {}'.format(soma))
