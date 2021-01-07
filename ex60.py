num = int(input('Digite um número: '))
val = num
cont = num
fat = 0
resultado = 1
while cont != 0:
    fat = val - 1
    resultado = fat * val * resultado
    val -= 2
    if val <= 1:
        cont = 0
print('O fatorial de {} é igual a {}.'.format(num, resultado))