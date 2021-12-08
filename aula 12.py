
#Programa para ler e identificar se um nome é popular, feio ou normal
#condições aninhadas


nome = str(input('Qual é o seu nome?: '))
if nome == 'Gustavo':
    print ('Que nome bonito')

elif nome == 'Pedro' or nome =='Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')

elif nome in 'Joackin Debi Saracura Cristivaldo Osvaldo Osmarilho Cristivaldo Neymar':
    print('Seu nome é muito feio')

else:
    print ('Seu nome é bem normal.')

print('Tenha um bom dia {}'.format(nome))

