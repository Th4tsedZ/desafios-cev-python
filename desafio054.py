from datetime import date
temp = date.today()
anoAtual = temp.year
calcMaior = 0
calcMenor = 0
for c in range(1,8):
    anoNasc = int(input('Digite o ano de nascimento de uma pessoa: '))
    idade = anoAtual - anoNasc
    if idade >= 18:
        calcMaior += 1
    elif idade <= 17:
        calcMenor += 1
print('{} pessoas já são maiores de idade!'.format(calcMaior))
print('{} pessoas ainda não são maiores de idade!'.format(calcMenor))
