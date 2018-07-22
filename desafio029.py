vel = int(input('Digite a velocidade do seu carro no momento: '))
if vel > 80:
    temp = vel - 80
    multa = temp * 7
    print('\033[30;41mVocê ultrapassou a velocidade permitida em {} quilometros. Sua multa eh de: R${}'.format(temp, multa))
else:
    print('\033[30;32mMuito bom! Você está na velocidade permitida.')