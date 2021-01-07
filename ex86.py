# minha solução funciona, porém a do prof é mais legal
'''matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
linha = 0
coluna = 0
for c in range(0, 9):
    num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    matriz[linha][coluna].append(num)
    coluna += 1
    if coluna >= 3:
        coluna = 0
        linha += 1
print(matriz[0])
print(matriz[1])
print(matriz[2])'''
# solução do profe
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*18)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^9}]', end='')
    print()