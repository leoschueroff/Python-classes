r = ''
while r != 'M' or 'F':
    r = str(input('Qual é o seu sexo? [M/F] : ' )).upper()
    if r in 'Mm':
        r = 'Homem'
        print('Você é {}'.format(r))
    elif r in 'Ff':
        r = 'Mulher'
        print('Você é {}'.format(r))

