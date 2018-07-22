n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Média: {}\nReprovado!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Média: {}\nRecuperação!'.format(media))
else:
    print('Média: {}\nAprovado!'.format(media))