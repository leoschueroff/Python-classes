# Crie um programa que faça o computador jogar Jokenpô com você

import random

escolha = int(input('''Escolha seu elemento do Jokenpô: 
1 - Papel
2 - Pedra
3 - Tesoura : '''))

opcoes = 'Papel' , 'Pedra' , 'Tesoura'
pc = random.choice(opcoes)

if escolha == 1 and pc == 'Tesoura':
    print('O computador escolheu TESOURA e te VENCEU')

elif escolha == 1 and pc == 'Pedra':
    print('O computador escolheu PEDRA e você VENCEU')

elif escolha == 1 and pc == 'Papel':
    print('O computador também escolheu PAPEL por isso não há um vencedor')

elif escolha == 2 and pc == 'Papel':
    print('O computador escolheu PAPEL e te VENCEU ')

elif escolha == 2 and pc == 'Pedra':
    print('O computador também escolheu PEDRA por isso não há um vencedor')

elif escolha == 2 and pc == 'Tesoura':
    print('O computador escolheu TESOURA e você VENCEU')

elif escolha == 3 and pc == 'Papel':
    print('O computador escolheu PAPEL e você VENCEU')

elif escolha == 3 and pc == 'Pedra':
    print('O computador escolheu PEDRA e te VENCEU')

elif escolha == 3 and pc == 'Tesoura':
    print('O computador também escolheu TESOURA por isso não há um vencedo')
