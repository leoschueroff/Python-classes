# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão
# aritimética . No final, mostre os 10 primeiros termos dessa progressão.

print('='*20)
print('PROGRESSÃO DE UMA PA')
print('='*20)

termo = int(input(' Digite o primeiro termo da sua PA: '))
razao = int(input(' Digite a razão dessa PA: '))
s = termo + 10 * razao

for i in range(termo, s, razao ):
    print(i)

print('FIM')