# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emrpéstimo será negado.


valor = float(input('Qual é o valor da casa que você deseja comprar? : '))
salario = float(input('Qual é o seu salário mensal? : '))
parcelas = int(input('Em quantas parcelas você deseja? : '))

prestacao = valor / parcelas
exceder = salario * 0.30

if prestacao > exceder:
    print('Infelizmente seu empréstimo não foi aprovado')

else:
    print('O valor da sua prestação é de {:.2f}'.format(prestacao))