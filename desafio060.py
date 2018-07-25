'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
'''
num = int(input('Digite um número: '))
#for c in range(num -1, 0, -1):
#    num *= c
#print(num)
fatorial = num
resultado = num
while fatorial != 1:
    fatorial -= 1
    resultado *= fatorial
print(resultado)