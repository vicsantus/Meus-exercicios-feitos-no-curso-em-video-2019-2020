valor = ('P�o', 1.4, 'Batata', 3.8, 'Xereca', 80,
         'DVD veloses e furiosos', 10, 'Cora��o humano', 0.5, 'DVD Furac�o 2000', -6.0, 'Consolo Black Neg�o', 24)
for c in range(0, len(valor), 2):
    print(f'{valor[c]:.<35}R${valor[c+1]:>6.2f}')