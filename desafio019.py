import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do primeiro aluno: ')
a3 = input('Digite o nome do primeiro aluno: ')
a4 = input('Digite o nome do primeiro aluno: ')
s = [a1,a2,a3,a4]
random.shuffle(s)
print('A sequência de apresentação dos alunos eh a seguinte: {}'.format((s)))