'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
km = float(input('Digite a distância da sua viagem em KM: '))
if km <= 200:
    valorp = km * 0.50
    print('O valor da sua passagem será de: \033[31;47mR${:.2f}\033[m'.format(valorp))
else:
    valorp = km * 0.45
    print('O valor da sua passagem será de: \033[36;41mR${:.2f}\033[m'.format(valorp))