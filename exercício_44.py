# Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e
# condição de pagamento:
#
# á vista dinheiro/cheque: 10% de desconto
# a vísta no cartao: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Qual é o valor do seu produto? : '))
pagamento = int(input(''' Escolha sua forma de pagamento: 
1 - Á vista no dinheiro/cheque 
2 - Á vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão : '''))

desconto1 = preco - (preco * 0.10)
desconto2 = preco - (preco * 0.05)
juros = preco + (preco * 0.20)

if pagamento == 1:
    print('Seu produto custará: {:.2f} reais'.format(desconto1))

elif pagamento == 2:
    print('Seu produto custará: {:.2f} reais '.format(desconto2))

elif pagamento == 3:
    print('Seu produto permanecerá custando {:.2f} reais '.format(preco))

elif pagamento == 4:
    print('''Seu produto terá um acréscimo de ' (preco * 0.20) reais
     ficando no valor de : {:.2f}'''.format(juros))