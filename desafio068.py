'''
Crie um programa que jogue par pi ímpar com o computador. O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v = s = c = d = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    v = int(input('Diga um valor: '))
    choice = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    r = randint(0, 10)
    s = v + r
    if s%2 == 0 and choice == 'P':
        print(f'Você jogou {v} e o computador {r}. Total de {s}, DEU PAR!')
        print('VOCÊ VENCEU!\nVamos jogar novamente...')
        print('=-'*15)
        c += 1
    elif s%2 != 0 and choice == 'I':
        print(f'Você jogou {v} e o computador {r}. Total de {s}, DEU ÍMPAR!')
        print('VOCÊ VENCEU!\nVamos jogar novamente...')
        print('=-' * 15)
        c += 1
    elif s%2 == 0 and choice == 'I':
        print(f'Você jogou {v} e o computador {r}. Total de {s}, DEU PAR!')
        print('VOCÊ PERDEU!')
        print('=-' * 15)
        print(f'GAME OVER! Você venceu {c} vezes')
        d = 1
    elif s%2 != 0 and choice == 'P':
        print(f'Você jogou {v} e o computador {r}. Total de {s}, DEU ÍMPAR!')
        print('VOCÊ PERDEU!')
        print('=-' * 15)
        print(f'GAME OVER! Você venceu {c} vezes')
        d = 1
    if d == 1:
        break
    d = 0