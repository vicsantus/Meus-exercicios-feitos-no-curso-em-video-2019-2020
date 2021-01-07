from time import sleep
from random import randint
def Maior(* arg):
    maior: int = 0
    print('-='*30)
    print('Analisando valores informados...')
    for c in arg:
        if c > maior:
            maior = c
        sleep(0.5)
        print(c, end=' ')
    print(f'Foram informados {len(arg)} valores.')
    print(f'O maior valor informado foi {maior}.')


Maior(2, randint(1, 50), 15, randint(1, 50), 4, 21)
Maior(4, 7, 0)
Maior(1, 2)
Maior(6)
Maior()