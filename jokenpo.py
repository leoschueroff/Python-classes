from random import randint
from time import sleep


elementos = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
escolha = int(input('Escolha o número que representa seu elemento: [0] PAPEL , [1] TESOURA , [2] PEDRA: '))

if escolha > 2 or escolha < 0:
    print('OPÇÃO INVÁLIDA!')

else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!')

print('====' *12)
print('Você jogou {}'.format(elementos[escolha]))
print('O computador jogou {} '.format(elementos[computador]))


if escolha == 0 and computador == 1:
    print('O COMPUTADOR GANHOU!')

elif escolha == computador:
    print('EMPATE')

elif escolha == 0 and computador == 2:
    print('VOCÊ ganhou!!')

elif escolha == 1 and computador == 0:
    print('VOCÊ GANHOU!!')

elif escolha == 1 and computador == 2:
    print('O COMPUTADOR GANHOU! ')

elif escolha == 2 and computador == 0:
    print('O COMPUTADOR GANHOU!')

elif escolha == 2 and computador == 1:
    print('VOCÊ GANHOU!!')

