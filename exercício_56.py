# Desenvolva um programa que leia o nome, idade e sexo
# de 4 pessoas. No final do programa, mostre:
#
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos

soma_idade = 0
homem_idade = 0
homem_nome = ''
c_mulheres = 0

for i in range(1,5):
    print('------ {}º Pessoa -------'.format(i))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]')).upper()

    soma_idade += idade

    if sexo in 'Mm' and idade > homem_idade:
        homem_idade = idade
        homem_nome = nome

    if sexo in 'Ff' and idade < 20:
        c_mulheres += 1

print('A média de idade do grupo é de: {} anos '.format(int(soma_idade / 4)))
print('O homem mais velho tem {} anos e se chama {} '.format(homem_idade, homem_nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(c_mulheres))