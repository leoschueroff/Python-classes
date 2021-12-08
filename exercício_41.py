# A confederação nacional de natação
# precisa de um programa que leia o ano
# de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade
#
# até 9 anos : Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Senior
# Acima: Master


from datetime import date

ano = int(input('Em que ano você nasceu?: '))
idade = date.today().year - ano

if idade <= 9:
    print('Sua categoria é: Mirim')

elif idade <= 14 and idade > 9:
    print('Sua categoria é: Infantil')

elif idade <= 19 and idade > 14:
    print('Sua categoria é: Junior')

elif idade == 20:
    print('Sua categoria é: Sênior')

elif idade > 20:
    print('Sua categoria é: Master')

    