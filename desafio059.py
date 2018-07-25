'''
Criar um programa que leia dois valores e mostre um menu na tela (somar, multiplicar, maior, novos números, sair do programa). Seu programa deverá realizar a operação solicitada em cada caso.
'''
escolha = 0
while escolha != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))

    escolha = int(input('''
1 - Soma
2 - Multiplicação
3 - Maior valor
4 - Novos números
5 - Sair do programa

Escolha uma das opções[1, 2, 3, 4, 5]: '''))
    if escolha == 1:
        ope = n1 + n2
        print('A soma dos valores é: {}'.format(ope))
    elif escolha == 2:
        ope = n1 * n2
        print('A multiplicação dos valores é: {}'.format(ope))
    elif escolha == 3:
        if n1 > n2:
            ope = n1
            print('O maior valor é: {}'.format(ope))
        elif n2 > n1:
            ope = n2
            print('O maior valor é: {}'.format(ope))
    elif escolha == 4:
        n1 = int(input('Digite o novo primeiro valor: '))
        n2 = int(input('Digite o novo segundo valor: '))
