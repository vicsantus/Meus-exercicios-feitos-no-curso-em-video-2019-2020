def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n1 = int(input('Digite um n�mero: '))
print(f'O fatorial de {n1} � igual a {fatorial(n1)}')