soma = 0
for c in range(0, 6):
    n = int(input('Digite um n�mero: '))
    if n % 2 == 0:
        soma += n
print('Valor total � {}.'.format(soma))