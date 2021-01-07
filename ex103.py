def ficha(nome='', gols=0):
    if gols == '' or gols == str(gols):
        gols = 0
    if nome == '' or nome.isnumeric():
        nome = '<desconhecido>'
    print('--' * 20)
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nm = input('Nome do jogador: ').title().strip()
gol = int(input('Número de gols: '))
print(ficha(nm, gol))