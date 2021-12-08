# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade>
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar.
# - Se ja passou do tempo do alistamento.
#
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date


ano_atual = date.today().year
genero = int(input(''' Qual é o seu gênero? : 
1 - Masculino
2 - Feminino : '''))

if genero == 1:
    ano = int(input('Em que ano você nasceu?: '))

idade = ano_atual - ano

if idade == 18:
    print('Você deve se alistar esse ano')

elif idade < 18:
    print('Ainda faltam {} ano(s) para você se alistar'.format(18 - idade))

else:
    print('Você deveria ter se alistado faz {} ano(s) '.format(idade - 18))