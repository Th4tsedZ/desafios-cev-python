'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Calcule o valor da prestção mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
vCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
tempoPag = float(input('Digite em quanto tempo você irá pagar a casa (anos): '))
prestMes = (vCasa / tempoPag) / 12

if prestMes > salario * 0.30:
    print('Empréstimo negado! \nO valor da prestação mensal é de R${:.2f} e equivale a mais de 30% do seu salário!'.format(prestMes))
else:print('Empréstimo aprovado! \nO valor da prestação mensal é de R${:.2f} e equivale a menos de 30% do seu salário!'.format(prestMes))