from random import randint
num = randint(0, 5)
adv = int(input('Tente adivinhar o número de 0 a 5: '))
print('Você acertou.' if adv == num else 'Você errou.')