# Refaça o exercício 035 dos triângulos
# acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
#
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))

if r1 == r2 and r1 == r3:
    print ('Suas retas podem formar um triângulo: Equilátero')

elif r1 == r2 and r1 != r3 and r1+r2 > r3:
    print ('Suas retas podem formar um triângulo: Isósceles')

elif r2 == r3 and r2+r3 > r1:
    print ('Suas retas podem formar um triângulo: Isósceles')

elif r3 == r1 and r3+r1 > r2:
    print ('Suas retas podem formar um triângulo: Isósceles' )

elif r3 != r2 and r2 != r1 and r3+r2 > r1 and r1+r2 > r3 and r3+r1 > r2:
    print ('Suas retas podem formar um triângulo: Escaleno')

else:
    print ('Seus valores não formam um triângulo!! ')