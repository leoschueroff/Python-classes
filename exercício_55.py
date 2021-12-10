# Crie um programa que leia o peso de 5 pessoas
# No final, mostre qual foi o maior e o menor peso.

maior = 0
menor = 1000
for i in range (1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('''O menor peso foi: {} 
O maior peso foi {} '''.format(menor,maior))