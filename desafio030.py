n = int(input('Digite um número qualquer: '))
if n%2 == 0:
    print('O número \033[34m{}\033[m eh par!'.format(n))
else:
    print('O número \033[33m{}\033[m eh ímpar!'.format(n))