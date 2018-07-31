'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar. No final mostre:
A) quantas pessoas tem mais de 18 anos;
B) quantos homens foram cadastrados;
C) quantas mulheres tem menos de 20 anos;
'''
idade = mIdade = cHomem = cMulher = 0
s = ''
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    i = int(input('Idade: '))
    while True:
        s = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if s == 'M' or s == 'F':
            break
    choice = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if i > 18:
        mIdade += 1
    if s == 'M':
        cHomem += 1
    if s == 'F' and idade < 20:
        cMulher += 1
    if choice == 'N':
        print('FIM DO PROGRAMA ========================')
        break
print(f'Total de pessoas com mais de 18 anos: {mIdade}')
print(f'Ao todo, temos {cHomem} homens cadastrados')
print(f'E temos {cMulher} mulheres com menos de 20 anos')