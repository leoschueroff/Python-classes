# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA
# [1] Somar [2] Multiplicar [3] Maior [4] Novos numeros [5] sair do programa.
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO

menu = 0
while menu != 5:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    menu = int(input(''' Digite a operação desejada: 
[1] Somar
[2] Multiplicar 
[3] Maior
[4] Novos números
[5] Sair do programa : '''))
    if menu == 1:
        print(n1 + n2)
        exit()
    elif menu == 2:
        print(n1 * n2)
        exit()
    elif menu == 3:
        if n1 < n2:
            print(n2)
            exit()
        elif n2 < n1:
            print(n1)
            exit()
        else:
            print('Os números são iguais!')
            exit()

print('Até logo!')
