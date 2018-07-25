'''
Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e consição de pagamento.
'''
precoNormal = float(input('Digite o preço do produto sem descontos nem acréscimos: '))
conPagamento = str(input('Digite a condição de pagamento: '))
if conPagamento.lower() == 'dinheiro' or conPagamento.lower() == 'cheque':
    precoDin = precoNormal - precoNormal * 0.10
    print('Valor do produto: R${:.2f}'.format(precoDin))
elif conPagamento.lower() == 'cartão':
    precoVista = precoNormal - precoNormal * 0.05
    print('Valor do produto: R${:.2f}'.format(precoVista))
elif conPagamento.lower() == '2x no cartão':
    print('Valor do produto: R${:.2f}'.format(precoNormal))
elif conPagamento.lower() == '3x ou mais':
    preco3x = precoNormal + precoNormal * 0.20
    print('Valor do produto: R${:.2f}'.format(preco3x))