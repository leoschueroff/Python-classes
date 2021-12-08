nome = str(input('Qual é o seu nome?: '))
if nome == 'Gustavo':
    print ('Que nome bonito')

elif nome == 'Pedro' or 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')

elif nome in 'Joackin Debiloide Saracura':
    print('Seu nome é muito feio')

else:
    print ('Seu nome é bem normal.')

