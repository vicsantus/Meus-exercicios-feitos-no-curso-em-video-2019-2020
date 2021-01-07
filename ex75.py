n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tropa = (n1, n2, n3, n4)
print(f'Voce digitou os valores {tropa}')
print(f'O valor 9 apareceu {tropa.count(9)} vezes.')
if 3 in tropa:
    print(f'O valor 3 apareceu na {tropa.index(3)+1}ª posição.')
else:
    print(f'O número 3 não apareceu em nenhuma posição.')
print('O valores pares digitados foram ', end='')
if n1 % 2 == 0:
    print(n1, end='')
if n2 % 2 == 0:
    print(n2, end=' ')
if n3 % 2 == 0:
    print(n3, end=' ')
if n4 % 2 == 0:
    print(n4, end=' ')