import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do primeiro aluno: '))
a3 = str(input('Digite o nome do primeiro aluno: '))
a4 = str(input('Digite o nome do primeiro aluno: '))
s = [a1,a2,a3,a4]
print('O(a) aluno(a) escolhido foi: {}'.format(random.choice(s)))
