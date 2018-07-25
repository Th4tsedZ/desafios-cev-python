'''
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos paspites foram necessários.
'''
import random
cont = 0
n = random.randint(0, 10)
nuser = int(input('O computador pensou em um número entre 0 e 10. Será que você consegue acertar qual? \nDigite o número que você escolheu: '))
while n != nuser:
    nuser = int(input('O valor não está correto! O computador escolheu {} e você {}. \nDigite novamente: '.format(n, nuser)))
    if n == nuser:
        print('\033[4;32mParábens!\033[m Você acertou o número que a máquina escolheu: {} :D'.format(n))
    cont +=1
print('Foram necessárias {} tentativas para acertar!'.format(cont))