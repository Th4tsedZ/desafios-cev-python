'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
s = float(input('Digite o salário atual do funcionário: '))
s2 = s * 0.15
sacr = s + s2
print('O salário do funcionário com acréscimo de 15% eh : R${:.2f}'.format(sacr))