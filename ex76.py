valor = ('Pão', 1.4, 'Batata', 3.8, 'Xereca', 80,
         'DVD veloses e furiosos', 10, 'Coração humano', 0.5, 'DVD Furacão 2000', -6.0, 'Consolo Black Negão', 24)
for c in range(0, len(valor), 2):
    print(f'{valor[c]:.<35}R${valor[c+1]:>6.2f}')