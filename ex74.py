from random import randint
n1 = randint(0, 100000000)
n2 = randint(0, 10000000)
n3 = randint(0, 1000000)
n4 = randint(0, 10000000)
n5 = randint(0, 100000000)
trompa = (n1, n2, n3, n4, n5)
print('Os valores da tupla são: ', end=' ')
for c in trompa:
    print(f'{c}', end=' ')
print(f'\n{sorted(trompa)}')
print(f'O maior valor sorteado foi {max(trompa)}.')
print(f'O menor valor sorteado foi {min(trompa)}.')