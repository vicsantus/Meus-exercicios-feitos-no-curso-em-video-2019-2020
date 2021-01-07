matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
linha = coluna = soma = somaterceiracoluna = maiorseg = 0
for c in range(0, 9):
    num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    if num % 2 == 0:
        soma += num
    matriz[linha][coluna].append(num)
    if coluna == 2:
        somaterceiracoluna += num
    if linha == 1:
        if num >= maiorseg:
            maiorseg = num
    coluna += 1
    if coluna >= 3:
        coluna = 0
        linha += 1
print('-='*30)
print(f'A soma dos pares é igual a: \033[31m{soma}\033[m')
print(f'A soma dos valores da terceira coluna é igual a: \033[31m{somaterceiracoluna}\033[m')
print(f'O maior valor da segunda linha é: \033[31m{maiorseg}\033[m')
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-='*30)