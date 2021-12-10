# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
# ja são maiores.

from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for i in range (1,8):
    idades = int(input('Digite o ano de nascimento da pessoa número {} : '.format(i)))
    if ano_atual - idades >= 18:
        maior += 1
    else:
        menor += 1
print(''' Maiores de idade: {} 
  Menores de idade: {} '''.format(maior, menor))