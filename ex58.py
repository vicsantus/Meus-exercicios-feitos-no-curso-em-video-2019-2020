from random import randint

while True:
    num = randint(0, 100)
    while True:
        adv = int(input('Tente adivinhar o n�mero de 0 a 100: '))
        if num > adv:
            print('O n�mero � maior!')
        elif num < adv:
            print('O n�mero � menor!')
        else:
            print('Voc� acertou! O n�mero � {}!'.format(num))
            break
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if continuar not in 'ns':
            print('Digite uma op��o v�lida!')
        else:
            break
    if continuar == 'n':
        print('BYE!')
        break