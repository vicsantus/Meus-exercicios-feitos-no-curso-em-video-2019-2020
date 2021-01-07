from random import randint
from time import sleep

num = []
soma = []


def Sorteia():
    for c in range(1, 6):
        num.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for c in num:
        if c % 2 == 0:
            soma.append(c)
        sleep(0.5)
        print(c, end=' ')
    print('PRONTO!')


def Somar():
    print(f'Somando os valores pares de {num}, temos {sum(soma)}')


Sorteia()
Somar()