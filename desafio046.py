'''
Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício.
'''
import time
import emoji
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize(':fireworks:'))