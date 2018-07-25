'''
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final, exiba a média de idade, o nome do homeme mais velho e quantas mulheres tem menos de 20 anos.
'''
soma = 0
nmOlder = ''
mlVinte = 0
for c in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().lower()
    #Definição homem mais velho
    if c == 1:
        hmOlder = idade
        nmOlder = nome
    else:
        if idade > hmOlder:
            hmOlder = idade
            nmOlder = nome
    #Definição qtd de mulheres com menos de 20 anos
    if sexo == 'feminino' or sexo == 'f' and idade < 20:
        mlVinte += 1
    #Soma das idades para realização da média
    soma += idade
    print(' \n ')
mediaIdade = soma / 4
print('Média das idades: {:.1f}'.format(mediaIdade))
print('Homem mais velho: {}'.format(nmOlder))
print('Mulheres com menos de 20 anos: {}'.format(mlVinte))