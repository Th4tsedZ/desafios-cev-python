import random
entrada = str(input('Digite pedra, papel ou tesoura: '))
entrada.lower()
maquina = random.randint(1, 4)
if maquina == 1:
    joken = 'pedra'
elif maquina == 2:
    joken = 'papel'
elif maquina == 3:
    joken = 'tesoura'
if entrada.strip() == 'pedra' and joken == 'tesoura':
    print('Você ganhou!\nA máquina escolheu {}'.format(joken))
elif entrada.strip() == 'pedra' and joken == 'pedra':
    print('Empate!\nA máquina também escolheu {}'.format(joken))
elif entrada.strip() == 'pedra' and joken == 'papel':
    print('Você perdeu!\nA máquina escolheu {}'.format(joken))
elif entrada.strip() == 'papel' and joken == 'pedra':
    print('Você ganhou!\nA máquina escolheu {}'.format(joken))
elif entrada.strip() == 'papel' and joken == 'papel':
    print('Empate!\nA máquina também escolheu {}'.format(joken))
elif entrada.strip() == 'papel' and joken == 'tesoura':
    print('Você perdeu!\nA máquina escolheu {}'.format(joken))
elif entrada.strip() == 'tesoura' and joken == 'papel':
    print('Você ganhou!\nA máquina escolheu {}'.format(joken))
elif entrada.strip() == 'tesoura' and joken == 'tesoura':
    print('Empate!\nA máquina também escolheu {}'.format(joken))
elif entrada.strip() == 'tesoura' and joken == 'pedra':
    print('Você perdeu!\nA máquina escolheu {}'.format(joken))