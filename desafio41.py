'''
Criar um programa que leia o ano de nascimento de um atleta e informe sua categoria de acordo com sua idade.
'''
from datetime import date
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
temp = date.today()
anoAtual = temp.year
idade = anoAtual - anoNasc
if idade <= 9:
    print('Idade: {}\nCategoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Idade: {}\nCategoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade: {}\nCategoria: JUNIOR'.format(idade))
elif idade <= 20:
    print('Idade: {}\nCategoria: SÊNIOR'.format(idade))
else:
    print('Idade: {}\nCategoria: MASTER'.format(idade))