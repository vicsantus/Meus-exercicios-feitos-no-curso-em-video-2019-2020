from random import randint
num = randint(0, 5)
adv = int(input('Tente adivinhar o n�mero de 0 a 5: '))
print('Voc� acertou.' if adv == num else 'Voc� errou.')