prim = int(input('Digite o primeiro termo da P.A.: '))
raz = int(input('Digite a raz�o da P.A.: '))
dec = prim + (10 - 1) * raz
for c in range(prim, dec + raz, raz):
    print(c)
print('FIM!!!!')