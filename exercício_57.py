r = ''
while r != 'M' and r != 'F':
    r = str(input('Qual é o seu sexo? [M/F] : ' )).strip().upper()
if r == 'M':
    print('Sexo masculino registrado')
else:
    print('Sexo feminino registrado')