# Desenvolva uma lógica que leia o peso e
# a altura de uma pessoa.
# Calcule seu IMC e mostre seu status
# de acordo com a tabela abaixo:
#
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40 : Obesidade
# Acima de 40: Obesidade mórbida

altura = float(input('Qual é a sua altura em metros? :'))
peso = float(input('Qual é o seu peso em kg? : '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(''' Seu IMC é de {} .
    Você está abaixo do peso!'''.format(imc))

elif imc >= 18.5 and imc < 25:
    print(''' Seu IMC é de {:.0f} 
    Você está no peso ideal!'''.format(imc))

elif imc >= 25 and imc < 30:
    print(''' Seu IMC é de {:.0f}
    Você está com sobrepeso!'''.format(imc))

elif imc >= 30 and imc < 40:
    print(''' Seu IMC é de {:.0f}
    Você está obeso! '''.format(imc))

elif imc > 40:
    print(''' Seu IMC é de {:.0f}
    Você está com obesidade mórbida!'''.format(imc))



