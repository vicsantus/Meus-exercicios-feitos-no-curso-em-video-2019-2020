from random import randint
print('=O=' * 10)
print('Vamos jogar par ou impar?')
print('=O=' * 10)
while True:
    computador = randint(1, 10)
    player = int(input('Escolha um número: '))
    soma = computador + player
    pop = str(input('Escolha par ou impar [P/I]: ')).upper().strip()
    while True:
        if pop != 'P' and pop != 'I':
            print('Opção inválida!')
        else:
            break
    if pop == 'P':
        if soma % 2 == 0:
            print('\nVocê VENCEU!')
            print('Vamos jogar novamente...\n')
        elif soma % 2 != 0:
            print('Você PERDEU. LOSER. PERDEDOR. INUTIL. XÔ!')
            break
    elif pop == 'I':
        if soma % 2 != 0:
            print('\nVocê VENCEU!')
            print('Vamos jogar novamente...\n')
        elif soma % 2 == 0:
            print('Você PERDEU. LOSER. PERDEDOR. INUTIL. XÔ!')
            break