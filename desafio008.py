'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
mt = int(input('Digite um valor em metros: '))
cm = mt*100
ml = mt*1000
print('A distância digitada em centímetros eh: {}cm'.format(cm))
print('A distância digitada em milemetros eh: {}ml'.format(ml))
