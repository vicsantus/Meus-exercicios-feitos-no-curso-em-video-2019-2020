n1 = float(input('Digite um n�mero: '))
n2 = float(input('Digite outro n�mero: '))
print('O que voc� deseja fazer?')
print("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR N�MERO
[4] NOVOS N�MEROS
[5] SAIR DO PROGRAMA""")
rep = 0
novo = 0
mult = n1 * n2
adc = n1 + n2
while rep < 1:
    menu = int(input('\nDigite a op��o desejada: '))
    if menu == 5:
        rep += 1
    elif menu == 2:
        print('O valor da multiplica��o � igual a {}.'.format(mult))
    elif menu == 1:
        print('O valor da adi��o � igual a {}.'.format(adc))
    elif menu == 4:
        novo = float(input('Digite o novo valor: '))
        adc += novo
        mult *= novo
    elif menu == 3:
        if n1 > n2 and n1 > novo:
            print('O n�mero {} � o maior.'.format(n1))
        elif n2 > n1 and n2 > novo:
            print('O n�mero {} � o maior.'.format(n2))
        else:
            print('O n�mero {} � o maior.'.format(novo))
    else:
        print('Op��o inv�lida!')