from time import sleep
from random import randint
palpite = []
temp = []
qto = int(input('Quantos jogos você quer criar?: '))
for c in range(0, qto):
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if temp.count(num) == 0:
            temp.append(num)
            temp.sort()
            cont += 1
    palpite.append(temp[:])
    temp.clear()
for c in range(0, qto):
    print(f'{c+1}º jogo: {palpite[c]}')
    sleep(0.5)