# Crie um programa que leia uma frase qualquer e diga
# se ela é palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
print('Sua frase invertida fica: {}. {}'.format(inverso,'É uma frase palíndromo' if inverso == junto else 'Não é uma frase palíndroma'))

