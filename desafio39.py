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
