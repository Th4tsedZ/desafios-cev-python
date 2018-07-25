'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade se ele ainda vai se alistar, se é hora de se alistar ou se ja passou da data de alistamento. Também será necessário mostrar o tempo que falta ou quanto passou do prazo.
'''
from datetime import date
anoNasc = int(input('Digite o seu ano de nascimento: '))
temp = date.today()
anoAtual = temp.year
anoBirth = anoNasc + 17
resto = anoBirth - anoAtual
calc = anoAtual - anoNasc
if calc < 17:
    print('Faltam {} anos para você de alistar: '.format(resto))
elif calc > 17:
    print('Você está {} anos atrasado para o alistamento militar! '.format(calc - 17))
else:
    print('Está na hora de se alistar! ')
