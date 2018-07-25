'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
n = random.randint(0, 5)
nuser = int(input('O computador pensou em um número entre 0 e 5. Será que você consegue acertar qual? \nDigite o número que você escolheu: '))
if n == nuser:
    print('\033[4;32mParábens!\033[m Você acertou a número que a máquina escolheu: {} :D'.format(n))
else:
    print('\033[4;31mQue pena!\033[m Você não acertou o número em que a máquina estava pensando: {} :('.format(n))


