from random import randint
from time import sleep
player = int(input('Escolha - \033[31m0 para pedra\033[m / \033[32m1 para '
                   'papel\033[m / \033[33m2 para tesoura\033[m: '))
x = {0: '\033[31mpedra\033[m',
     1: '\033[32mpapel\033[m',
     2: '\033[33mtesoura\033[m'}
pc = randint(0, 2)
print('CALCULANDO...\n')
sleep(2)
if player == pc:
    print('EMPATE.')
elif (player == 0 and pc == 1) or (player == 1 and pc == 2) or (player == 2 and pc == 0):
    print('Você escolheu {}, o PC escolheu '
          '{}. \033[1;34m\nPC WIN!\033[m \033[1;31mYOU LOSE!\033[m'.format(x[player], x[pc]))
else:
    print('Você escolheu {}, o PC escolheu '
          '{}. \033[1;34m\nYOU WIN!\033[m \033[1;31mPC LOSE!\033[m'.format(x[player], x[pc]))