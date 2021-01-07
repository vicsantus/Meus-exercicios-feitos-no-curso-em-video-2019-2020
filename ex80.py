# MANEIRA QUE EU FIZ O CODIGO
'''num1 = list()
for c in range(0, 5):
    num2 = int(input('Digite um valor: '))
    if len(num1) == 0:
        num1.append(num2)
    elif num2 >= max(num1):
        num1.append(num2)
    elif num2 <= min(num1):
        num1.insert(0, num2)
    elif min(num1) < num2 < max(num1):
        cont = 1
        while True:
            if num2 <= num1[cont]:
                num1.insert(cont, num2)
                break
            else:
                cont += 1
print(num1)'''
# MANEIRA QUE O PROFESSOR FEZ
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')