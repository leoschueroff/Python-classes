# Escreva um programa que leia um número
# inteiro qualquer e peça para o
# usuário  escolher qual será a base de conversão.


numero = int(input('Digite um número : ' ))
pergunta2 = int(input(''' Qual conversão deseja fazer? :

1 - Binário.
2 - Octal.
3 - Hexadecimal
 '''))

if pergunta2 == 1:
    print ('Binário: {}'.format(bin(numero)[2:]))

elif pergunta2 == 2:
    print('Octal: {}'.format(oct(numero)[2:]))

elif pergunta2 == 3:
    print('Hexadecimal: {}'.format(hex(numero)[2:]))

else:
    print('Comando inválido')