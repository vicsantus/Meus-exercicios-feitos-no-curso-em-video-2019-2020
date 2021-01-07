from random import choice

n1 = input('Digite o nome da primeira vítima: ')
n2 = input('Digite o nome da segunda vítima: ')
n3 = input('Digite o nome da terceira vítima: ')
n4 = input('Digite o nome da quarta vítima: ')
sorteio = (n1, n2, n3, n4)
print('O felizardo foi {}. Parabéns!'.format(choice(sorteio)))