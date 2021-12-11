# REFAÇA O EXERCÍCIO 28
# DESSA VEZ UTILIZANDO A ESTRUTURA WHILE

from random import randint
from time import sleep

# cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}


print("{}-=-{}".format(cor['amarelo'], cor['limpa']) * 19)
print("{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}".format(cor['azul'], cor['limpa']))
print("{}-=-{}".format(cor['amarelo'], cor['limpa']) * 19)

computador = randint(0, 6)
palpites = 0
jogador = 0

while jogador != computador:
    jogador = int(input("Em que número eu pensei? "))
    palpites += 1
    print("{}Processando...{}".format(cor['lilas'], cor['limpa']))
    sleep(3)
if jogador == computador:
            print("{}PARABENS! Você acertou!{}".format(cor['verde'], cor['limpa']))
else:
            print("{}Que pena, você errou. Pensei no número {}{}".format(cor['vermelho'], computador, cor['limpa']))