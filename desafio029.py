'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel = int(input('Digite a velocidade do seu carro no momento: '))
if vel > 80:
    temp = vel - 80
    multa = temp * 7
    print('\033[30;41mVocê ultrapassou a velocidade permitida em {} quilometros. Sua multa eh de: R${}'.format(temp, multa))
else:
    print('\033[30;32mMuito bom! Você está na velocidade permitida.')