# Faça um programa que leia um número qualquer
# E mostre o seu fatorial.

n = int(input('Digite um número e veja seu fatorial: '))
fat = 1
print('Calculando {} ! = '.format(n), end='')

while n > 0:
    if n == 1:
        print(n, end='')
    else:
        print(n,end='x')
    fat *= n
    n -= 1
print(' = {} '.format(fat))












