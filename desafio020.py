'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do primeiro aluno: ')
a3 = input('Digite o nome do primeiro aluno: ')
a4 = input('Digite o nome do primeiro aluno: ')
s = [a1,a2,a3,a4]
random.shuffle(s)
print('A sequência de apresentação dos alunos eh a seguinte: {}'.format((s)))