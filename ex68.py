from random import randint
print('=O=' * 10)
print('Vamos jogar par ou impar?')
print('=O=' * 10)
while True:
    computador = randint(1, 10)
    player = int(input('Escolha um n�mero: '))
    soma = computador + player
    pop = str(input('Escolha par ou impar [P/I]: ')).upper().strip()
    while True:
        if pop != 'P' and pop != 'I':
            print('Op��o inv�lida!')
        else:
            break
    if pop == 'P':
        if soma % 2 == 0:
            print('\nVoc� VENCEU!')
            print('Vamos jogar novamente...\n')
        elif soma % 2 != 0:
            print('Voc� PERDEU. LOSER. PERDEDOR. INUTIL. X�!')
            break
    elif pop == 'I':
        if soma % 2 != 0:
            print('\nVoc� VENCEU!')
            print('Vamos jogar novamente...\n')
        elif soma % 2 == 0:
            print('Voc� PERDEU. LOSER. PERDEDOR. INUTIL. X�!')
            break