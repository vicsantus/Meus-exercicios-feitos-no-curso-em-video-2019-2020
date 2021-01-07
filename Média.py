mediarep = float(input('A média de quantos valores você quer calcular?: '))
numedia = mediarep
val = 0
nx = 0
while mediarep > 0:
    nx = float(input('\nDigite o valor {:.0f}: '.format(mediarep)))
    nx = nx + val
    val = nx
    mediarep -= 1
med = nx / numedia
print('\nO valor da média é: {:.2f}.'.format(med))