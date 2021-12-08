# Escreva um programa que leia um número
# inteiro qualquer e peça para o
# usuário  escolher qual será a base de conversão.


numero = int(input('Digite um número : ' ))
pergunta2 = int(input(''' 1 - Binário.
2 - Octal.
3 - Hexadecimal

converter para: '''))

if pergunta2 == 1:
    print('O valor convertido para binário é de: {} '.format(bin.(numero)[2:]))