from random import choice

n1 = input('Digite o nome da primeira v�tima: ')
n2 = input('Digite o nome da segunda v�tima: ')
n3 = input('Digite o nome da terceira v�tima: ')
n4 = input('Digite o nome da quarta v�tima: ')
sorteio = (n1, n2, n3, n4)
print('O felizardo foi {}. Parab�ns!'.format(choice(sorteio)))