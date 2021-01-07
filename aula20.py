'''def Soma(a: int, b: int):
    s = a + b
    print(f'O valor de A é {a} e o valor de B é {b}.')
    print(f'Valor da soma é {s}.')


Soma(
    int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: '))
)'''
'''def contador(*num):
    print(sum(num))


contador(2, 1, 7, 5, 6, 14)
contador(8, 8)'''


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 12, 16]
dobra(valores)
print(valores)