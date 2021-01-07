print('Você vai escrever o peso de 5 pessoas. O programa vai adivinhar o maior peso.')
v = 0
for r in range(0, 5):
    peso = float(input('Digite o peso: '))
    if peso >= v:
        v = peso
print('O maior peso foi {}Kg.'.format(v))