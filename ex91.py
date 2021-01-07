from random import randint
from time import sleep
from operator import itemgetter
'''
lvalores = []
dado = {}

for j in range(0, 4):
    print('SORTEANDO DADOS!')
    valor = randint(1, 6)
    sleep(1)
    print(f'Foi sorteado o valor {valor}')
    dado['jogador']: int = j+1
    dado['valor']: int = valor

    if len(lvalores) == 0 or valor >= lvalores[-1]['valor']:
        lvalores.append(dado.copy())
    else:
        print(lvalores)
        for l in range(0, len(lvalores)):
            if valor > lvalores[l]['valor'] and valor <= lvalores[l+1]['valor']:
                lvalores.insert(l+1, dado.copy())

    dado.clear()

print(lvalores)
for k in range(0, 4):
    print(f'Em {k+1}º lugar o jogador {lvalores[k]["jogador"]}, atingiu {lvalores[k]["valor"]} pontos')
'''
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = {}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-x'*20)
for c in range(0, 4):
    print(f'Em {c+1}º lugar o {ranking[c][0]} tirou {ranking[c][1]} ponto(s).')