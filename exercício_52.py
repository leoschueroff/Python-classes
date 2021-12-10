# Desenvolva um programa que leia um número e mostre na tela se ele é numero primo.


total = 0
num = int(input('Digite um número e veja se ele é primo: '))
for i in range(1, num + 1):
    if num % i == 0:
        total += 1
print('O número {}, {}'.format(num, 'Não é primo' if total > 2 else 'É primo' ))

