km = float(input('Digite a distância da sua viagem em KM: '))
if km <= 200:
    valorp = km * 0.50
    print('O valor da sua passagem será de: \033[31;47mR${:.2f}\033[m'.format(valorp))
else:
    valorp = km * 0.45
    print('O valor da sua passagem será de: \033[36;41mR${:.2f}\033[m'.format(valorp))