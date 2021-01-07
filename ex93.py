jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
qtpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for q in range(0, qtpartidas):
    gols.append(int(input(f'Quantos gols na partida {q+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])
print('-='*25)
print(f'O jogador {jogador["nome"]} jogou {qtpartidas} partidas.')
for q in range(0, len(gols)):
    print(f'Na {q+1}ª partida, fez {gols[q]} gols.')
print(f'Foi um total de {jogador["total"]} gol(s).')