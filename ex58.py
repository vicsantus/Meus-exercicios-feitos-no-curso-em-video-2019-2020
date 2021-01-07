from random import randint

while True:
    num = randint(0, 100)
    while True:
        adv = int(input('Tente adivinhar o número de 0 a 100: '))
        if num > adv:
            print('O número é maior!')
        elif num < adv:
            print('O número é menor!')
        else:
            print('Você acertou! O número é {}!'.format(num))
            break
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if continuar not in 'ns':
            print('Digite uma opção válida!')
        else:
            break
    if continuar == 'n':
        print('BYE!')
        break