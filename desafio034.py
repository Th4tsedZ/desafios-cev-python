'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
sal = float(input('Digite o seu salário: '))
if sal > 1250:
    aumento = sal * 1.10
    print('\033[44mO salário com 10% de aumento eh:\033[m R${:.2f}'.format(aumento))
else:
    aumento = sal * 1.15
    print('\033[45mO salário com 15% de aumento eh:\033[m R${:.2f}'.format(aumento))
